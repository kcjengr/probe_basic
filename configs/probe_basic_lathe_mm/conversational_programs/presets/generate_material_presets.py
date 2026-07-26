#!/usr/bin/env python3
"""Generate the full 15-material preset JSON set from FreeCAD's Path
FeedsAndSpeeds material cards (CC-BY 3.0, (c) 2022 Daniel Wood -- see
NOTICE.md in this directory) plus the 3 already-tuned tier-anchor presets
(aluminum/steel/stainless) already in this directory.

This is a starting-point heuristic, not a rigorous physics derivation:

- rough/finish surface speed is derived from FreeCAD's SurfaceSpeed_Carbide
  (m/min), converted to SFM and scaled down so it reads as a comfortable
  starting point rather than a maximum (calibrated against the existing,
  already-accepted aluminum preset).
- Feedrate/step-depth/RPM-limit have no such external reference, so each
  material is sorted into one of 3 machinability tiers by FreeCAD's Kp
  (a relative specific-cutting-force indicator) and simply inherits that
  tier's already-tuned values from the aluminum/steel/stainless anchor
  presets wholesale.

Each operation is emitted twice: `params` in inch and `params_mm` in
metric, so a metric machine never has to read inch numbers out of a preset
(the scale button in pb_lathe_conv picks the slot matching the machine's
lathe-conv.machine-units setting). Surface speeds in the metric slot come
straight off the same FreeCAD m/min source rather than being converted back
out of SFM; the length-derived values have no metric source, so those are
converted from the inch anchors.

Run from this directory: python3 generate_material_presets.py
"""
import json
import os
import re
import sys

SFM_PER_M_MIN = 3.28084
MM_PER_INCH = 25.4
SURFACE_SPEED_SCALE = 0.65
ROUGH_TO_FINISH_RATIO = 0.85

HERE = os.path.dirname(os.path.abspath(__file__))
LATHE_CONV_PY = os.path.join(
    HERE, '..', '..', '..', '..', '..', 'pb_lathe_conv',
    'src', 'lathe_conversational', 'lathe_conv.py')
LATHE_CONV_PY = os.path.normpath(LATHE_CONV_PY)

# (display_label, output_filename, SurfaceSpeed_Carbide m/min, Kp)
# -- source: github.com/dubstar-04/FeedsAndSpeeds Materials/*.FCMat, CC-BY 3.0
MATERIALS = [
    ('Aluminium (6061)', 'aluminum_6061_preset.json', 395, 0.9),
    ('Aluminium (7075)', 'aluminum_7075_preset.json', 395, 0.9),
    ('Aluminium (Cast)', 'aluminum_cast_preset.json', 395, 0.68),
    ('Brass (Soft)', 'brass_soft_preset.json', 300, 0.68),
    ('Brass (Medium)', 'brass_medium_preset.json', 350, 1.36),
    ('Brass (Hard)', 'brass_hard_preset.json', 395, 2.27),
    ('Carbon Steel', 'carbon_steel_preset.json', 120, 1.88),
    ('Tool Steel', 'tool_steel_preset.json', 45, 1.88),
    ('Stainless (303)', 'stainless_303_preset.json', 85, 2.07),
    ('Stainless (304)', 'stainless_304_preset.json', 37.5, 2.07),
    ('Stainless (316)', 'stainless_316_preset.json', 25, 2.07),
    ('Hardwood', 'hardwood_preset.json', 275, 0.75),
    ('Softwood', 'softwood_preset.json', 255, 0.5),
    ('Hard Plastics', 'hard_plastics_preset.json', 275, 0.75),
    ('Soft Plastics', 'soft_plastics_preset.json', 255, 0.5),
]

TIER_ANCHORS = {
    'soft': 'aluminum_preset.json',
    'medium': 'steel_preset.json',
    'hard': 'stainless_preset.json',
}

# Keys that get a material-specific surface-speed override (same physical
# concept wherever they appear: rough/finish cutting speed for a pass).
ROUGH_SFM_KEYS = {'rough_surface_speed', 'rough_ssp_axial', 'rough_ssp_radial'}
FINISH_SFM_KEYS = {'finish_surface_speed', 'finish_ssp_axial', 'finish_ssp_radial'}
# Parting has one single-pass speed, not a rough/finish split -- parting is
# a heavier, full-width cut closer in character to a roughing pass, and the
# existing aluminum anchor's own data confirms this (parting surface_speed
# 800 matches facing's rough_surface_speed 800, not its finish 850).
SINGLE_SFM_ROUGH_LIKE_KEYS = {'surface_speed'}

# Keys that get the tier's RPM ceiling uniformly (max_rpm_limit and
# constant_rpm are set equal -- every anchor preset already runs CSS mode,
# where constant_rpm is an unused fallback, not the operative value).
RPM_CEILING_KEYS = {
    'max_rpm_limit', 'constant_rpm', 'max_rpm_axial', 'max_rpm_radial',
    'rpm_axial', 'rpm_radial',
}

TIER_RPM_LIMIT = {'soft': 1500, 'medium': 2200, 'hard': 1800}

# Length-derived keys -- feed per rev/min, depth of cut, clearance. These
# only exist in the inch anchors, so the metric slot converts them. Every
# other numeric key is unit-neutral (RPM, tip angle, dwell seconds, pass
# counts) or a surface speed, which is sourced natively in m/min instead.
LENGTH_KEYS = {
    'rough_feedrate', 'finish_feedrate',
    'rough_step_depth', 'finish_step_depth',
    'rough_feed_axial', 'rough_feed_radial',
    'finish_feed_axial', 'finish_feed_radial',
    'rough_step_axial', 'rough_step_radial',
    'finish_step_axial', 'finish_step_radial',
    'feedrate', 'retract_feed',
    'z_stock_face', 'z_clearance', 'x_clearance',
}


def tier_for_kp(kp):
    if kp < 1.0:
        return 'soft'
    if kp < 2.0:
        return 'medium'
    return 'hard'


def load_whitelist_fn():
    """Import _material_preset_param_keys from lathe_conv.py in isolation,
    bypassing lathe_conversational/__init__.py (segfaults outside a full
    qtpyvcp app context -- see this session's established workaround)."""
    src = open(LATHE_CONV_PY, encoding='utf-8').read()
    m = re.search(
        r'    def _material_preset_param_keys\(self, operation_name\):.*?'
        r'\n    def _apply_profile_points_to_table_widget',
        src, re.DOTALL)
    if not m:
        raise RuntimeError('Could not locate _material_preset_param_keys in lathe_conv.py')
    method_src = m.group(0).rsplit('\n    def _apply_profile_points_to_table_widget', 1)[0]
    method_src = method_src.replace(
        'def _material_preset_param_keys(self, operation_name):',
        'def _material_preset_param_keys(operation_name):', 1)
    lines = method_src.split('\n')
    method_src = '\n'.join(l[4:] if l.startswith('    ') else l for l in lines)
    ns = {}
    exec(method_src, ns)
    return ns['_material_preset_param_keys']


def compute_surface_speeds(m_per_min):
    """Return ((rough_sfm, finish_sfm), (rough_smm, finish_smm)).

    Both pairs derive from the same FreeCAD m/min figure -- the metric one
    just skips the SFM conversion rather than converting back out of it.
    """
    baseline_smm = m_per_min * SURFACE_SPEED_SCALE
    baseline_sfm = baseline_smm * SFM_PER_M_MIN
    inch_pair = (round(baseline_sfm * ROUGH_TO_FINISH_RATIO, 1), round(baseline_sfm, 1))
    metric_pair = (round(baseline_smm * ROUGH_TO_FINISH_RATIO, 1), round(baseline_smm, 1))
    return inch_pair, metric_pair


def to_metric_params(inch_params, rough_smm, finish_smm):
    """Return the metric equivalent of one operation's inch params.

    Surface speeds are replaced with the natively-metric values; length
    values are converted; unit-neutral values (RPM, angles, dwell, counts)
    and mode strings are copied through unchanged, apart from units_mode
    itself, which is what drives G20/G21 downstream.
    """
    metric_params = {}
    for key, value in inch_params.items():
        if key == 'units_mode':
            metric_params[key] = 'MM'
        elif key in ROUGH_SFM_KEYS or key in SINGLE_SFM_ROUGH_LIKE_KEYS:
            metric_params[key] = rough_smm
        elif key in FINISH_SFM_KEYS:
            metric_params[key] = finish_smm
        elif key in LENGTH_KEYS:
            metric_params[key] = round(float(value) * MM_PER_INCH, 4)
        else:
            metric_params[key] = value
    return metric_params


def build_preset(label, m_per_min, kp, tier_data, whitelist_fn):
    (rough_sfm, finish_sfm), (rough_smm, finish_smm) = compute_surface_speeds(m_per_min)
    tier = tier_for_kp(kp)
    anchor = tier_data[tier]
    rpm_limit = TIER_RPM_LIMIT[tier]

    operations = {}
    for op_id, op_entry in anchor['operations'].items():
        op_type = op_entry['type']
        whitelist = set(whitelist_fn(op_type))
        src_params = op_entry.get('params', {})
        new_params = {k: v for k, v in src_params.items() if k in whitelist}

        for key in list(new_params.keys()):
            if key in ROUGH_SFM_KEYS:
                new_params[key] = rough_sfm
            elif key in FINISH_SFM_KEYS:
                new_params[key] = finish_sfm
            elif key in SINGLE_SFM_ROUGH_LIKE_KEYS:
                new_params[key] = rough_sfm
            elif key in RPM_CEILING_KEYS:
                new_params[key] = rpm_limit

        operations[op_id] = {
            'id': op_entry['id'],
            'type': op_type,
            'name': op_entry['name'],
            'enabled': op_entry.get('enabled', True),
            'params': new_params,
            'params_mm': to_metric_params(new_params, rough_smm, finish_smm),
            'preview_snapshot': {
                'snapshot_version': 2,
                'removal': {'geometry_table': []},
                'finish_boundary': {'finish_boundary_table': [], 'parameter_map': {}},
            },
        }

    # version 2 adds the params_mm slot alongside the inch params.
    return {
        'version': 2,
        'operations': operations,
        'operation_order': list(anchor['operation_order']),
    }


def main():
    whitelist_fn = load_whitelist_fn()

    tier_data = {}
    for tier, filename in TIER_ANCHORS.items():
        with open(os.path.join(HERE, filename), encoding='utf-8') as f:
            tier_data[tier] = json.load(f)

    for label, filename, m_per_min, kp in MATERIALS:
        preset = build_preset(label, m_per_min, kp, tier_data, whitelist_fn)
        out_path = os.path.join(HERE, filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(preset, f, indent=2)
            f.write('\n')
        print(f"wrote {filename} ({label}, tier={tier_for_kp(kp)})")

    old_alloys = os.path.join(HERE, 'alloys_preset.json')
    if os.path.isfile(old_alloys):
        os.remove(old_alloys)
        print("removed alloys_preset.json (superseded by specific grades)")


if __name__ == '__main__':
    main()
