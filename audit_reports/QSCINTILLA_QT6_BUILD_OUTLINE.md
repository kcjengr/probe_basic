# QScintilla Qt6 Build Outline (Lean Path)

Date: 2026-02-28  
Target: Replace current `GcodeTextEdit` with a Qt6-compatible Scintilla-backed editor path for large-file performance.

---

## 1) Revised Effort (Lean, Realistic)

Assumptions:
- Existing UI/logic stays mostly intact.
- We do not chase full feature parity in phase 1.
- We keep current editor as fallback during rollout.

Estimated effort:
- **MVP (load, line numbers, current line, jump/run-from-line, basic styling): 3–5 dev days**
- **Operational parity (find/replace, settings bridge, robust edge cases): +3–5 dev days**
- **Optional polish (custom lexer, perf tuning, migration cleanup): +3–7 dev days**

Total practical range: **~1 to 3 weeks**, depending on depth.

---

## 2) Build Strategy

## Phase A — Spike / Feasibility (0.5–1 day)

Goal: Verify Qt6 + QScintilla package/build is working in your environment.

Tasks:
1. Install Qt6-compatible QScintilla package in dev env.
2. Instantiate a minimal editor widget in a standalone test.
3. Verify large file load (e.g., 35MB) and scroll behavior.
4. Confirm line-number margin + line highlight API behavior.

Exit criteria:
- Widget launches in app runtime environment.
- Basic load + scroll works without crash.

---

## Phase B — Drop-in Wrapper (1–2 days)

Goal: Introduce a compatibility wrapper so existing app code changes are minimal.

Create `GcodeScintillaEdit` wrapper with compatibility methods/signals mirroring current usage:

Required API compatibility:
- `loadProgramFile(fname)`
- `setCurrentLine(line)`
- `getCurrentLine()`
- `saveFile(...)`, `saveFileAs(...)` (or delegated)
- `focusLine` signal (emit on cursor/line change)
- `runFromHere()` callback path

Core editor features in wrapper:
- read-only/editable toggle
- line numbers margin
- current line highlight
- no-wrap monospaced rendering
- keyboard up/down centered-ish behavior (or simplified)

Exit criteria:
- Wrapper can substitute current editor in one screen behind a feature flag.

---

## Phase C — Integrate with Existing Load/Run Path (1 day)

Goal: Wire to existing status/program actions without redesign.

Tasks:
1. Connect status file notifications to wrapper load.
2. Keep `run-from-line` action binding in place.
3. Keep existing signals to backplot (`focusLine`) unchanged.
4. Use feature flag:
   - `editor.backend = "qtextedit" | "qscintilla"`

Exit criteria:
- Program loads and run-from-line works via new widget.

---

## Phase D — Styling Bridge (0.5–1.5 days)

Goal: Preserve your current styling controls where possible.

Tasks:
1. Map existing font settings:
   - editor family/size/weight
   - margin family/size/weight
2. Map colors:
   - current line background/foreground
   - margin normal/active colors
3. Replace unsupported QSS-dependent settings with explicit setter methods.

Note:
- Scintilla styling is API-driven more than QSS-driven.

Exit criteria:
- Looks close to current theme with known, documented differences.

---

## Phase E — Search/Replace + Navigation Parity (1–2 days)

Goal: Match practical workflow parity.

Tasks:
1. Find next/prev with case/word options.
2. Replace/replace-all.
3. Highlight all matches (if needed for UX parity).
4. Jump to line and keep line marker/highlight in sync.

Exit criteria:
- Daily operator flows pass using new editor.

---

## 3) Technical Design Notes

## Keep this unchanged (reduce risk)
- LinuxCNC `program_actions.load()` behavior.
- VTK load path.
- Existing action names/signals in higher-level screens.

## Change only at editor boundary
- Replace current `GcodeTextEdit` internals with a compatibility layer.
- Avoid widespread `.ui` rewiring initially; use one custom class replacement path.

## Feature flag rollout
- Default to old widget until confidence is high.
- Enable new widget per-machine or per-config.

---

## 4) Minimal Deliverable Definition (MVP)

MVP is complete when:
1. 35MB file opens in new editor.
2. Scroll/jump-to-line are responsive.
3. Current line + line numbers visible.
4. Run-from-line uses selected/current line.
5. No regressions in load/run workflow.

Non-goals in MVP:
- Perfect QSS parity.
- Full custom G-code lexer sophistication.
- Advanced visual extras.

---

## 5) Risk Register (Lean)

1. Qt6 package friction for QScintilla in your distro.
   - Mitigation: spike first, fallback to wrapper C++ build if needed.

2. Designer integration mismatch.
   - Mitigation: keep fallback widget and use runtime replacement path.

3. Styling differences from QTextEdit/QSS model.
   - Mitigation: explicit style mapping API + doc of accepted deltas.

---

## 6) Suggested First Week Plan

Day 1:
- Feasibility spike + package verification.

Day 2:
- Implement wrapper skeleton + line numbers/current line.

Day 3:
- Load/status integration + run-from-line compatibility.

Day 4:
- Styling bridge + basic find/replace.

Day 5:
- Large-file test pass + bugfix + feature flag packaging.

---

## 7) Recommendation

Proceed with a **feature-flagged, compatibility-wrapper migration** to QScintilla.

This keeps schedule short, risk contained, and gives measurable performance gains quickly without a broad architectural rewrite.
