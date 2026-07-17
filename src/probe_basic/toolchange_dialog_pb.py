# coding=utf-8
"""Probe Basic manual tool change dialog.

Subclass of qtpyvcp's ToolChangeDialog that words the prompt for what the
operator actually has to do. The base dialog always says "Insert tool", but
the toolchange.ngc removal branch (manual-only ATC=0 tools, or a full
carousel) uses the same dialog to ask the operator to take a tool OUT of the
spindle -- with the stock wording that showed up as a confusing
"Insert tool 0" prompt.

No new HAL pins: the mode is inferred from the pins the base dialog already
listens to. The removal branch of toolchange.ngc prepares the tool being
removed (T#<tool_in_spindle>), so when the prepared tool number matches the
tool currently in the spindle the change request can only mean "remove it".
A prepared tool of 0 while a tool is in the spindle (older macros that prep
T0 to mean "empty the spindle") is treated as a removal too, and the labels
are rewritten to name the real tool instead of T0. Anything else is a
normal load prompt, same as the base dialog.

The remove prompt is deliberately louder than the load prompt: blindly
pressing resume without physically removing the tool means the next store
attempt could stuff an oversize tool into the carousel -- a crash. In
remove mode the main prompt (label_1) is replaced with a bright red
warning sentence naming the cause: the spindle tool's ATC flag unchecked
(non storable), or a full carousel (no open pocket). The flag is read via
the tool table plugin's getToolExtras and defaults to storable whenever it
can't be read (file-based tool table configs, no extras row, DB error) --
the same default as _lookup_tool_atc in stdglue.py, so the dialog's
explanation always matches why the macro actually routed the change to the
dialog. If the ui file provides a QLabel named lblWarnIcon it is shown in
remove mode with a warning icon (Qt's standard warning triangle unless a
pixmap was set on it in Designer) and hidden for normal loads; the widget
is optional and the dialog works unchanged until it exists.

Drawbar interlock (optional, [ATC]DRAWBAR_MONITOR_PIN in the INI): when a
HAL pin or signal name is configured, the resume button starts DISABLED on
a manual removal and only enables after the drawbar has been actuated AND
released while the dialog is up -- physical evidence the tool actually came
out of the spindle before the change is allowed to complete. The pin is
read with hal.get_value() (no HAL pins are created), sampled by the
dialog's existing 100ms poll, so it works for any readable pin or signal:
point it at the drawbar button input, the solenoid drive signal, whatever
reflects actuation on the machine. The HAL change_button path (physical
resume button) is gated too, via accept(). Deliberately fail-open: if the
configured name can't be read the button enables and the problem is
logged -- a typo in the INI must never strand the operator mid-change with
a dead resume button. Manual LOADS are not gated, only removals. Unset =
no gate, exactly the old behavior.
"""

import os

from PySide6.QtWidgets import QStyle

from qtpyvcp.plugins import getPlugin
from qtpyvcp.utilities import logger
from qtpyvcp.widgets.dialogs.toolchange_dialog import ToolChangeDialog

LOG = logger.getLogger(__name__)

# LinuxCNC's own hal module (not qtpyvcp.hal): provides get_value() for
# reading arbitrary pins/signals without creating a HAL component
try:
    import hal as machine_hal
except ImportError:
    machine_hal = None

try:
    import linuxcnc
    _ini_path = os.getenv('INI_FILE_NAME')
    INIFILE = linuxcnc.ini(_ini_path) if _ini_path else None
except Exception:
    INIFILE = None

LOAD_PROMPT = 'Tool Change Requested, Insert tool'
LOAD_BUTTON = 'ONCE TOOL IS LOADED - PRESS TO RESUME'
REMOVE_BUTTON = 'ONCE TOOL IS REMOVED - PRESS TO RESUME'

NON_STORABLE_PROMPT = ('Tool in spindle is flagged as non storable, '
                       'Please remove tool from spindle to proceed.')
CAROUSEL_FULL_PROMPT = ('No open carousel pocket to store the tool in the spindle, '
                        'Please remove tool from spindle to proceed.')

# inline stylesheet beats the parent frame's "QLabel { color: white }" rule;
# cleared (back to the frame's white) for normal load prompts
REMOVE_PROMPT_STYLE = 'color: #ff0000;'

WARN_ICON_SIZE = 48


def removal_tool(prepared_tool, spindle_tool):
    """Return the tool number the operator must remove, or None for a load.

    A change request is a removal when a tool is in the spindle and the
    prepared tool is either that same tool (new macro) or T0 (older macros
    that prep T0 to mean "empty the spindle").
    """
    if spindle_tool and spindle_tool > 0 and prepared_tool in (0, spindle_tool):
        return spindle_tool
    return None


class ToolChangeDialogPB(ToolChangeDialog):

    def __init__(self, *args, **kwargs):
        super(ToolChangeDialogPB, self).__init__(*args, **kwargs)

        self._warn_icon_set = False

        # drawbar gate state: armed = a removal is up and the gate applies,
        # pressed = drawbar seen active since arming, satisfied = full
        # press+release cycle observed (or fail-open), button may enable
        self._gate_armed = False
        self._gate_pressed = False
        self._gate_satisfied = False

        self._drawbar_pin = None
        try:
            if INIFILE is not None:
                value = INIFILE.find('ATC', 'DRAWBAR_MONITOR_PIN')
                if value:
                    self._drawbar_pin = value.strip()
        except Exception:
            LOG.exception("Could not read [ATC]DRAWBAR_MONITOR_PIN from the INI")
        if self._drawbar_pin and machine_hal is None:
            LOG.warning("hal module not available, drawbar interlock disabled")
            self._drawbar_pin = None
        if self._drawbar_pin:
            LOG.info("Manual removal drawbar interlock enabled, monitoring %s",
                     self._drawbar_pin)

        # optional abort hook: if the ui file provides a QPushButton named
        # btnAbortChange it becomes an always-enabled program abort (kills
        # the M6 macro; on_abort.ngc drops the dialog request pin and the
        # dialog hides and disarms itself on the next poll). Not populated
        # in the shipped ui -- a stuck change is recoverable from a second
        # terminal via halcmd (see the Carousel ATC Setup doc page).
        abort_button = getattr(self.ui, 'btnAbortChange', None)
        if abort_button is not None:
            abort_button.clicked.connect(self._abort_change)

        try:
            self._status = getPlugin('status')
        except Exception:
            LOG.exception("Could not get status plugin, "
                          "tool change dialog will always show the load prompt")
            self._status = None

    def _spindle_tool(self):
        if self._status is None:
            return None
        try:
            return int(self._status.tool_in_spindle.getValue())
        except Exception:
            LOG.exception("Could not read tool_in_spindle from status plugin")
            return None

    def _tool_is_storable(self, tool_no):
        get_extras = getattr(self.tt, 'getToolExtras', None)
        if get_extras is None:
            return True
        try:
            extras = get_extras(tool_no) or {}
            atc = extras.get('atc')
            return True if atc is None else bool(atc)
        except Exception:
            LOG.exception("Could not read ATC flag for T%s", tool_no)
            return True

    def _set_label(self, name, text):
        widget = getattr(self.ui, name, None)
        if widget is not None:
            widget.setText(text)

    def _set_prompt(self, text, style, wrap):
        label = getattr(self.ui, 'label_1', None)
        if label is None:
            return
        label.setText(text)
        label.setStyleSheet(style)
        # the long warning sentence needs to wrap; the stock one-liners keep
        # the ui file's no-wrap default
        label.setWordWrap(wrap)

    def _ensure_warn_icon(self, label):
        """Fill lblWarnIcon with the Qt standard warning triangle, unless a
        pixmap was already set on it in Designer -- that one wins."""
        if self._warn_icon_set:
            return
        try:
            pixmap = label.pixmap()
            if pixmap is None or pixmap.isNull():
                icon = self.style().standardIcon(QStyle.StandardPixmap.SP_MessageBoxWarning)
                label.setPixmap(icon.pixmap(WARN_ICON_SIZE, WARN_ICON_SIZE))
            self._warn_icon_set = True
        except Exception:
            LOG.exception("Could not set the warning icon on lblWarnIcon")
            self._warn_icon_set = True

    def _abort_change(self):
        try:
            # deferred import: qtpyvcp.actions needs the status plugin at
            # import time, which only exists inside a running VCP
            from qtpyvcp.actions import program_actions
            program_actions.abort()
        except Exception:
            LOG.exception("Could not abort the tool change from the dialog")

    # ------------------------------------------------------------ drawbar gate

    def _set_resume_enabled(self, enabled):
        button = getattr(self.ui, 'btnDone', None)
        if button is not None:
            button.setEnabled(enabled)

    def _arm_gate(self):
        if self._gate_armed:
            return  # prepare_tool and on_change both refresh; arm only once per dialog
        self._gate_armed = True
        self._gate_pressed = False
        self._gate_satisfied = False
        self._set_resume_enabled(False)

    def _disarm_gate(self):
        self._gate_armed = False
        self._gate_pressed = False
        self._gate_satisfied = False
        self._set_resume_enabled(True)

    def _read_drawbar(self):
        try:
            return bool(machine_hal.get_value(self._drawbar_pin))
        except Exception:
            LOG.exception("Could not read drawbar monitor pin %s, "
                          "releasing the interlock", self._drawbar_pin)
            return None

    def _poll_gate(self):
        """One gate sample: enable resume after a full press+release cycle."""
        value = self._read_drawbar()
        if value is None:
            # fail open: never strand the operator with a dead resume button
            self._gate_satisfied = True
            self._set_resume_enabled(True)
        elif value:
            self._gate_pressed = True
        elif self._gate_pressed:
            self._gate_satisfied = True
            self._set_resume_enabled(True)

    def timerEvent(self, timer):
        super(ToolChangeDialogPB, self).timerEvent(timer)
        if not self._gate_armed:
            return
        try:
            change_active = bool(self.change_pin.value)
        except Exception:
            change_active = self.isVisible()
        if not change_active:
            # change request ended (dialog done or aborted): reset for next time
            self._disarm_gate()
        elif not self._gate_satisfied:
            self._poll_gate()

    def accept(self):
        # gates the HAL change_button (physical resume) path too; the ui
        # button can't get here while disabled
        if self._gate_armed and not self._gate_satisfied:
            LOG.warning("Tool change resume blocked: waiting for drawbar "
                        "press and release on %s", self._drawbar_pin)
            return
        super(ToolChangeDialogPB, self).accept()

    # ------------------------------------------------------------ prompt

    def _update_prompt(self):
        remove_tool = removal_tool(self.tool_number, self._spindle_tool())

        warn_icon = getattr(self.ui, 'lblWarnIcon', None)

        if remove_tool is None:
            self._set_prompt(LOAD_PROMPT, '', False)
            self._set_label('btnDone', LOAD_BUTTON)
            if warn_icon is not None:
                warn_icon.hide()
            self._disarm_gate()
            return

        if self._tool_is_storable(remove_tool):
            prompt = CAROUSEL_FULL_PROMPT
        else:
            prompt = NON_STORABLE_PROMPT
        self._set_prompt(prompt, REMOVE_PROMPT_STYLE, True)
        self._set_label('btnDone', REMOVE_BUTTON)

        if remove_tool != self.tool_number:
            # T0 was prepped to mean "empty the spindle": name the real tool
            self._set_label('lblToolNumber', str(remove_tool))
            try:
                tool_data = self.tt.getToolTable().get(remove_tool, {})
                self._set_label('lblToolRemark', tool_data.get('R', 'UNKNOWN'))
            except Exception:
                LOG.exception("Could not look up remark for T%s", remove_tool)

        if warn_icon is not None:
            self._ensure_warn_icon(warn_icon)
            warn_icon.show()

        if self._drawbar_pin:
            self._arm_gate()
        else:
            self._disarm_gate()

    def prepare_tool(self, tool_no):
        super(ToolChangeDialogPB, self).prepare_tool(tool_no)
        self._update_prompt()

    def on_change(self, value=True):
        self._update_prompt()
        super(ToolChangeDialogPB, self).on_change(value)
