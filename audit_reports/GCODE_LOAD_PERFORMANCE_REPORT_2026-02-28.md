# G-code Program Load Performance Report

Date: 2026-02-28  
Project: Probe Basic (QtPyVCP, Qt6/PySide6)  
Scope: End-to-end program load latency for large G-code files (~35 MB), including LinuxCNC load, GcodeTextEdit behavior, and VTK backplot generation.

---

## 1) Executive Summary

Large-file program load is currently slowed by a combination of:

1. **Synchronous LinuxCNC load/wait** (`program_open` + `wait_complete`) on the UI path.
2. **Duplicate/expensive front-end work** after load (multiple editor consumers, full-document rebuild/format passes).
3. **Heavy VTK rebuild cost** (full parse + high-volume Python/VTK object creation per load).
4. **Extra pre-load file reads** in file browser selection logic.

For very large files, these costs stack in series and can produce multi-minute load times.

---

## 2) Current End-to-End Load Flow

### User action to LinuxCNC load

1. User clicks main load button.
2. UI signal routes to file table load handler.
3. Handler calls `program_actions.load(...)`.
4. `program_actions.load(...)` calls LinuxCNC `program_open(...)` and blocks on `wait_complete()`.

Relevant locations:

- `probe_basic/src/probe_basic/probe_basic_ui.py` (main load button connection)
- `qtpyvcp/src/qtpyvcp/widgets/input_widgets/file_system.py` (`loadSelectedFile`, `openSelectedItem`)
- `qtpyvcp/src/qtpyvcp/actions/program_actions.py` (`load`)

### Post-load fanout on status file update

After LinuxCNC reports the loaded file (`status.file`), multiple components react:

1. `GcodeTextEdit` loads full file text and rebuilds document.
2. VTK data source emits `programLoaded`.
3. `VTKBackPlot.load_program(...)` re-parses and reconstructs path actors.

Relevant locations:

- `qtpyvcp/src/qtpyvcp/widgets/input_widgets/gcode_text_edit.py`
- `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/linuxcnc_datasource.py`
- `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/vtk_backplot.py`
- `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/base_backplot.py`
- `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/vtk_canon.py`

---

## 3) Bottleneck Analysis

## A. LinuxCNC boundary (expected baseline cost)

- `program_actions.load()` performs `CMD.program_open(...)` then `CMD.wait_complete()`.
- This enforces synchronous completion before UI unlock.
- Some load time here is unavoidable and interpreter-dependent.

Impact: **High baseline** for large files.

## B. File browser selection pre-read overhead

`FileSystemTable.onSelectionChanged()` currently reads full selected file contents (encoding probe loop + full `read()`) even before user clicks Load.

Impact: **Medium to High** (wasted I/O and decoding for large files).

## C. Editor-side full rebuild work

`GcodeTextEdit.loadProgramFile()`:

- tries many encodings,
- reads whole file into memory,
- calls custom `setPlainText` that creates a new `QTextDocument`,
- applies document font and block formatting passes.

Potential multipliers:

- two `GcodeTextEdit` widgets in UI can both respond to file changes,
- `old_docs` keeps prior documents alive (memory pressure over repeated loads),
- line-height merge over full doc is expensive on huge text.

Impact: **High** for large files and repeated loads.

## D. VTK backplot rebuild costs

`VTKBackPlot.load_program(...)`:

- constructs fresh canon,
- calls `BaseBackPlot.load()` which performs full `gcode.parse(...)`,
- rebuilds geometry/path actors,
- loops many segments with Python-level point/line insertion.

Additionally, there are UI thread render/update operations and actor churn after parse.

Impact: **Very High** for dense/long programs.

---

## 4) Prioritized Optimization Plan

## Priority 1 (Fastest ROI, lowest risk)

### 1. Stop full-file reads during selection preview

- In `file_system.py`, avoid full `read()` for `onSelectionChanged` unless preview is actually wired and file is below threshold (for example 256 KB–1 MB).
- For large files, emit filename only (or limited preview chunk).

Expected gain: **Immediate reduction in unnecessary I/O and decode churn**.

### 2. Prevent duplicate editor load work

- Confirm only visible/active `GcodeTextEdit` loads large text at startup.
- Lazy-load secondary editor instances when user opens the relevant tab.

Expected gain: **Potential near-2x editor-side reduction** where duplicate listeners exist.

### 3. Bound document retention memory

- Replace unbounded `old_docs` growth with bounded queue (for example keep last 1–2 docs) or explicit cleanup strategy.

Expected gain: **Stability + reduced GC/memory pressure** over long sessions.

### 4. Large-file fast path in `GcodeTextEdit`

- For files above threshold:
  - skip expensive full-document formatting passes on first paint,
  - defer optional styling/highlight operations until idle.

Expected gain: **Substantial perceived load improvement**.

## Priority 2 (High ROI, medium risk)

### 5. VTK geometry build optimization

- Reduce Python object churn in `draw_lines()`:
  - batch populate points/connectivity where possible,
  - avoid per-line allocations where VTK arrays can be pre-sized.
- Add optional decimation/fast mode for initial preview, refine after first display.

Expected gain: **Major reduction in backplot build time on large programs**.

### 6. Avoid unnecessary datasource/canon recreation churn

- Review whether new `LinuxCncDataSource` in `VTKCanon` per load is required.
- Reuse shared datasource where safe.

Expected gain: **Lower overhead and fewer signal connections**.

## Priority 3 (Responsiveness and UX)

### 7. Stage heavy work with progress and cancellation

- Keep LinuxCNC load as-is where required, but decouple editor and VTK post-processing from a single blocking UI phase.
- Show “program loaded” state early, build heavy visuals progressively.

Expected gain: **Better operator experience even if absolute runtime unchanged**.

---

## 5) Measurement and Validation Plan

To avoid guesswork, instrument each stage with timings.

Suggested timing points:

1. Button click → `program_actions.load` entry.
2. `program_open` start/end.
3. `wait_complete` duration.
4. `status.file` signal to each `GcodeTextEdit.loadProgramFile` start/end.
5. `VTKBackPlot.load_program` total.
6. Internal split:
   - `gcode.parse` duration,
   - `VTKCanon.draw_lines` duration,
   - actor add/render duration.

Metrics to track:

- total load time,
- time to first responsive UI,
- peak RSS memory,
- number of active `GcodeTextEdit` loaders.

Acceptance target examples:

- 35 MB file total load reduction by at least 40–60%,
- time-to-first-usable-UI under 10–20 seconds,
- no regressions in toolpath correctness.

---

## 6) Recommended Implementation Sequence (Team-Friendly)

Sprint 1:

- P1.1 selection preview guard
- P1.2 single-active editor load
- P1.3 bounded `old_docs`
- baseline timing logs

Sprint 2:

- P1.4 large-file editor fast path
- early/idle deferred formatting
- compare timing delta

Sprint 3:

- P2.5 VTK draw optimization pass
- optional fast/decimated backplot mode
- compare timing delta

Sprint 4:

- P3 staged loading UX and cancellation
- hardening + rollback toggles (feature flags)

---

## 7) Risks and Mitigations

1. **Rendering correctness risk (VTK decimation/fast path).**  
   Mitigation: keep full-precision mode default for validation, gate fast mode by setting.

2. **Editor behavior differences for large-file fast path.**  
   Mitigation: apply threshold-based behavior, keep small/normal files unchanged.

3. **Signal/order regressions.**  
   Mitigation: log signal path and add focused smoke tests for load + run + run-from-line.

---

## 8) Notes from Current Session

- The attached sample (`bracket_fixture_top.ngc`) is small (~87 KB, 4230 lines) and not representative of the reported 35 MB issue.
- Prior reported behavior (up to ~15 minutes for large files) is consistent with cumulative sync parse + multi-consumer UI work + VTK rebuild costs.

---

## 9) Conclusion

The best path is **not** a full rewrite first. The highest-value approach is:

1. remove unnecessary pre-load and duplicate editor work,
2. add large-file fast path in `GcodeTextEdit`,
3. optimize VTK build path with batched operations and optional decimated preview,
4. stage heavy post-load work for responsiveness.

This sequence minimizes risk, delivers measurable improvements quickly, and preserves current behavior for normal-size programs.
