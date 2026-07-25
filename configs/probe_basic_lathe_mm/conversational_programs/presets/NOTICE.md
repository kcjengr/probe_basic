# Third-party data attribution

The baseline cutting-speed values (`rough_surface_speed`/`finish_surface_speed`
and the surface-speed-derived fields) in the material preset JSON files in
this directory are derived from FreeCAD's Path Workbench "FeedsAndSpeeds"
material cards:

- Source: https://github.com/dubstar-04/FeedsAndSpeeds (`Materials/*.FCMat`)
- Author: (c) 2022 Daniel Wood
- License: Creative Commons Attribution 3.0 (CC-BY 3.0) —
  https://creativecommons.org/licenses/by/3.0/

Values were converted (m/min to SFM) and scaled per
`generate_material_presets.py` in this directory; feedrate/step-depth/RPM
values are not from this source (see that script's docstring for the
tiering approach used instead).

This notice satisfies CC-BY 3.0's attribution requirement; it does not
place any additional license obligation on pb_lathe_conv itself.
