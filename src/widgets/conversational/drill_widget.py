from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QLabel, QLineEdit

from qtpyvcp.utilities import logger

from .base_widget import ConversationalBaseWidget
from .base_widget import _is_qt_valid


LOG = logger.getLogger(__name__)


class DrillWidgetBase(ConversationalBaseWidget):
    def __init__(self, ui, parent=None):
        super(DrillWidgetBase, self).__init__(ui, parent)

        self._feed_sync_in_progress = False
        self._last_feed_source = 'z_feed'
        self.feed_per_rev_input = None

        if self.drill_retract_mode_input.count() == 0:
            self.drill_retract_mode_input.addItem('G98')
            self.drill_retract_mode_input.addItem('G99')

        if self.drill_type_input.count() == 0:
            self.drill_type_input.addItem('DRILL')
            self.drill_type_input.addItem('PECK')
            self.drill_type_input.addItem('BREAK')
            self.drill_type_input.addItem('DWELL')
            self.drill_type_input.addItem('TAP')
            self.drill_type_input.addItem('RIGID TAP')
            self.drill_type_input.addItem('MANUAL')
        self.drill_type_param_value.setVisible(False)
        self.drill_type_param_label.setVisible(False)
        self.drill_type_input.currentIndexChanged.connect(self.set_drill_type_params)
        self.drill_type_input.currentIndexChanged.connect(self._log_drill_type_signal)

        LOG.debug(
            "drill_type_input class=%s object=%s",
            type(self.drill_type_input).__name__,
            self.drill_type_input.objectName(),
        )

        self.z_feed_rate_input.setEnabled(True)
        self.set_drill_type_params(None)

        # Defer two-way feed sync setup until the event loop is running to avoid
        # raising from custom-widget construction during QUiLoader startup.
        QTimer.singleShot(0, self._init_feed_sync_safe)

    def drill_type(self):
        return self.drill_type_input.currentText()

    def drill_peck_depth(self):
        return self.drill_type_param_value.value()

    def drill_break_depth(self):
        return self.drill_type_param_value.value()

    def drill_dwell_time(self):
        return self.drill_type_param_value.value()

    def tap_pitch(self):
        return self.drill_type_param_value.value()

    def retract_mode(self):
        return self.drill_retract_mode_input.currentText()

    def _init_feed_sync_safe(self):
        try:
            self.feed_per_rev_input = self._resolve_feed_per_rev_input()
            if self.feed_per_rev_input is None:
                return
            if not hasattr(self.feed_per_rev_input, 'editingFinished'):
                return

            if _is_qt_valid(getattr(self, 'z_feed_rate_input', None)):
                self.z_feed_rate_input.editingFinished.connect(self._on_z_feed_edited)

            if _is_qt_valid(getattr(self, 'spindle_rpm_input', None)):
                self.spindle_rpm_input.editingFinished.connect(self._on_spindle_rpm_edited)

            self.feed_per_rev_input.editingFinished.connect(self._on_fpr_edited)

            self._sync_feed_from_existing_values()
        except Exception:
            LOG.exception("Drill feed sync initialization failed; leaving widgets independent")

    def _resolve_feed_per_rev_input(self):
        for name in ('feed_per_rev_input', 'xy_coord_feed_per_rev', 'hole_circle_feed_per_rev'):
            widget = getattr(self, name, None)
            if widget is not None:
                return widget
        return None

    def _numeric_value(self, widget, default=0.0):
        if widget is None:
            return default
        try:
            return float(widget.value())
        except Exception:
            try:
                return float(widget.text())
            except Exception:
                return default

    def _set_numeric_value(self, widget, value):
        if widget is None:
            return
        try:
            widget.setValue(float(value))
        except Exception:
            try:
                widget.setText('{:.4f}'.format(float(value)))
            except Exception:
                pass

    def _sync_feed_from_existing_values(self):
        rpm = self._numeric_value(getattr(self, 'spindle_rpm_input', None))
        z_feed = self._numeric_value(getattr(self, 'z_feed_rate_input', None))
        fpr = self._numeric_value(self.feed_per_rev_input)

        if rpm <= 0:
            return

        if z_feed > 0 and fpr <= 0:
            self._on_z_feed_edited()
        elif fpr > 0 and z_feed <= 0:
            self._on_fpr_edited()

    def _on_z_feed_edited(self):
        try:
            self._last_feed_source = 'z_feed'
            if self._feed_sync_in_progress:
                return

            rpm = self._numeric_value(getattr(self, 'spindle_rpm_input', None))
            if rpm <= 0:
                return

            z_feed = self._numeric_value(getattr(self, 'z_feed_rate_input', None))

            self._feed_sync_in_progress = True
            self._set_numeric_value(self.feed_per_rev_input, z_feed / rpm)
        except Exception:
            LOG.exception("Failed updating feed/rev from Z feed")
        finally:
            self._feed_sync_in_progress = False

    def _on_fpr_edited(self):
        try:
            self._last_feed_source = 'feed_per_rev'
            if self._feed_sync_in_progress:
                return

            rpm = self._numeric_value(getattr(self, 'spindle_rpm_input', None))
            if rpm <= 0:
                return

            fpr = self._numeric_value(self.feed_per_rev_input)

            self._feed_sync_in_progress = True
            self._set_numeric_value(getattr(self, 'z_feed_rate_input', None), fpr * rpm)
        except Exception:
            LOG.exception("Failed updating Z feed from feed/rev")
        finally:
            self._feed_sync_in_progress = False

    def _on_spindle_rpm_edited(self):
        if self._last_feed_source == 'feed_per_rev':
            self._on_fpr_edited()
        else:
            self._on_z_feed_edited()

    def _resolve_drill_param_widgets(self):
        label = getattr(self, 'drill_type_param_label', None)
        value = getattr(self, 'drill_type_param_value', None)

        # Cached references can become stale when Qt re-parents/rebuilds pages.
        if not _is_qt_valid(label):
            label = None
        if not _is_qt_valid(value):
            value = None

        if label is None and hasattr(self, 'findChild'):
            label = self.findChild(QLabel, 'drill_type_param_label')

        if value is None and hasattr(self, 'findChild'):
            value = self.findChild(QLineEdit, 'drill_type_param_value')

        if not _is_qt_valid(label):
            label = None
        if not _is_qt_valid(value):
            value = None

        if label is not None:
            self.drill_type_param_label = label
        if value is not None:
            self.drill_type_param_value = value

        return label, value

    def _log_drill_type_signal(self, *_):
        try:
            LOG.info(
                "drill_type signal idx=%s text=%s",
                self.drill_type_input.currentIndex(),
                self.drill_type_input.currentText(),
            )
        except Exception:
            LOG.exception("Failed logging drill_type signal")

    def set_drill_type_params(self, _=None):
        if not _is_qt_valid(getattr(self, 'drill_type_input', None)):
            LOG.debug("set_drill_type_params skipped: drill_type_input invalid")
            return
        label, value = self._resolve_drill_param_widgets()
        if label is None:
            LOG.debug("set_drill_type_params skipped: drill_type_param_label not found")
            return
        if value is None:
            LOG.debug("set_drill_type_params skipped: drill_type_param_value not found")
            return
        if not _is_qt_valid(label):
            LOG.debug("set_drill_type_params skipped: drill_type_param_label invalid")
            return
        if not _is_qt_valid(value):
            LOG.debug("set_drill_type_params skipped: drill_type_param_value invalid")
            return
        if not _is_qt_valid(getattr(self, 'z_feed_rate_input', None)):
            LOG.debug("set_drill_type_params skipped: z_feed_rate_input invalid")
            return

        drill_type = str(self.drill_type()).strip().upper()
        drill_idx = self.drill_type_input.currentIndex()
        # Fallback to index mapping in case text values are overridden/translated.
        if drill_type not in ['DRILL', 'PECK', 'BREAK', 'DWELL', 'TAP', 'RIGID TAP', 'MANUAL']:
            drill_type_by_idx = {
                0: 'DRILL',
                1: 'PECK',
                2: 'BREAK',
                3: 'DWELL',
                4: 'TAP',
                5: 'RIGID TAP',
                6: 'MANUAL',
            }
            drill_type = drill_type_by_idx.get(drill_idx, drill_type)

        try:
            self.z_feed_rate_input.setEnabled(True)
            if drill_type == 'DWELL':
                label.setText('DWELL TIME (SEC.)')
                value.setText('0.00')
                value.setVisible(True)
                label.setVisible(True)
            elif drill_type == 'PECK':
                label.setText('PECK DEPTH')
                value.setText('0.0000')
                value.setVisible(True)
                label.setVisible(True)
            elif drill_type == 'BREAK':
                label.setText('BREAK DEPTH')
                value.setText('0.0000')
                value.setVisible(True)
                label.setVisible(True)
            elif drill_type in ['TAP', 'RIGID TAP']:
                self.z_feed_rate_input.setEnabled(False)
                label.setText('PITCH')
                value.setText('0.0000')
                value.setVisible(True)
                label.setVisible(True)
            else:
                value.setVisible(False)
                label.setVisible(False)
        except RuntimeError:
            LOG.debug("set_drill_type_params skipped: parameter widgets deleted during update")
            return

        LOG.debug(
            "drill_type=%s idx=%s combo_class=%s param_visible=%s label_visible=%s",
            drill_type,
            drill_idx,
            type(self.drill_type_input).__name__,
            value.isVisible(),
            label.isVisible(),
        )
