#!/usr/bin/env python

from qtpy.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, 
                           QLabel, QLineEdit, QPushButton, QMessageBox, QGroupBox, 
                           QSizePolicy, QRadioButton, QButtonGroup, QFrame)
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
        self.setMinimumSize(450, 700)  # Increased height for additional fields
        
        # Get parent's machine units if available, otherwise determine from INI
        if hasattr(parent, 'machine_units'):
            self.machine_units = parent.machine_units
        else:
            self.machine_units = self.get_machine_units()
        
        # Store thread source type (SAE, Metric, Custom, or None)
        # This is informational only - data is always in machine units
        self.thread_source_type = thread_source_type
        
        # Track what units the fields currently contain
        # Initially, fields will contain values in machine units
        self.current_field_units = self.machine_units
        
        # Flag to prevent recursive unit conversions
        self.updating_units = False
        
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
        
        # Store current values
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
    
    def get_preferred_display_units(self):
        """Determine preferred display units based on machine units (data is always in machine units)"""
        # Since data is always passed in machine units, default to machine units
        # User can toggle to other units if desired for easier editing
        return self.machine_units
    
    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        layout.setSizeConstraint(QVBoxLayout.SetMinimumSize)
        
        # Unit Selection Group (allow user to choose units for display/entry)
        unit_group = QGroupBox("Entry Units")
        unit_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        unit_layout = QHBoxLayout(unit_group)
        unit_layout.setSpacing(20)
        
        # Unit selection radio buttons
        self.unit_button_group = QButtonGroup()
        self.inch_radio = QRadioButton("Inch")
        self.mm_radio = QRadioButton("Millimeter")
        
        # Always default to machine units since data is passed in machine units
        if self.machine_units == 'mm':
            self.mm_radio.setChecked(True)
            print(f"DEBUG: Setting initial display units to MM (machine units)")
        else:
            self.inch_radio.setChecked(True)
            print(f"DEBUG: Setting initial display units to INCH (machine units)")
        
        self.unit_button_group.addButton(self.inch_radio)
        self.unit_button_group.addButton(self.mm_radio)
        
        # Connect unit change signal
        self.inch_radio.toggled.connect(self.on_unit_changed)
        self.mm_radio.toggled.connect(self.on_unit_changed)
        
        # Add info labels
        info_label = QLabel(f"Machine units: {self.machine_units.upper()}")
        info_label.setStyleSheet("font-size: 10pt; color: #cccccc;")
        
        # Show thread source type for information
        source_info = ""
        if self.thread_source_type == 'SAE':
            source_info = "SAE Thread"
        elif self.thread_source_type == 'Metric':
            source_info = "Metric Thread"  
        elif self.thread_source_type == 'Custom':
            source_info = "Custom Thread"
        else:
            source_info = "Manual Entry"
            
        source_label = QLabel(f"Source: {source_info}")
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
        params_group = QGroupBox("Thread Parameters")
        params_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        params_layout = QGridLayout(params_group)
        params_layout.setHorizontalSpacing(9)
        params_layout.setVerticalSpacing(15)
        
        # Create labels that will be updated dynamically
        self.pitch_label = QLabel("Pitch")
        self.ext_major_label = QLabel("Ext Major Diameter")
        self.ext_minor_label = QLabel("Ext Minor Diameter") 
        self.ext_pitch_label = QLabel("Ext Pitch Diameter")
        self.int_major_label = QLabel("Int Major Diameter")
        self.int_minor_label = QLabel("Int Minor Diameter")
        self.int_pitch_label = QLabel("Int Pitch Diameter")
        self.lead_length_label = QLabel("Lead Length")
        
        # Add labels and inputs
        params_layout.addWidget(self.pitch_label, 0, 0)
        self.pitch_edit = VCPLineEdit()
        params_layout.addWidget(self.pitch_edit, 0, 1)
        
        params_layout.addWidget(self.ext_major_label, 1, 0)
        self.ext_major_edit = VCPLineEdit()
        params_layout.addWidget(self.ext_major_edit, 1, 1)
        
        params_layout.addWidget(self.ext_minor_label, 2, 0)
        self.ext_minor_edit = VCPLineEdit()
        params_layout.addWidget(self.ext_minor_edit, 2, 1)
        
        params_layout.addWidget(self.ext_pitch_label, 3, 0)
        self.ext_pitch_edit = VCPLineEdit()
        params_layout.addWidget(self.ext_pitch_edit, 3, 1)
        
        params_layout.addWidget(self.int_major_label, 4, 0)
        self.int_major_edit = VCPLineEdit()
        params_layout.addWidget(self.int_major_edit, 4, 1)
        
        params_layout.addWidget(self.int_minor_label, 5, 0)
        self.int_minor_edit = VCPLineEdit()
        params_layout.addWidget(self.int_minor_edit, 5, 1)
        
        params_layout.addWidget(self.int_pitch_label, 6, 0)
        self.int_pitch_edit = VCPLineEdit()
        params_layout.addWidget(self.int_pitch_edit, 6, 1)
        
        params_layout.addWidget(self.lead_length_label, 7, 0)
        self.lead_length_edit = VCPLineEdit()
        params_layout.addWidget(self.lead_length_edit, 7, 1)
        
        layout.addWidget(params_group)
        
        # Drill Sizes Group
        drill_group = QGroupBox("Drill Sizes")
        drill_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        drill_layout = QGridLayout(drill_group)
        drill_layout.setHorizontalSpacing(9)
        drill_layout.setVerticalSpacing(15)
        
        # Drill size labels and inputs
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
        self.update_formatting()
        
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
        if self.updating_units:
            return  # Prevent recursive calls
            
        self.updating_units = True
        try:
            print(f"DEBUG: Unit changed, converting values...")
            
            # Get current values before conversion
            current_values = self.get_current_field_values()
            print(f"DEBUG: Current field values before conversion: {current_values}")
            
            # Update labels and formatting
            self.update_unit_labels()
            self.update_formatting()
            
            # Convert and populate with new unit values
            self.populate_fields_with_conversion(current_values)
            
            # Update the tracked field units to the new selection
            self.current_field_units = self.get_selected_units()
            
        finally:
            self.updating_units = False
    
    def get_current_field_values(self):
        """Get current values from all fields in the currently stored units"""
        try:
            return {
                'pitch': float(self.pitch_edit.text() or "0"),
                'lead_length': float(self.lead_length_edit.text() or "0"),
                'external': {
                    'major_diameter': float(self.ext_major_edit.text() or "0"),
                    'minor_diameter': float(self.ext_minor_edit.text() or "0"),
                    'pitch_diameter': float(self.ext_pitch_edit.text() or "0"),
                },
                'internal': {
                    'major_diameter': float(self.int_major_edit.text() or "0"),
                    'minor_diameter': float(self.int_minor_edit.text() or "0"),
                    'pitch_diameter': float(self.int_pitch_edit.text() or "0"),
                },
                'units': self.current_field_units  # Use tracked field units, not radio button state
            }
        except ValueError:
            # If conversion fails, return zeros
            return {
                'pitch': 0,
                'lead_length': 0,
                'external': {'major_diameter': 0, 'minor_diameter': 0, 'pitch_diameter': 0},
                'internal': {'major_diameter': 0, 'minor_diameter': 0, 'pitch_diameter': 0},
                'units': self.current_field_units
            }
    
    def populate_fields_with_conversion(self, values):
        """Populate fields with values, converting as needed"""
        from_units = values.get('units', 'inch')
        to_units = self.get_selected_units()
        
        if from_units == to_units:
            return  # No conversion needed
        
        print(f"DEBUG: Converting values from {from_units} to {to_units}")
        
        # Convert and set basic parameters
        if values['pitch'] != 0:
            converted_pitch = self.convert_value(values['pitch'], from_units, to_units)
            pitch_text = f"{converted_pitch:.4f}" if to_units == 'inch' else f"{converted_pitch:.3f}"
            self.pitch_edit.setText(pitch_text)
            print(f"DEBUG: Converted pitch: {values['pitch']} {from_units} -> {pitch_text} {to_units}")
        
        if values['lead_length'] != 0:
            converted_lead = self.convert_value(values['lead_length'], from_units, to_units)
            lead_text = f"{converted_lead:.4f}" if to_units == 'inch' else f"{converted_lead:.3f}"
            self.lead_length_edit.setText(lead_text)
            print(f"DEBUG: Converted lead length: {values['lead_length']} {from_units} -> {lead_text} {to_units}")
        
        # Convert external diameters
        ext_data = values.get('external', {})
        for diameter_type, edit_field in [
            ('major_diameter', self.ext_major_edit),
            ('minor_diameter', self.ext_minor_edit),
            ('pitch_diameter', self.ext_pitch_edit)
        ]:
            value = ext_data.get(diameter_type, 0)
            if value != 0:
                converted_value = self.convert_value(value, from_units, to_units)
                value_text = f"{converted_value:.4f}" if to_units == 'inch' else f"{converted_value:.3f}"
                edit_field.setText(value_text)
                print(f"DEBUG: Converted ext {diameter_type}: {value} {from_units} -> {value_text} {to_units}")
        
        # Convert internal diameters
        int_data = values.get('internal', {})
        for diameter_type, edit_field in [
            ('major_diameter', self.int_major_edit),
            ('minor_diameter', self.int_minor_edit),
            ('pitch_diameter', self.int_pitch_edit)
        ]:
            value = int_data.get(diameter_type, 0)
            if value != 0:
                converted_value = self.convert_value(value, from_units, to_units)
                value_text = f"{converted_value:.4f}" if to_units == 'inch' else f"{converted_value:.3f}"
                edit_field.setText(value_text)
                print(f"DEBUG: Converted int {diameter_type}: {value} {from_units} -> {value_text} {to_units}")
    
    def get_selected_units(self):
        """Get the currently selected units"""
        return 'inch' if self.inch_radio.isChecked() else 'mm'
    
    def convert_value(self, value, from_unit, to_unit):
        """Convert value between units"""
        if from_unit == to_unit:
            return value
        
        if from_unit == 'inch' and to_unit == 'mm':
            return value * 25.4
        elif from_unit == 'mm' and to_unit == 'inch':
            return value / 25.4
        else:
            return value
    
    def load_current_values(self):
        """Pre-fill dialog with current UI values"""
        print(f"DEBUG: load_current_values called with: {self.current_values}")
        
        if not self.current_values:
            print("DEBUG: No current values provided")
            return

        # Pre-fill suggested name if available
        if 'suggested_name' in self.current_values:
            print(f"DEBUG: Setting suggested name: {self.current_values['suggested_name']}")
            self.name_edit.setText(self.current_values['suggested_name'])
        else:
            print("DEBUG: No suggested_name found")
        
        # Pre-fill description
        if 'description' in self.current_values:
            print(f"DEBUG: Setting description: {self.current_values['description']}")
            self.description_edit.setText(self.current_values['description'])
        elif 'suggested_name' in self.current_values:
            desc_text = f"Custom variation of {self.current_values.get('original_name', 'thread')}"
            print(f"DEBUG: Setting generated description: {desc_text}")
            self.description_edit.setText(desc_text)

        # Get selected units for formatting
        selected_units = self.get_selected_units()
        
        # Basic parameters - values are expected to be in machine units
        # Convert to display units if needed
        pitch = self.current_values.get('pitch')
        if pitch is not None:
            display_pitch = self.convert_value(pitch, self.machine_units, selected_units)
            pitch_text = f"{display_pitch:.4f}" if selected_units == 'inch' else f"{display_pitch:.3f}"
            print(f"DEBUG: Setting pitch: {pitch_text} (converted from {pitch} {self.machine_units} to {selected_units})")
            self.pitch_edit.setText(pitch_text)
        
        lead_length = self.current_values.get('lead_length')
        if lead_length is not None:
            display_lead = self.convert_value(lead_length, self.machine_units, selected_units)
            lead_text = f"{display_lead:.4f}" if selected_units == 'inch' else f"{display_lead:.3f}"
            print(f"DEBUG: Setting lead_length: {lead_text} (converted from {lead_length} {self.machine_units} to {selected_units})")
            self.lead_length_edit.setText(lead_text)
        
        thread_type = self.current_values.get('thread_type', 'Custom')
        print(f"DEBUG: Setting thread_type: {thread_type}")
        self.thread_type_edit.setText(thread_type)
        
        # External diameters - convert and format based on selected units
        ext_data = self.current_values.get('external', {})
        ext_major = ext_data.get('major_diameter')
        if ext_major is not None:
            display_major = self.convert_value(ext_major, self.machine_units, selected_units)
            major_text = f"{display_major:.4f}" if selected_units == 'inch' else f"{display_major:.3f}"
            print(f"DEBUG: Setting external major: {major_text} (converted from {ext_major} {self.machine_units} to {selected_units})")
            self.ext_major_edit.setText(major_text)
            
        ext_minor = ext_data.get('minor_diameter')
        if ext_minor is not None:
            display_minor = self.convert_value(ext_minor, self.machine_units, selected_units)
            minor_text = f"{display_minor:.4f}" if selected_units == 'inch' else f"{display_minor:.3f}"
            print(f"DEBUG: Setting external minor: {minor_text} (converted from {ext_minor} {self.machine_units} to {selected_units})")
            self.ext_minor_edit.setText(minor_text)
        
        ext_pitch = ext_data.get('pitch_diameter')
        if ext_pitch is not None:
            display_pitch = self.convert_value(ext_pitch, self.machine_units, selected_units)
            pitch_text = f"{display_pitch:.4f}" if selected_units == 'inch' else f"{display_pitch:.3f}"
            print(f"DEBUG: Setting external pitch: {pitch_text} (converted from {ext_pitch} {self.machine_units} to {selected_units})")
            self.ext_pitch_edit.setText(pitch_text)
        
        # Internal diameters - convert and format based on selected units
        int_data = self.current_values.get('internal', {})
        int_major = int_data.get('major_diameter')
        if int_major is not None:
            display_major = self.convert_value(int_major, self.machine_units, selected_units)
            major_text = f"{display_major:.4f}" if selected_units == 'inch' else f"{display_major:.3f}"
            print(f"DEBUG: Setting internal major: {major_text} (converted from {int_major} {self.machine_units} to {selected_units})")
            self.int_major_edit.setText(major_text)
            
        int_minor = int_data.get('minor_diameter')
        if int_minor is not None:
            display_minor = self.convert_value(int_minor, self.machine_units, selected_units)
            minor_text = f"{display_minor:.4f}" if selected_units == 'inch' else f"{display_minor:.3f}"
            print(f"DEBUG: Setting internal minor: {minor_text} (converted from {int_minor} {self.machine_units} to {selected_units})")
            self.int_minor_edit.setText(minor_text)
        
        int_pitch = int_data.get('pitch_diameter')
        if int_pitch is not None:
            display_pitch = self.convert_value(int_pitch, self.machine_units, selected_units)
            pitch_text = f"{display_pitch:.4f}" if selected_units == 'inch' else f"{display_pitch:.3f}"
            print(f"DEBUG: Setting internal pitch: {pitch_text} (converted from {int_pitch} {self.machine_units} to {selected_units})")
            self.int_pitch_edit.setText(pitch_text)
        
        # Drill sizes (if available) - these are usually text with descriptions
        drill_data = self.current_values.get('drill_sizes', {})
        tap_drill = drill_data.get('tap_drill', '')
        clearance_close = drill_data.get('clearance_close', '')
        clearance_free = drill_data.get('clearance_free', '')
        print(f"DEBUG: Setting drill sizes - tap: {tap_drill}, close: {clearance_close}, free: {clearance_free}")
        if tap_drill:
            self.tap_drill_edit.setText(tap_drill)
        if clearance_close:
            self.clearance_close_edit.setText(clearance_close)
        if clearance_free:
            self.clearance_free_edit.setText(clearance_free)
    
    def save_thread(self):
        """Validate and save the custom thread"""
        
        # Validate required fields
        name = self.name_edit.text().strip()
        if not name:
            QMessageBox.warning(self, "Validation Error", "Thread name is required!")
            return
        
        try:
            # Get selected units
            selected_units = self.get_selected_units()
            
            # Helper function to get and convert values to machine units
            def get_converted_value(field, default=0.0):
                text = field.text().strip()
                if not text:
                    return default
                value = float(text)
                return self.convert_value(value, selected_units, self.machine_units)
            
            # Create thread data structure - all values stored in machine units
            thread_data = {
                "pitch": get_converted_value(self.pitch_edit),
                "lead_length": get_converted_value(self.lead_length_edit),
                "thread_type": self.thread_type_edit.text() or "Custom",
                "description": self.description_edit.text() or f"{name} Custom Thread",
                "npt_taper": False,
                "external": {
                    "major_diameter": get_converted_value(self.ext_major_edit),
                    "minor_diameter": get_converted_value(self.ext_minor_edit),
                    "pitch_diameter": get_converted_value(self.ext_pitch_edit),
                },
                "internal": {
                    "major_diameter": get_converted_value(self.int_major_edit),
                    "minor_diameter": get_converted_value(self.int_minor_edit),
                    "pitch_diameter": get_converted_value(self.int_pitch_edit),
                },
                "drill_sizes": {
                    "tap_drill": self.tap_drill_edit.text(),
                    "clearance_close": self.clearance_close_edit.text(),
                    "clearance_free": self.clearance_free_edit.text()
                },
                "created_date": datetime.now().isoformat(),
                "units_created": selected_units,  # Record the units used for creation
                "machine_units": self.machine_units  # Record machine units for reference
            }
            
            print(f"DEBUG: Saving thread data in {self.machine_units} units: {thread_data}")
            
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
    
    def get_thread_data(self):
        """Get thread data from dialog fields, converting to machine units for storage"""
        try:
            selected_units = self.get_selected_units()
            
            # Get raw values from dialog
            pitch = float(self.pitch_edit.text() or "0")
            ext_major = float(self.ext_major_edit.text() or "0")
            ext_minor = float(self.ext_minor_edit.text() or "0")
            ext_pitch = float(self.ext_pitch_edit.text() or "0")
            int_major = float(self.int_major_edit.text() or "0")
            int_minor = float(self.int_minor_edit.text() or "0")
            int_pitch = float(self.int_pitch_edit.text() or "0")
            lead_length = float(self.lead_length_edit.text() or "0")
            
            # Convert to machine units if needed
            if selected_units != self.machine_units:
                pitch = self.convert_value(pitch, selected_units, self.machine_units)
                ext_major = self.convert_value(ext_major, selected_units, self.machine_units)
                ext_minor = self.convert_value(ext_minor, selected_units, self.machine_units)
                ext_pitch = self.convert_value(ext_pitch, selected_units, self.machine_units)
                int_major = self.convert_value(int_major, selected_units, self.machine_units)
                int_minor = self.convert_value(int_minor, selected_units, self.machine_units)
                int_pitch = self.convert_value(int_pitch, selected_units, self.machine_units)
                lead_length = self.convert_value(lead_length, selected_units, self.machine_units)
            
            # Apply proper decimal formatting for machine units
            if self.machine_units == 'inch':
                decimal_places = 4
            else:
                decimal_places = 3
            
            thread_data = {
                "pitch": round(pitch, decimal_places),
                "external": {
                    "major_diameter": round(ext_major, decimal_places),
                    "minor_diameter": round(ext_minor, decimal_places),
                    "pitch_diameter": round(ext_pitch, decimal_places)
                },
                "internal": {
                    "major_diameter": round(int_major, decimal_places),
                    "minor_diameter": round(int_minor, decimal_places),
                    "pitch_diameter": round(int_pitch, decimal_places)
                },
                "lead_length": round(lead_length, decimal_places),
                "description": self.description_edit.text() or f"Custom {self.name_edit.text()}",
                "thread_type": self.thread_type_edit.text() or "CUSTOM",
                "npt_taper": False,
                "units": self.machine_units,  # Always store in machine units
                "created_date": datetime.now().isoformat(),
                "drill_sizes": {
                    "tap_drill": self.tap_drill_edit.text() or "CUSTOM",
                    "clearance_close": self.clearance_close_edit.text() or "CUSTOM", 
                    "clearance_free": self.clearance_free_edit.text() or "CUSTOM"
                }
            }
            
            return thread_data
            
        except ValueError as e:
            print(f"Error converting thread values: {e}")
            return None
        except Exception as e:
            print(f"Error getting thread data: {e}")
            return None
    
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
    
    def update_formatting(self):
        """Update field formatting based on selected units"""
        if self.inch_radio.isChecked():
            # Inch formatting - 4 decimal places
            format_str = "{:.4f}"
            placeholder = "0.0000"
        else:
            # Metric formatting - 3 decimal places
            format_str = "{:.3f}"
            placeholder = "0.000"
        
        # Update placeholders
        numeric_fields = [
            self.pitch_edit, self.lead_length_edit,
            self.ext_major_edit, self.ext_minor_edit, self.ext_pitch_edit,
            self.int_major_edit, self.int_minor_edit, self.int_pitch_edit
        ]
        
        for field in numeric_fields:
            field.setPlaceholderText(placeholder)