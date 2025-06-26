#!/usr/bin/env python

from qtpy.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, 
                           QLabel, QLineEdit, QPushButton, QMessageBox, QGroupBox, 
                           QSizePolicy, QRadioButton, QButtonGroup)
from qtpy.QtCore import Qt
from qtpyvcp.widgets.input_widgets.line_edit import VCPLineEdit
import json
import os
from datetime import datetime
import linuxcnc

# Get INI file for machine units
INIFILE = linuxcnc.ini(os.getenv("INI_FILE_NAME"))

class CustomThreadDialog(QDialog):
    def __init__(self, parent=None, current_values=None, thread_source_type=None):
        super(CustomThreadDialog, self).__init__(parent)
        self.setWindowTitle("Save Custom Thread")
        self.setModal(True)
        self.setMinimumSize(450, 700)
        
        # Get parent's machine units if available, otherwise determine from INI
        if hasattr(parent, 'machine_units'):
            self.machine_units = parent.machine_units
        else:
            self.machine_units = self.get_machine_units()
        
        # Store thread source type for informational display
        self.thread_source_type = thread_source_type
        
        # Track current display units (can be different from machine units)
        self.current_display_units = self.machine_units
        
        # Flag to prevent recursive updates
        self.updating_values = False
        
        # Apply custom stylesheet
        self.setStyleSheet("""
            QDialog {
                background-color: #2e3436;
                color: white;
            }            
            QGroupBox {
                font-family: "Bebas Kai";
                font-size: 12pt;
                font-weight: bold;
                border-style: solid;
                border-color: rgb(186, 189, 182);
                border-width: 2px;
                border-radius: 6px;
                margin-top: 1ex;
                padding: 6px 12px 6px 12px;
                background-color: rgb(100,100,100);
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 11px;
                padding: 0 5px 0 5px;
                color: #ffffff;
                font-family: "Bebas Kai";
                font-size: 11pt;
            }
            QLineEdit, VCPLineEdit {
                font-family: "Bebas Kai";
                font-size: 12pt;
                padding: 5px;
                min-height: 25px;
                max-height: 25px;
                border-style: transparent;
                border-color: rgb(235, 235, 235);
                border-width: 1px;
                border-radius: 5px;
                color: black;
                background: rgb(235, 235, 235);                            
            }
            QLineEdit:focus, VCPLineEdit:focus {
                border-style: solid;
                border-width: 3px;
                border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));
            }
            QPushButton {
                color: white;    
                border-color: black;
                border-style: solid;
                border-radius: 5px;
                border-width: 2px;
                background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(213, 218, 216, 255), stop:0.169312 rgba(82, 82, 83, 255), stop:0.328042 rgba(72, 70, 73, 255), stop:0.492063 rgba(78, 77, 79, 255), stop:0.703704 rgba(72, 70, 73, 255), stop:0.86 rgba(82, 82, 83, 255), stop:1 rgba(213, 218, 216, 255));
                font-family: "Bebas Kai";
                font-size: 14pt;
                min-height: 40px;
                max-height: 40px;
                min-width: 200px;
                max-width: 200px;
            }
            QPushButton:hover {
                background:  qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                                stop: 0 #A19E9E, stop: 1.0 #5C5959);
            }
            QPushButton:pressed {
                background:  qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));
            }
            QLabel {
                font-family: "Bebas Kai";
                font-size: 12pt;
                color: white;
                min-height: 25px;
                max-height: 25px;
            }
            QRadioButton {
                font-family: "Bebas Kai";
                font-size: 12pt;
                color: white;
                min-height: 25px;
                max-height: 25px;
            }
            QRadioButton::indicator {
                width: 15px;
                height: 15px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid white;
                border-radius: 8px;
                background-color: transparent;
            }
            QRadioButton::indicator:checked {
                border: 2px solid white;
                border-radius: 8px;
                background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(85, 85, 238, 255), stop:0.544974 rgba(90, 91, 239, 255), stop:1 rgba(126, 135, 243, 255));
            }
        """)
        
        # Store current values (data is always in machine units)
        self.current_values = current_values or {}
        
        # Setup UI
        self.setup_ui()
        
        # Pre-fill with current values
        self.load_current_values()

    def get_machine_units(self):
        """Get machine units from INI file"""
        try:
            linear_units = INIFILE.find("TRAJ", "LINEAR_UNITS")
            if linear_units and linear_units.strip().lower() in ['mm', 'metric']:
                return 'mm'
            else:
                return 'inch'
        except:
            return 'inch'  # Default to inch if unable to determine
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        
        # Unit Selection Group
        unit_group = QGroupBox("Display Units")
        unit_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        unit_layout = QHBoxLayout(unit_group)
        unit_layout.setSpacing(20)
        
        # Unit selection radio buttons
        self.unit_button_group = QButtonGroup()
        self.inch_radio = QRadioButton("Inch")
        self.mm_radio = QRadioButton("Millimeter")
        
        # Default to machine units
        if self.machine_units == 'mm':
            self.mm_radio.setChecked(True)
        else:
            self.inch_radio.setChecked(True)
        
        self.unit_button_group.addButton(self.inch_radio)
        self.unit_button_group.addButton(self.mm_radio)
        
        # Connect unit change signal
        self.inch_radio.toggled.connect(self.on_unit_changed)
        self.mm_radio.toggled.connect(self.on_unit_changed)
        
        # Add info labels
        info_label = QLabel(f"Machine units: {self.machine_units.upper()}")
        info_label.setStyleSheet("font-size: 10pt; color: #cccccc;")
        
        # Show thread source type for information
        if self.thread_source_type:
            source_info = f"Based on {self.thread_source_type} Thread"
            source_label = QLabel(source_info)
            source_label.setStyleSheet("font-size: 10pt; color: #cccccc;")
        else:
            source_label = QLabel("Manual Entry")
            source_label.setStyleSheet("font-size: 10pt; color: #cccccc;")
        
        unit_layout.addWidget(self.inch_radio)
        unit_layout.addWidget(self.mm_radio)
        unit_layout.addStretch()
        unit_layout.addWidget(info_label)
        unit_layout.addWidget(source_label)
        
        layout.addWidget(unit_group)
        
        # Thread Info Group
        info_group = QGroupBox("Thread Info")
        info_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        info_layout = QGridLayout(info_group)
        info_layout.setHorizontalSpacing(9)
        info_layout.setVerticalSpacing(15)
        
        # Thread name (required)
        info_layout.addWidget(QLabel("Thread Name"), 0, 0)
        self.name_edit = QLineEdit()
        self.name_edit.setPlaceholderText("My Custom 1/4-20")
        info_layout.addWidget(self.name_edit, 0, 1)
        
        # Thread type
        info_layout.addWidget(QLabel("Thread Type"), 1, 0)
        self.thread_type_edit = QLineEdit()
        self.thread_type_edit.setPlaceholderText("Custom")
        info_layout.addWidget(self.thread_type_edit, 1, 1)
        
        # Description
        info_layout.addWidget(QLabel("Description"), 2, 0)
        self.description_edit = QLineEdit()
        self.description_edit.setPlaceholderText("Optional description")
        info_layout.addWidget(self.description_edit, 2, 1)
        
        layout.addWidget(info_group)
        
        # Thread Parameters Group
        self.params_group = QGroupBox("Thread Parameters")
        self.params_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        params_layout = QGridLayout(self.params_group)
        params_layout.setHorizontalSpacing(9)
        params_layout.setVerticalSpacing(15)
        
        # Create labels that will be updated dynamically
        self.pitch_label = QLabel("Pitch")
        self.lead_length_label = QLabel("Lead Length")
        self.ext_major_label = QLabel("Ext Major Diameter")
        self.ext_minor_label = QLabel("Ext Minor Diameter")
        self.ext_pitch_label = QLabel("Ext Pitch Diameter")
        self.int_major_label = QLabel("Int Major Diameter")
        self.int_minor_label = QLabel("Int Minor Diameter")
        self.int_pitch_label = QLabel("Int Pitch Diameter")
        
        # Create input fields with high precision storage
        params_layout.addWidget(self.pitch_label, 0, 0)
        self.pitch_edit = VCPLineEdit(parent=self)
        self.pitch_edit.highPrecisionStorage = True
        params_layout.addWidget(self.pitch_edit, 0, 1)
        
        params_layout.addWidget(self.lead_length_label, 1, 0)
        self.lead_length_edit = VCPLineEdit(parent=self)
        self.lead_length_edit.highPrecisionStorage = True
        params_layout.addWidget(self.lead_length_edit, 1, 1)
        
        params_layout.addWidget(self.ext_major_label, 2, 0)
        self.ext_major_edit = VCPLineEdit(parent=self)
        self.ext_major_edit.highPrecisionStorage = True
        params_layout.addWidget(self.ext_major_edit, 2, 1)
        
        params_layout.addWidget(self.ext_minor_label, 3, 0)
        self.ext_minor_edit = VCPLineEdit(parent=self)
        self.ext_minor_edit.highPrecisionStorage = True
        params_layout.addWidget(self.ext_minor_edit, 3, 1)
        
        params_layout.addWidget(self.ext_pitch_label, 4, 0)
        self.ext_pitch_edit = VCPLineEdit(parent=self)
        self.ext_pitch_edit.highPrecisionStorage = True
        params_layout.addWidget(self.ext_pitch_edit, 4, 1)
        
        params_layout.addWidget(self.int_major_label, 5, 0)
        self.int_major_edit = VCPLineEdit(parent=self)
        self.int_major_edit.highPrecisionStorage = True
        params_layout.addWidget(self.int_major_edit, 5, 1)
        
        params_layout.addWidget(self.int_minor_label, 6, 0)
        self.int_minor_edit = VCPLineEdit(parent=self)
        self.int_minor_edit.highPrecisionStorage = True
        params_layout.addWidget(self.int_minor_edit, 6, 1)
        
        params_layout.addWidget(self.int_pitch_label, 7, 0)
        self.int_pitch_edit = VCPLineEdit(parent=self)
        self.int_pitch_edit.highPrecisionStorage = True
        params_layout.addWidget(self.int_pitch_edit, 7, 1)
        
        layout.addWidget(self.params_group)
        
        # Drill Sizes Group
        drill_group = QGroupBox("Drill Sizes")
        drill_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        drill_layout = QGridLayout(drill_group)
        drill_layout.setHorizontalSpacing(9)
        drill_layout.setVerticalSpacing(15)
        
        drill_layout.addWidget(QLabel("Tap Drill"), 0, 0)
        self.tap_drill_edit = QLineEdit()
        self.tap_drill_edit.setPlaceholderText("e.g., #7 or 5.5mm")
        drill_layout.addWidget(self.tap_drill_edit, 0, 1)
        
        drill_layout.addWidget(QLabel("Close Clearance"), 1, 0)
        self.clearance_close_edit = QLineEdit()
        self.clearance_close_edit.setPlaceholderText("e.g., 1/4 or 6.5mm")
        drill_layout.addWidget(self.clearance_close_edit, 1, 1)
        
        drill_layout.addWidget(QLabel("Free Clearance"), 2, 0)
        self.clearance_free_edit = QLineEdit()
        self.clearance_free_edit.setPlaceholderText("e.g., 17/64 or 7mm")
        drill_layout.addWidget(self.clearance_free_edit, 2, 1)
        
        layout.addWidget(drill_group)
        
        # Update labels and formatting
        self.update_unit_labels()
        self.update_display_decimals()
        
        # Buttons
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        
        self.save_button = QPushButton("Save Thread")
        self.cancel_button = QPushButton("Cancel")
        
        self.save_button.clicked.connect(self.save_thread)
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        
        layout.addLayout(button_layout)

    def on_unit_changed(self):
        """Handle unit selection change - convert all values to new units"""
        if self.updating_values:
            return  # Prevent recursive calls
        
        new_units = 'inch' if self.inch_radio.isChecked() else 'mm'
        old_units = self.current_display_units
        
        if new_units == old_units:
            return  # No change needed
        
        self.updating_values = True
        try:
            # Update labels and decimal places
            self.update_unit_labels()
            self.update_display_decimals()
            
            # Convert all numeric field values
            self.convert_field_values(old_units, new_units)
            
            # Update current display units
            self.current_display_units = new_units
            
        finally:
            self.updating_values = False

    def update_unit_labels(self):
        """Update labels based on selected units"""
        if self.inch_radio.isChecked():
            # Inch labels
            self.pitch_label.setText("Pitch (inch)")
            self.lead_length_label.setText("Lead Length (inch)")
            self.ext_major_label.setText("Ext Major Diameter (inch)")
            self.ext_minor_label.setText("Ext Minor Diameter (inch)")
            self.ext_pitch_label.setText("Ext Pitch Diameter (inch)")
            self.int_major_label.setText("Int Major Diameter (inch)")
            self.int_minor_label.setText("Int Minor Diameter (inch)")
            self.int_pitch_label.setText("Int Pitch Diameter (inch)")
            self.params_group.setTitle("Thread Parameters (inch)")
        else:
            # Metric labels
            self.pitch_label.setText("Pitch (mm)")
            self.lead_length_label.setText("Lead Length (mm)")
            self.ext_major_label.setText("Ext Major Diameter (mm)")
            self.ext_minor_label.setText("Ext Minor Diameter (mm)")
            self.ext_pitch_label.setText("Ext Pitch Diameter (mm)")
            self.int_major_label.setText("Int Major Diameter (mm)")
            self.int_minor_label.setText("Int Minor Diameter (mm)")
            self.int_pitch_label.setText("Int Pitch Diameter (mm)")
            self.params_group.setTitle("Thread Parameters (mm)")

    def update_display_decimals(self):
        """Update display decimal places based on selected units"""
        if self.inch_radio.isChecked():
            decimal_places = 4  # Inch precision
        else:
            decimal_places = 3  # Metric precision
        
        # Update all numeric fields
        numeric_fields = [
            self.pitch_edit, self.lead_length_edit,
            self.ext_major_edit, self.ext_minor_edit, self.ext_pitch_edit,
            self.int_major_edit, self.int_minor_edit, self.int_pitch_edit
        ]
        
        for field in numeric_fields:
            field.displayDecimals = decimal_places

    def convert_field_values(self, from_units, to_units):
        """Convert all field values from one unit to another"""
        if from_units == to_units:
            return
        
        # Conversion factor
        if from_units == 'inch' and to_units == 'mm':
            factor = 25.4
        elif from_units == 'mm' and to_units == 'inch':
            factor = 1.0 / 25.4
        else:
            return
        
        # Convert all numeric fields
        numeric_fields = [
            self.pitch_edit, self.lead_length_edit,
            self.ext_major_edit, self.ext_minor_edit, self.ext_pitch_edit,
            self.int_major_edit, self.int_minor_edit, self.int_pitch_edit
        ]
        
        for field in numeric_fields:
            try:
                current_value = field.value()  # Get high precision value
                if current_value != 0:
                    new_value = current_value * factor
                    field.setValue(new_value)  # Set high precision value
            except (ValueError, TypeError):
                pass  # Skip invalid values

    def load_current_values(self):
        """Pre-fill dialog with current UI values (convert from machine units to display units)"""
        if not self.current_values:
            return

        # Pre-fill text fields
        if 'suggested_name' in self.current_values:
            self.name_edit.setText(self.current_values['suggested_name'])
        
        if 'description' in self.current_values:
            self.description_edit.setText(self.current_values['description'])
        elif 'suggested_name' in self.current_values:
            desc_text = f"Custom variation of {self.current_values.get('original_name', 'thread')}"
            self.description_edit.setText(desc_text)

        thread_type = self.current_values.get('thread_type', 'Custom')
        self.thread_type_edit.setText(thread_type)
        
        # Convert values from machine units to display units
        display_units = 'inch' if self.inch_radio.isChecked() else 'mm'
        conversion_factor = 1.0
        
        if self.machine_units != display_units:
            if self.machine_units == 'inch' and display_units == 'mm':
                conversion_factor = 25.4
            elif self.machine_units == 'mm' and display_units == 'inch':
                conversion_factor = 1.0 / 25.4
        
        # Fill numeric fields (convert from machine units to display units)
        if 'pitch' in self.current_values:
            value = self.current_values['pitch'] * conversion_factor
            self.pitch_edit.setValue(value)
        
        if 'lead_length' in self.current_values:
            value = self.current_values['lead_length'] * conversion_factor
            self.lead_length_edit.setValue(value)
        
        # External diameters
        external_data = self.current_values.get('external', {})
        if 'major_diameter' in external_data:
            value = external_data['major_diameter'] * conversion_factor
            self.ext_major_edit.setValue(value)
        if 'minor_diameter' in external_data:
            value = external_data['minor_diameter'] * conversion_factor
            self.ext_minor_edit.setValue(value)
        if 'pitch_diameter' in external_data:
            value = external_data['pitch_diameter'] * conversion_factor
            self.ext_pitch_edit.setValue(value)
        
        # Internal diameters
        internal_data = self.current_values.get('internal', {})
        if 'major_diameter' in internal_data:
            value = internal_data['major_diameter'] * conversion_factor
            self.int_major_edit.setValue(value)
        if 'minor_diameter' in internal_data:
            value = internal_data['minor_diameter'] * conversion_factor
            self.int_minor_edit.setValue(value)
        if 'pitch_diameter' in internal_data:
            value = internal_data['pitch_diameter'] * conversion_factor
            self.int_pitch_edit.setValue(value)
        
        # Handle drill sizes
        drill_data = self.current_values.get('drill_sizes', {})
        if drill_data.get('tap_drill'):
            self.tap_drill_edit.setText(drill_data['tap_drill'])
        if drill_data.get('clearance_close'):
            self.clearance_close_edit.setText(drill_data['clearance_close'])
        if drill_data.get('clearance_free'):
            self.clearance_free_edit.setText(drill_data['clearance_free'])
        
        # Set current display units
        self.current_display_units = display_units
    
    def save_thread(self):
        """Validate and save the custom thread"""
        
        # Validate required fields
        name = self.name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, "Validation Error", "Thread name is required!")
            return
        
        try:
            # Get high precision values from fields
            pitch = self.pitch_edit.value()
            lead_length = self.lead_length_edit.value()
            
            ext_major = self.ext_major_edit.value()
            ext_minor = self.ext_minor_edit.value()
            ext_pitch = self.ext_pitch_edit.value()
            
            int_major = self.int_major_edit.value()
            int_minor = self.int_minor_edit.value()
            int_pitch = self.int_pitch_edit.value()
            
            # Convert values back to machine units for storage
            display_units = 'inch' if self.inch_radio.isChecked() else 'mm'
            conversion_factor = 1.0
            
            if self.machine_units != display_units:
                if display_units == 'inch' and self.machine_units == 'mm':
                    conversion_factor = 25.4
                elif display_units == 'mm' and self.machine_units == 'inch':
                    conversion_factor = 1.0 / 25.4
            
            # Create thread data structure (stored in machine units)
            thread_data = {
                "pitch": pitch * conversion_factor,
                "lead_length": lead_length * conversion_factor,
                "thread_type": self.thread_type_edit.text() or "Custom",
                "description": self.description_edit.text() or f"{name} Custom Thread",
                "npt_taper": False,
                "external": {
                    "major_diameter": ext_major * conversion_factor,
                    "minor_diameter": ext_minor * conversion_factor,
                    "pitch_diameter": ext_pitch * conversion_factor,
                },
                "internal": {
                    "major_diameter": int_major * conversion_factor,
                    "minor_diameter": int_minor * conversion_factor,
                    "pitch_diameter": int_pitch * conversion_factor,
                },
                "drill_sizes": {
                    "tap_drill": self.tap_drill_edit.text(),
                    "clearance_close": self.clearance_close_edit.text(),
                    "clearance_free": self.clearance_free_edit.text()
                },
                "created_date": datetime.now().isoformat(),
                "machine_units": self.machine_units,
                "source_type": self.thread_source_type
            }
            
            # Store for retrieval
            self.thread_name = name
            self.thread_data = thread_data
            
            # Accept the dialog
            self.accept()
            
        except ValueError as e:
            QMessageBox.warning(self, "Validation Error", 
                              f"Please enter valid numeric values for diameters and measurements.\nError: {str(e)}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while saving: {str(e)}")