# Full C++ Backplot Rewrite - File Edit List

Goal: build a new C++ backplot pipeline on a fresh branch, keep current Python flow as control, benchmark, then decide merge.

## 1) Branch and repo layout

- Create branch in `qtpyvcp` for all runtime/widget changes.
- Create matching branch in `probe_basic` for settings/UI and launch integration.
- Keep the current Python backplot code present as fallback until benchmark sign-off.

## 2) Existing files to edit (qtpyvcp)

1. `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/vtk_backplot.py`
   - Replace Python geometry build path (`VTKCanon + draw_lines`) with calls into C++ builder bridge.
   - Keep camera, renderer, actor attach, offsets, and UI signal wiring in Python initially.
   - Preserve perf timing stamps and summary update calls.

2. `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/vtk_canon.py`
   - Mark as legacy/fallback path.
   - Remove from primary execution path in `vtk_backplot.py`.

3. `qtpyvcp/src/qtpyvcp/widgets/display_widgets/vtk_backplot/base_canon.py`
   - Keep only if needed for fallback.
   - Add clear deprecation note for full C++ branch.

4. `qtpyvcp/src/qtpyvcp/utilities/load_perf_summary.py`
   - Keep stage names and timestamps stable.
   - Ensure C++ bridge returns parse/build timings so summary rows remain compatible.

5. `qtpyvcp/src/qtpyvcp/actions/program_actions.py`
   - No semantic change expected.
   - Confirm timing phase sequence remains valid with C++ backplot path.

## 3) New C++ runtime files (qtpyvcp)

Create a new native module folder:

- `qtpyvcp/src/qtpyvcp/native/backplot_cpp/CMakeLists.txt`
- `qtpyvcp/src/qtpyvcp/native/backplot_cpp/backplot_builder.h`
- `qtpyvcp/src/qtpyvcp/native/backplot_cpp/backplot_builder.cpp`
- `qtpyvcp/src/qtpyvcp/native/backplot_cpp/backplot_types.h`
- `qtpyvcp/src/qtpyvcp/native/backplot_cpp/backplot_bridge_pybind.cpp` (or SIP/Shiboken equivalent)

Responsibilities:
- Parse canonical motion stream or consume pre-parsed segment stream.
- Build VTK geometry buffers in C++ (points/cells/colors) with minimal Python object churn.
- Return per-WCS outputs and offset transition metadata.
- Return timing struct: parse_ms, geometry_ms, actor_build_ms, total_ms.

## 4) Build + packaging files to edit (qtpyvcp)

- `qtpyvcp/pyproject.toml`
  - Add native extension build config.
- `qtpyvcp/MANIFEST.in`
  - Include native sources/artifacts as needed.
- `qtpyvcp/requirements.txt` (only if adding new build/runtime dependency).
- `qtpyvcp/package_dependencies.sh` (if native build deps required in your packaging flow).

## 5) Existing files to edit (probe_basic)

1. `probe_basic/src/probe_basic/probe_basic.yml`
   - Add one explicit toggle for experimental C++ backplot path (branch-only), default off.

2. `probe_basic/src/probe_basic/menubar.yml` (optional)
   - Add debug toggle under View/Tools only for branch testing.

3. `probe_basic/configs/probe_basic/*.ini` (if needed)
   - Add optional env/settings switch for branch experiments.

## 6) New validation/benchmark files

- `qtpyvcp/scripts/bench_backplot_cpp_vs_python.py`
  - Run N loads on same file; output median/p95 for parse/build/total.
- `probe_basic/audit_reports/CPP_BACKPLOT_BENCH_RESULTS.md`
  - Track side-by-side results and correctness notes.

## 7) Correctness gates before merge decision

- Toolpath visual parity (line count, bounds, offset transitions).
- No regression in active WCS transforms.
- Summary timing stamps remain monotonic and consistent.
- Crash/exception behavior equivalent or improved.
- Target improvement threshold agreed in advance (for example: >=25% total load reduction on large files).

## 8) Recommended implementation order

1. Add native module skeleton + Python import stub.
2. Implement C++ geometry builder and timing outputs.
3. Switch `vtk_backplot.py` primary path to C++ builder.
4. Keep Python path as fallback behind branch toggle.
5. Benchmark, fix correctness deltas, then decide merge strategy.
