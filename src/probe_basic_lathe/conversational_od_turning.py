"""
conversational_od_turning.py

Module for generating LinuxCNC G-code for OD turning operations in Probe Basic Lathe.
Configured for RADIUS MODE ONLY (G8).
"""

import math

def calculate_arc_boundary_intersection(x_center, z_center, radius, x_boundary):
    """Calculate where arc intersects the X boundary"""
    dx = x_boundary - x_center
    if abs(dx) > radius:
        return None  # No intersection
    
    dz_squared = radius**2 - dx**2
    if dz_squared < 0:
        return None
    
    dz = math.sqrt(dz_squared)
    
    # For our corner arcs, we want the intersection point that's closer to z_pass_end
    z_intersection_1 = z_center + dz
    z_intersection_2 = z_center - dz
    
    # Choose the Z that makes sense for corner arc direction (usually the lower Z)
    return z_intersection_2

def collect_od_turning_parameters_from_ui(ui):
    """
    Collect OD turning parameters using the YAML VCP setting names.
    Uses getSetting(setting_name).getValue() for each parameter.
    Adds debug output for each setting.
    """
    from qtpyvcp.utilities.settings import getSetting

    # Map: setting_name -> debug label
    setting_map = [
        ('turn-od.wcs', 'wcs'),
        ('turn-od.tool', 'tool'),
        ('turn-od.units', 'units'),
        ('turn-od.coolant', 'coolant'),
        ('turn-od.feed-mode', 'feed_mode'),
        ('turn-od.rough-feedrate', 'rough_feed'),
        ('turn-od.finish-feedrate', 'finish_feed'),
        ('turn-od.rpm-mode', 'rpm_mode'),
        ('turn-od.rpm', 'rpm'),
        ('turn-od.max-rpm', 'max_rpm'),
        ('turn-od.sf-speed-rough', 'rough_ssp'),
        ('turn-od.sf-speed-finish', 'finish_ssp'),
        ('turn-od.rotation', 'rotation'),
        ('turn-od.diam-rad', 'diam_rad_mode'),
        ('turn-od.x-start-diam', 'x_start'),
        ('turn-od.x-end-diam', 'x_end'),
        ('turn-od.z-start', 'z_start'),
        ('turn-od.z-end', 'z_end'),
        ('turn-od.rough-step', 'rough_step'),
        ('turn-od.finish-step', 'finish_step'),
        ('turn-od.corner-rad', 'corner_radius'),
        ('turn-od.z-taper', 'taper_angle'),
        ('turn-od.xz-clearance', 'xz_clearance'),
    ]

    params = {}
    for setting, label in setting_map:
        try:
            val = getSetting(setting).getValue()
            print(f"[DEBUG] Setting '{setting}' ({label}): {val}")
            params[label] = val
        except Exception as e:
            print(f"[DEBUG] Error getting setting '{setting}': {e}")
            params[label] = None

    print("[DEBUG] Final collected OD turning parameters (from settings):")
    for k, v in params.items():
        print(f"    {k}: {v}")
    return params

def generate_od_turning_gcode(params):
    """
    Generate LinuxCNC G-code for an OD turning operation using the provided parameters dict.
    """
    import math
    
    # Helper: get int or str for G/M codes
    def as_int(val, default=0):
        try:
            return int(float(val))
        except Exception:
            return default
    def as_float(val, default=0.0):
        try:
            return float(val)
        except Exception:
            return default
    def as_str(val, default=""):
        try:
            return str(val)
        except Exception:
            return default

    # G/M code mappings
    units_code = as_int(params.get('units', 20))
    gcode_units = 'G20' if units_code == 20 else 'G21'
    feed_mode_code = as_int(params.get('feed_mode', 94))
    gcode_feed_mode = 'G94' if feed_mode_code == 94 else 'G95'
    rpm_mode_code = as_int(params.get('rpm_mode', 96))
    gcode_rpm_mode = 'G96' if rpm_mode_code == 96 else 'G97'
    spindle_dir_code = as_int(params.get('rotation', 3))
    gcode_spindle_dir = 'M3' if spindle_dir_code == 3 else 'M4'
    coolant_code = as_int(params.get('coolant', 9))
    gcode_coolant = {7: 'M7', 8: 'M8', 9: 'M9'}.get(coolant_code, 'M9')
    wcs_val = params.get('wcs', 54)
    gcode_wcs = f"G{as_int(wcs_val, 54)}" if isinstance(wcs_val, (int, float)) or str(wcs_val).isdigit() else as_str(wcs_val, "G54")
    tool_val = as_int(params.get('tool', 0))

    # Numeric values - Convert diameter inputs to radius
    rpm_val = as_float(params.get('rpm', 500))
    max_rpm_val = as_float(params.get('max_rpm', 1000))
    rough_ssp_val = as_float(params.get('rough_ssp', 0))
    finish_ssp_val = as_float(params.get('finish_ssp', 0))
    rough_feed_val = as_float(params.get('rough_feed', 0.1))
    finish_feed_val = as_float(params.get('finish_feed', 0.05))
    xz_clearance_val = as_float(params.get('xz_clearance', 2))
    
    # CONVERT DIAMETER INPUTS TO RADIUS
    x_start_diameter = as_float(params.get('x_start', 50))
    x_end_diameter = as_float(params.get('x_end', 0))
    rough_step_diameter = as_float(params.get('rough_step', 1))
    finish_step_diameter = as_float(params.get('finish_step', 0.2))
    
    # Get user's preferred diameter/radius mode
    diam_rad_code = as_int(params.get('diam_rad_mode', 8))  # Default to radius mode
    gcode_diam_rad = 'G7' if diam_rad_code == 7 else 'G8'
    print(f"[DEBUG] UI sent diam_rad_mode: {params.get('diam_rad_mode')}, processed as: {diam_rad_code}")

    # Convert inputs to radius for internal calculations (if needed)
    if diam_rad_code == 7:  # User specified diameter mode
        x_start = x_start_diameter / 2  # Convert diameter input to radius
        x_end = x_end_diameter / 2 if x_end_diameter > 0 else 0
        rough_step = rough_step_diameter / 2
        finish_step = finish_step_diameter / 2
    else:  # User specified radius mode
        x_start = x_start_diameter  # Input is already radius
        x_end = x_end_diameter if x_end_diameter > 0 else 0
        rough_step = rough_step_diameter
        finish_step = finish_step_diameter
    
    z_start = as_float(params.get('z_start', 2))
    z_end = as_float(params.get('z_end', 0))
    corner_radius = as_float(params.get('corner_radius', 0))  # Already a radius
    taper_angle_deg = as_float(params.get('taper_angle', 0))

    # Calculate taper in radians and tangent
    taper_angle_rad = math.radians(taper_angle_deg)
    taper_tan = math.tan(taper_angle_rad)

    # Calculate X end at Z end, accounting for taper
    z_length = z_end - z_start
    x_end_tapered = x_start + (z_length * taper_tan)

    # If user provided x_end, use the smaller (for OD turning, tool moves in)
    if x_end > 0:
        x_end_final = min(x_end, x_end_tapered)
    else:
        x_end_final = x_end_tapered

    # Calculate number of passes (rough + finish)
    total_cut = abs(x_start - x_end_final)
    
    # Handle finish step logic
    if finish_step <= 0:
        # No separate finishing pass - use roughing steps all the way to final dimension
        # The last roughing pass will use finish feed rate and surface speed
        rough_distance = total_cut
        has_separate_finish_pass = False
    else:
        # Traditional rough + finish approach
        rough_distance = total_cut - finish_step
        has_separate_finish_pass = True
    
    x_positions = []
    if rough_distance <= 0:
        x_positions = [x_end_final]
    else:
        rough_passes_float = rough_distance / rough_step
        rough_passes = int(rough_passes_float)
        fractional = rough_passes_float - rough_passes

        direction = -1 if x_end_final < x_start else 1
        current_x = x_start
        if fractional > 1e-6:
            first_step = rough_step * fractional
            current_x += direction * first_step
            x_positions.append(round(current_x, 6))
        for i in range(rough_passes):
            current_x += direction * rough_step
            x_positions.append(round(current_x, 6))
        
        # Add finishing pass only if finish_step > 0
        if has_separate_finish_pass:
            x_positions.append(x_end_final)

    # PRE-CALCULATE FINISHING PASS GEOMETRY for roughing pass constraints
    finish_pass_geometry = None
    if corner_radius > 0 and taper_angle_deg != 0 and has_separate_finish_pass:
        # Calculate finish pass geometry once at the beginning
        finish_vertex_x = x_end_final + abs(z_end - z_start) * taper_tan
        finish_vertex_z = z_end
        
        angle_deg = abs(taper_angle_deg)
        interior_angle = 90 + angle_deg
        bisector_angle_deg = interior_angle / 2
        bisector_angle_rad = math.radians(bisector_angle_deg)
        supplementary_angle = 180 - interior_angle
        arc_start_offset_deg = supplementary_angle / 2
        
        # Calculate finish pass arc geometry
        center_distance = corner_radius / math.sin(bisector_angle_rad)
        finish_arc_center_x = finish_vertex_x + center_distance * math.cos(bisector_angle_rad)
        finish_arc_center_z = finish_vertex_z + center_distance * math.sin(bisector_angle_rad)
        
        vertex_to_center_dx = finish_arc_center_x - finish_vertex_x
        vertex_to_center_dz = finish_arc_center_z - finish_vertex_z
        vertex_center_angle = math.atan2(vertex_to_center_dz, vertex_to_center_dx)
        
        arc_start_angle = vertex_center_angle - math.radians(arc_start_offset_deg)
        finish_arc_start_x = finish_arc_center_x - corner_radius * math.cos(arc_start_angle)
        finish_arc_start_z = finish_arc_center_z - corner_radius * math.sin(arc_start_angle)
        
        finish_pass_geometry = {
            'arc_start_x': finish_arc_start_x,
            'arc_start_z': finish_arc_start_z,
            'arc_center_x': finish_arc_center_x,
            'arc_center_z': finish_arc_center_z,
            'vertex_x': finish_vertex_x,
            'vertex_z': finish_vertex_z
        }

    # --- G-code header with parameter dump ---
    gcode = f"""(OD Turning Operation Generated by Probe Basic Lathe - Corrected Taper Arcs)
(===== COLLECTED PARAMETERS =====)
(Units: {units_code} = {gcode_units})
(Diameter/Radius Mode: {diam_rad_code} = {gcode_diam_rad})
(Feed Mode: {feed_mode_code} = {gcode_feed_mode})
(RPM Mode: {rpm_mode_code} = {gcode_rpm_mode})
(WCS: {wcs_val} = {gcode_wcs})
(Tool: {tool_val})
(Spindle Direction: {spindle_dir_code} = {gcode_spindle_dir})
(Coolant: {coolant_code} = {gcode_coolant})
(===== FEED & SPEED VALUES =====)
(Rough Feed: {rough_feed_val})
(Finish Feed: {finish_feed_val})
(RPM: {rpm_val})
(Max RPM: {max_rpm_val})
(Rough Surface Speed: {rough_ssp_val})
(Finish Surface Speed: {finish_ssp_val})
(===== DIMENSIONS - INPUT CONVERSION =====)
(Mode: {gcode_diam_rad})
(X Start Input: {x_start_diameter} -> Internal Radius: {x_start})
(X End Input: {x_end_diameter} -> Internal Radius: {x_end})
(Z Start: {z_start})
(Z End: {z_end})
(Rough Step Input: {rough_step_diameter} -> Internal Radius: {rough_step})
(Finish Step Input: {finish_step_diameter} -> Internal Radius: {finish_step})
(Corner Radius: {corner_radius})
(Taper Angle deg: {taper_angle_deg})
(XZ Clearance: {xz_clearance_val})
(===== CALCULATED VALUES =====)
(Taper Angle rad: {taper_angle_rad:.6f})
(Taper Tangent: {taper_tan:.6f})
(Z Length: {z_length})
(X End Tapered: {x_end_tapered})
(X End Final: {x_end_final})
(Total Cut: {total_cut})
(Rough Distance: {rough_distance})
(Has Separate Finish Pass: {has_separate_finish_pass})
(Direction: {direction})
(X Positions: {x_positions})
{gcode_units} (Set units)
{gcode_diam_rad} (User's preferred mode)
G18 (XZ plane select)
{gcode_feed_mode} (Feed mode)
{gcode_wcs} (Work coordinate system)
T{tool_val} (Tool number)
M6 (Tool change)
G43 (Apply tool length/geometry offset)
{gcode_coolant} (Coolant)
{gcode_spindle_dir} (Spindle direction)
"""

    # Spindle speed and mode
    if gcode_rpm_mode == 'G97':
        gcode += f"S{rpm_val:.4f} (Spindle RPM)\n"
        gcode += f"{gcode_rpm_mode} (RPM mode)\n"
    elif gcode_rpm_mode == 'G96':
        gcode += f"{gcode_rpm_mode} D{max_rpm_val:.4f} S{rough_ssp_val:.4f} (CSS: D=Max RPM, S=Surface Speed)\n"

    gcode += "M3 (Spindle start)\n" if gcode_spindle_dir == 'M3' else "M4 (Spindle start, reverse)\n"

    # --- Helper functions ---
    def x_output(val):
        """Convert radius coordinates to user's preferred coordinate system"""
        if diam_rad_code == 7:  # User wants diameter mode output
            return val * 2  # Convert radius to diameter for G-code
        else:  # User wants radius mode output
            return val  # Already in radius

    def add_safe_interpolated_move(current_gcode, x_start, z_start, x_end, z_end, feed_rate):
        """Add an interpolated move that respects safety boundaries by truncating at boundary"""
        x_safe_limit = x_start + abs(xz_clearance_val)
        
        # Check if end position violates X boundary
        if x_end > x_safe_limit:
            # Calculate where the move intersects the safety boundary
            if abs(x_end - x_start) > 1e-6:  # Avoid division by zero
                z_at_boundary = z_start + (z_end - z_start) * (x_safe_limit - x_start) / (x_end - x_start)
                current_gcode += f"(Safety: Move truncated at boundary X={x_output(x_safe_limit):.4f}, Z={z_at_boundary:.4f})\n"
                current_gcode += f"G1 X{x_output(x_safe_limit):.4f} Z{z_at_boundary:.4f} F{feed_rate:.4f}\n"
                return current_gcode, True
            else:
                current_gcode += f"(Safety: X position limited to boundary)\n"
                current_gcode += f"G1 X{x_output(x_safe_limit):.4f} Z{z_end:.4f} F{feed_rate:.4f}\n"
                return current_gcode, True
        else:
            current_gcode += f"G1 X{x_output(x_end):.4f} Z{z_end:.4f} F{feed_rate:.4f}\n"
            return current_gcode, False

    # Define safety boundaries
    x_safe_limit = x_start + abs(xz_clearance_val)
    z_safe_limit = z_start + abs(xz_clearance_val)

    gcode += f"(===== SAFETY BOUNDARIES =====)\n"
    gcode += f"(X Safe Limit: {x_output(x_safe_limit):.4f})\n"
    gcode += f"(Z Safe Limit: {z_safe_limit:.4f})\n"
    gcode += f"(Intelligent boundary checking: Moves crossing X limit will be truncated)\n"

    # PRE-CALCULATE LAST ROUGHING PASS GEOMETRY for non-tapered conditions with corner radius
    last_roughing_pass_geometry = None
    roughing_transition_points = {}
    
    if corner_radius > 0 and taper_angle_deg == 0 and has_separate_finish_pass:
        # Calculate the last roughing pass geometry (finish pass offset by finish_step)
        last_rough_x = x_end_final + finish_step
        last_rough_z = z_end + finish_step  # CORRECTED: Last roughing Z should be offset from finish
        
        # Last roughing pass arc geometry (90-degree corner offset from finish)
        last_rough_arc_center_x = last_rough_x + corner_radius
        last_rough_arc_center_z = last_rough_z + corner_radius
        last_rough_arc_start_z = last_rough_z + corner_radius
        last_rough_arc_end_x = last_rough_x + corner_radius
        last_rough_arc_end_z = last_rough_z  # CORRECTED: Arc ends at last roughing Z
        
        last_roughing_pass_geometry = {
            'x_pos': last_rough_x,
            'z_pos': last_rough_z,
            'arc_center_x': last_rough_arc_center_x,
            'arc_center_z': last_rough_arc_center_z,
            'arc_start_z': last_rough_arc_start_z,
            'arc_end_x': last_rough_arc_end_x,
            'arc_end_z': last_rough_arc_end_z,
            'radius': corner_radius
        }
        
        # Calculate transition points for each roughing pass using roughing_step intervals
        roughing_x_positions = x_positions[:-1] if has_separate_finish_pass else x_positions
        
        gcode += f"(===== LAST ROUGHING PASS GEOMETRY CALCULATION =====)\n"
        gcode += f"(Last roughing X: {last_rough_x:.4f}, Z: {last_rough_z:.4f})\n"
        gcode += f"(Arc center: X={last_rough_arc_center_x:.4f}, Z={last_rough_arc_center_z:.4f})\n"
        gcode += f"(Arc radius: {corner_radius:.4f})\n"
        
        for i, rough_x in enumerate(roughing_x_positions):
            # Determine if this roughing pass needs a transition point
            # Only passes SMALLER than arc center X get arcs (use >= for at/beyond)
            if rough_x < last_rough_arc_center_x:
                # This pass is inside the arc center - needs transition
                # Calculate where this X intersects the last roughing arc
                dx_from_center = last_rough_arc_center_x - rough_x
                
                if dx_from_center <= corner_radius:
                    # Calculate Z position on arc at this X
                    dz_from_center = math.sqrt(corner_radius**2 - dx_from_center**2)
                    transition_z = last_rough_arc_center_z - dz_from_center
                    
                    # Cascading arc end positions: end at previous pass's X position
                    if i == 0:
                        # First arc pass ends at reference arc center
                        arc_end_x_for_this_pass = last_rough_arc_center_x
                        arc_end_z_for_this_pass = last_rough_arc_center_z - corner_radius
                    else:
                        # Subsequent passes end at previous pass's X position
                        arc_end_x_for_this_pass = roughing_x_positions[i - 1]
                        # Calculate correct Z position to maintain radius from arc center
                        dx_to_end = last_rough_arc_center_x - arc_end_x_for_this_pass
                        if dx_to_end <= corner_radius:
                            dz_to_end = math.sqrt(corner_radius**2 - dx_to_end**2)
                            arc_end_z_for_this_pass = last_rough_arc_center_z - dz_to_end
                        else:
                            # Fallback to bottom of arc if geometry invalid
                            arc_end_z_for_this_pass = last_rough_arc_center_z - corner_radius
                    
                    roughing_transition_points[rough_x] = {
                        'transition_z': transition_z,
                        'arc_center_x': last_rough_arc_center_x,
                        'arc_center_z': last_rough_arc_center_z,
                        'arc_end_x': arc_end_x_for_this_pass,
                        'arc_end_z': arc_end_z_for_this_pass,
                        'radius': corner_radius
                    }
                    gcode += f"(Roughing X={rough_x:.4f} transition at Z={transition_z:.4f}, arc to X={arc_end_x_for_this_pass:.4f})\n"
                else:
                    gcode += f"(Roughing X={rough_x:.4f} beyond arc radius - no transition)\n"
            else:
                gcode += f"(Roughing X={rough_x:.4f} at/beyond arc center - straight cut)\n"

    # --- OD turning passes ---
    for i, x_pos in enumerate(x_positions):
        is_last = (i == len(x_positions) - 1)
        
        # Determine if this is a finishing pass
        is_finish_pass = (has_separate_finish_pass and is_last) or (not has_separate_finish_pass and is_last)
        
        # Select appropriate feed rate and surface speed
        if is_finish_pass:
            feed = finish_feed_val
            surface_speed = finish_ssp_val if gcode_rpm_mode == 'G96' else rpm_val
            pass_type = "Finishing"
        else:
            feed = rough_feed_val
            surface_speed = rough_ssp_val if gcode_rpm_mode == 'G96' else rpm_val
            pass_type = "Roughing"
        
        z_safe = z_start + abs(xz_clearance_val)

        # Calculate Z for this pass
        if has_separate_finish_pass and is_last:
            z_pass_end = z_end
        else:
            z_finish = abs(finish_step)
            z_pass_end = z_end + z_finish if z_end < z_start else z_end - z_finish

        gcode += f"(Pass {i+1}: {pass_type} at X={x_output(x_pos):.4f})\n"
        
        # Update spindle speed if needed
        if gcode_rpm_mode == 'G96' and i > 0:
            gcode += f"G96 D{max_rpm_val:.4f} S{surface_speed:.4f} (CSS: Surface Speed for {pass_type})\n"
        
        # Safe positioning moves
        gcode += f"G0 Z{z_safe:.4f}\n"
        x_approach = min(x_pos, x_safe_limit)
        if x_pos > x_safe_limit:
            gcode += f"(Safety: Approach position limited from {x_output(x_pos):.4f} to {x_output(x_safe_limit):.4f})\n"
        gcode += f"G0 X{x_output(x_approach):.4f}\n"
        gcode += f"G1 X{x_output(x_pos):.4f} F{feed:.4f}\n"
        gcode += f"G1 Z{z_start:.4f}\n"

        # Calculate taper geometry
        if taper_angle_deg != 0:
            dz = z_pass_end - z_start
            dx = dz * taper_tan
            x_end_pass = x_pos - dx  # For OD turning: part gets larger toward chuck
            
            # Vertex is where taper line meets the END Z position
            vertex_x = x_end_pass
            vertex_z = z_pass_end
            
            # Calculate angles for arc geometry
            angle_deg = abs(taper_angle_deg)
            interior_angle = 90 + angle_deg  # CORRECT: 95° for 5° taper
            bisector_angle_deg = interior_angle / 2  # CORRECT: 47.5° for 5° taper
            bisector_angle_rad = math.radians(bisector_angle_deg)
        else:
            x_end_pass = x_pos

        gcode += f"(x_pos: {x_pos}, x_end_pass: {x_end_pass}, z_pass_end: {z_pass_end})\n"

        # Arc calculation for corner radius
        if corner_radius > 0:
            if taper_angle_deg == 0:
                # Check if this roughing pass has a pre-calculated transition point
                if x_pos in roughing_transition_points and not is_finish_pass:
                    # Use sophisticated transition strategy
                    transition_data = roughing_transition_points[x_pos]
                    gcode += f"(Using pre-calculated transition strategy)\n"
                    
                    # Cut straight down to transition point
                    transition_z = transition_data['transition_z']
                    if not math.isclose(z_start, transition_z, abs_tol=1e-6):
                        gcode += f"G1 Z{transition_z:.4f}\n"
                    
                    # Follow the last roughing arc from current position to arc end
                    arc_center_x = transition_data['arc_center_x']
                    arc_center_z = transition_data['arc_center_z']
                    arc_end_x = transition_data['arc_end_x']
                    arc_end_z = transition_data['arc_end_z']
                    
                    # Calculate I,K offsets for arc move
                    i_offset = arc_center_x - x_pos
                    k_offset = arc_center_z - transition_z
                    
                    gcode += f"(Following last roughing arc: center X={arc_center_x:.4f}, Z={arc_center_z:.4f})\n"
                    gcode += f"G2 X{x_output(arc_end_x):.4f} Z{arc_end_z:.4f} I{i_offset:.4f} K{k_offset:.4f}\n"
                else:
                    # Calculate dynamic apex detection for this parameter set
                    if corner_radius > 0 and has_separate_finish_pass:
                        # Dynamically calculate the arc center for current parameters
                        current_last_rough_x = x_end_final + finish_step
                        current_arc_center_x = current_last_rough_x + corner_radius
                        
                        # Check if this pass is at/beyond the dynamically calculated arc center
                        if x_pos >= current_arc_center_x:
                            # This pass is at/beyond arc center - use straight cut
                            gcode += f"(Pass at/beyond dynamic arc center X={current_arc_center_x:.4f} - using straight cut)\n"
                            gcode += f"G1 Z{z_pass_end:.4f}\n"
                            gcode += f"G1 X{x_output(x_end_pass):.4f} F{feed:.4f}\n"
                        else:
                            # Use traditional 90-degree corner logic
                            arc_start_z = z_pass_end + abs(corner_radius)
                            arc_end_x = x_pos + abs(corner_radius)
                            arc_end_z = z_pass_end
                            
                            if arc_end_x <= x_safe_limit:
                                arc_center_x = arc_end_x
                                arc_center_z = z_pass_end + abs(corner_radius)
                                i_offset = arc_center_x - x_pos
                                k_offset = arc_center_z - arc_start_z
                                
                                if not math.isclose(z_start, arc_start_z, abs_tol=1e-6):
                                    gcode += f"G1 Z{arc_start_z:.4f}\n"
                                gcode += f"G2 X{x_output(arc_end_x):.4f} Z{arc_end_z:.4f} I{i_offset:.4f} K{k_offset:.4f}\n"
                            else:
                                gcode += f"(Arc exceeds boundaries - using straight cut)\n"
                                gcode, _ = add_safe_interpolated_move(gcode, x_pos, z_start, x_end_pass, z_pass_end, feed)
                    else:
                        # No corner radius - use straight cut
                        gcode += f"G1 Z{z_pass_end:.4f}\n"
                        gcode += f"G1 X{x_output(x_end_pass):.4f} F{feed:.4f}\n"
            else:
                # CORRECTED TAPER ARC CALCULATION
                if angle_deg > 0:
                    if is_finish_pass:
                        # CORRECTED: Calculate proper arc start angle from taper angle
                        supplementary_angle = 180 - interior_angle  # 85° for 5° taper
                        arc_start_offset_deg = supplementary_angle / 2  # 42.5° for 5° taper
                        
                        # Calculate arc geometry using CORRECTED formulas
                        center_distance = corner_radius / math.sin(bisector_angle_rad)
                        arc_center_x = vertex_x + center_distance * math.cos(bisector_angle_rad)
                        arc_center_z = vertex_z + center_distance * math.sin(bisector_angle_rad)
                        
                        # Calculate arc start using CORRECTED angle (not hard-coded 37.5°)
                        vertex_to_center_dx = arc_center_x - vertex_x
                        vertex_to_center_dz = arc_center_z - vertex_z
                        vertex_center_angle = math.atan2(vertex_to_center_dz, vertex_to_center_dx)
                        
                        # Use CALCULATED arc start offset, not hard-coded 37.5°
                        arc_start_angle = vertex_center_angle - math.radians(arc_start_offset_deg)
                        x_arc_start = arc_center_x - corner_radius * math.cos(arc_start_angle)
                        z_arc_start = arc_center_z - corner_radius * math.sin(arc_start_angle)
                        
                        # Arc end X matches arc center X position
                        arc_end_x = arc_center_x
                        arc_end_z = vertex_z
                        
                        # Calculate I,K offsets
                        i_offset = arc_center_x - x_arc_start
                        k_offset = arc_center_z - z_arc_start
                        
                        gcode += f"(FINISH CORRECTED: interior_angle={interior_angle:.1f}°, bisector={bisector_angle_deg:.1f}°)\n"
                        gcode += f"(FINISH CORRECTED: supplementary={supplementary_angle:.1f}°, arc_offset={arc_start_offset_deg:.1f}°)\n"
                        gcode += f"(FINISH CORRECTED: vertex X={vertex_x:.4f}, Z={vertex_z:.4f})\n"
                        gcode += f"(FINISH CORRECTED: center X={arc_center_x:.4f}, Z={arc_center_z:.4f})\n"
                        gcode += f"(FINISH CORRECTED: start X={x_arc_start:.4f}, Z={z_arc_start:.4f})\n"
                        gcode += f"(FINISH CORRECTED: end X={arc_end_x:.4f}, Z={arc_end_z:.4f})\n"
                        gcode += f"(FINISH CORRECTED: I={i_offset:.4f}, K={k_offset:.4f})\n"
                        
                        expected_radius = corner_radius
                    else:
                        # Roughing passes: CONSTRAINED by finishing pass geometry
                        if finish_pass_geometry and not is_finish_pass:
                            # Calculate what the finishing pass profile looks like at this Z level
                            rough_z_level = z_pass_end
                            
                            # Check if we're in the arc region
                            if rough_z_level >= finish_pass_geometry['arc_start_z']:
                                # We're in the arc region - calculate max allowed X at this Z
                                arc_center_x = finish_pass_geometry['arc_center_x']
                                arc_center_z = finish_pass_geometry['arc_center_z']
                                
                                # Calculate X position on finishing arc at this Z level
                                dz = rough_z_level - arc_center_z
                                if abs(dz) <= corner_radius:
                                    dx_from_center = math.sqrt(corner_radius**2 - dz**2)
                                    max_allowed_x_at_z = arc_center_x - dx_from_center
                                    
                                    # Ensure roughing doesn't exceed finishing profile
                                    if vertex_x > max_allowed_x_at_z:
                                        gcode += f"(Roughing constrained: vertex limited from {vertex_x:.4f} to {max_allowed_x_at_z:.4f})\n"
                                        vertex_x = max_allowed_x_at_z
                                else:
                                    # Beyond arc radius - use straight line constraint
                                    max_allowed_x_at_z = finish_pass_geometry['vertex_x']
                                    if vertex_x > max_allowed_x_at_z:
                                        gcode += f"(Roughing constrained: vertex limited from {vertex_x:.4f} to {max_allowed_x_at_z:.4f})\n"
                                        vertex_x = max_allowed_x_at_z
                        
                        # Now calculate roughing arc with constrained vertex
                        max_allowed_x = x_safe_limit
                        effective_radius = min(corner_radius, max_allowed_x - vertex_x)
                        
                        # Use same corrected angle calculation for roughing
                        supplementary_angle = 180 - interior_angle
                        arc_start_offset_deg = supplementary_angle / 2
                        
                        center_distance = effective_radius / math.sin(bisector_angle_rad)
                        arc_center_x = vertex_x + center_distance * math.cos(bisector_angle_rad)
                        arc_center_z = vertex_z + center_distance * math.sin(bisector_angle_rad)
                        
                        vertex_to_center_dx = arc_center_x - vertex_x
                        vertex_to_center_dz = arc_center_z - vertex_z
                        vertex_center_angle = math.atan2(vertex_to_center_dz, vertex_to_center_dx)
                        
                        arc_start_angle = vertex_center_angle - math.radians(arc_start_offset_deg)
                        x_arc_start = arc_center_x - effective_radius * math.cos(arc_start_angle)
                        z_arc_start = arc_center_z - effective_radius * math.sin(arc_start_angle)
                        
                        arc_end_x = arc_center_x
                        arc_end_z = vertex_z
                        expected_radius = effective_radius
                        
                        gcode += f"(Roughing arc: scaled radius={effective_radius:.4f} from full={corner_radius:.4f})\n"
                        gcode += f"(Arc maintains tangency: center X={arc_center_x:.4f}, Z={arc_center_z:.4f})\n"

                    # Geometry validation
                    if arc_end_x <= x_safe_limit and expected_radius > 0:
                        geometry_valid = True
                        gcode += f"(Progressive taper arc: radius={expected_radius:.4f}, finish_pass={is_finish_pass})\n"
                        
                        if is_finish_pass:
                            # Validate I,K offsets
                            calculated_radius = math.sqrt(i_offset**2 + k_offset**2)
                            radius_error = abs(calculated_radius - expected_radius)
                            if radius_error > 0.001:
                                gcode += f"(WARNING: I,K radius mismatch - calculated: {calculated_radius:.4f}, expected: {expected_radius:.4f})\n"
                            gcode += f"(I,K validation: I={i_offset:.4f}, K={k_offset:.4f}, calc_radius={calculated_radius:.4f})\n"
                    else:
                        geometry_valid = False
                        gcode += f"(Arc exceeds boundaries: arc_end_x={arc_end_x:.4f} > safe_limit={x_safe_limit:.4f})\n"
                    
                    gcode += f"(Geometry valid: {geometry_valid})\n"
                    
                    if geometry_valid:
                        if not math.isclose(z_start, z_arc_start, abs_tol=1e-6):
                            gcode += f"G1 X{x_output(x_arc_start):.4f} Z{z_arc_start:.4f} F{feed:.4f}\n"
                        
                        if is_finish_pass:
                            # Use I,K mode for finishing pass
                            gcode += f"G2 X{x_output(arc_end_x):.4f} Z{arc_end_z:.4f} I{i_offset:.4f} K{k_offset:.4f}\n"
                        else:
                            # Use R mode for roughing passes
                            gcode += f"G2 X{x_output(arc_end_x):.4f} Z{arc_end_z:.4f} R{expected_radius:.4f}\n"
                    else:
                        gcode += f"(Using straight cut - arc geometry invalid)\n"
                        gcode, _ = add_safe_interpolated_move(gcode, x_pos, z_start, x_end_pass, z_pass_end, feed)
        else:
            # No corner radius - handle taper or straight cut
            if taper_angle_deg != 0:
                gcode, was_truncated = add_safe_interpolated_move(gcode, x_pos, z_start, x_end_pass, z_pass_end, feed)
            else:
                gcode += f"G1 Z{z_pass_end:.4f}\n"
                gcode += f"G1 X{x_output(x_end_pass):.4f} F{feed:.4f}\n"

        # Final cut move to complete face - cascading feedout strategy
        if is_finish_pass:
            # Finishing pass feeds out to X start position (traditional behavior)
            x_final_cut = x_start
        elif i == 0:
            # First roughing pass feeds out to X start position
            x_final_cut = x_start
        else:
            # Subsequent roughing passes feed out to previous pass's X position
            x_final_cut = x_positions[i - 1]
        
        gcode += f"(Final cut move to previous pass X position for cascading)\n"
        gcode += f"G1 X{x_output(x_final_cut):.4f} F{feed:.4f}\n"
        
        # Smart retraction
        gcode += f"G0 Z{z_safe:.4f}\n"
        
        if i < len(x_positions) - 1:
            next_x = x_positions[i + 1]
            x_safe_next = next_x + xz_clearance_val if direction == -1 else next_x - xz_clearance_val
            if x_safe_next > x_safe_limit:
                gcode += f"(Safety: Next position limited to safe boundary)\n"
                x_safe_next = x_safe_limit
            gcode += f"G0 X{x_output(x_safe_next):.4f}\n"
        else:
            gcode += f"(Final retraction to safe boundary)\n"
            gcode += f"G0 X{x_output(x_safe_limit):.4f}\n"

    gcode += "M5 (Spindle stop)\n"
    gcode += "M9 (Coolant off)\n"
    gcode += "M30 (End of program)\n"
    return gcode
    
    # DELETE EVERYTHING BELOW THIS LINE - it's unreachable code!