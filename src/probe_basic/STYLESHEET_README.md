# Probe Basic Stylesheet Management

## Single Source of Truth: probe_basic.qss

The **probe_basic.qss** file is the ONLY stylesheet source. The .ui file has an empty stylesheet property.

---

## What Changed from PyQt5 to PySide6/Qt6

### Problem 1: File Loading Bug
In the Qt6 migration, the `loadStylesheet()` method used this incorrect syntax:
```python
self.setStyleSheet("file:///" + stylesheet)  # ❌ Doesn't work in Qt Designer
```

**Qt Designer cannot resolve `file:///` references** - it only renders stylesheets that are:
1. Embedded directly in the .ui file, or  
2. Loaded with actual CSS content (not file paths)

**Solution**: Fixed qtpyvcp to **read and load the actual file contents**:
```python
with open(stylesheet, 'r') as f:
    qss_content = f.read()
self.setStyleSheet(qss_content)  # ✅ Works everywhere
```

### Problem 2: Designer Saves Stylesheet to .ui File
Qt5 vs Qt6 API change broke Designer preview:

**Qt5**: Used `formContainer()` - a preview wrapper that doesn't modify widget properties
```python
widget = form_window_interface.formContainer()  # ✅ Preview only
widget.setStyleSheet(style)  # Doesn't save to .ui file
```

**Qt6 (broken)**: Used `mainContainer()` - the actual widget that gets saved
```python  
widget = form_window_interface.mainContainer()  # ❌ The real widget
widget.setStyleSheet(style)  # Saves stylesheet to .ui file when Designer saves!
```

**Solution**: Changed back to `formContainer()` for Designer preview:
```python
# Apply to preview wrapper, not the real widget
form_container = form_window_interface.formContainer()
form_container.setStyleSheet(style)  # ✅ Preview only, not saved to .ui
```

Now the external .qss file works in **both** Qt Designer and at runtime, and Designer
**won't save the stylesheet** back into the .ui file!

---

## Developer Workflow

### Edit Styles in Text Editor
```bash
nano probe_basic.qss
cd ../../configs/probe_basic
linuxcnc probe_basic.ini
```

### Edit with Qt Designer Preview
```bash
./launch_designer.sh  # Launches Designer with stylesheet loaded
# Edit probe_basic.qss in your text editor while Designer is open
# Close and reopen Designer to see stylesheet changes
```

---

## How It Works

- **probe_basic.qss** - Single source of truth for all styles
- **probe_basic.ui** - UI layout only, empty `<property name="styleSheet">` 
- **launch_designer.sh** - Sets `QSS_STYLESHEET` environment variable
- **qtpyvcp** - Reads .qss file contents and applies with `setStyleSheet()`
- **Runtime & Designer** - Both load the same external .qss file

---

## Benefits

✅ **Single source of truth** - Only probe_basic.qss exists  
✅ **No embedded stylesheet** - .ui file stays clean  
✅ **Designer preview works** - See styles while editing layout  
✅ **No sync needed** - Both Designer and runtime use same file  
✅ **Version control friendly** - One .qss file to track  
✅ **No conflicts** - No duplicate stylesheet definitions  

---

## Files

- `probe_basic.qss` - The stylesheet (single source)
- `probe_basic.ui` - The UI layout (no embedded stylesheet)  
- `launch_designer.sh` - Launch Designer with stylesheet preview
- `probe_basic.yml` - Config that specifies the .qss file path
