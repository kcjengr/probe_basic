"""
conversational_od_turning.py

Module for generating LinuxCNC G-code for OD turning operations in Probe Basic Lathe.
Configured for RADIUS MODE ONLY (G8).
"""

import math

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
        ('turn-od.diam-rad', 'diam_rad_mode'),  # ADD THIS LINE
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

    # --- G-code header with parameter dump ---
    gcode = f"""(OD Turning Operation Generated by Probe Basic Lathe - Dual Mode Support)
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

    # --- OD turning passes - RADIUS MODE ONLY ---
    # Helper functions simplified for radius mode only
    def x_output(val):
        """Convert radius coordinates to user's preferred coordinate system"""
        if diam_rad_code == 7:  # User wants diameter mode output
            return val * 2  # Convert radius to diameter for G-code
        else:  # User wants radius mode output
            return val  # Already in radius

    # Test the function immediately
    print(f"[DEBUG] Testing x_output(0.5) with diam_rad_code={diam_rad_code}: {x_output(0.5)}")

    # Define safety boundaries based on user input + clearance
    x_safe_limit = x_start + abs(xz_clearance_val)  # Furthest safe X position
    z_safe_limit = z_start + abs(xz_clearance_val)  # Furthest safe Z position
    
    def add_safe_interpolated_move(current_gcode, x_start, z_start, x_end, z_end, feed_rate):
        """Add an interpolated move that respects safety boundaries by truncating at boundary"""
        # Check if end position violates X boundary
        if x_end > x_safe_limit:
            # Calculate where the move intersects the safety boundary
            # For linear interpolation: find Z position when X = x_safe_limit
            if abs(x_end - x_start) > 1e-6:  # Avoid division by zero
                # Linear interpolation: z = z_start + (z_end - z_start) * (x_safe_limit - x_start) / (x_end - x_start)
                z_at_boundary = z_start + (z_end - z_start) * (x_safe_limit - x_start) / (x_end - x_start)
                current_gcode += f"(Safety: Move truncated at boundary X={x_output(x_safe_limit):.4f}, Z={z_at_boundary:.4f})\n"
                current_gcode += f"G1 X{x_output(x_safe_limit):.4f} Z{z_at_boundary:.4f} F{feed_rate:.4f}\n"
                return current_gcode, True  # Return True to indicate move was truncated
            else:
                # Pure Z move - just limit X and complete Z move
                current_gcode += f"(Safety: X position limited to boundary)\n"
                current_gcode += f"G1 X{x_output(x_safe_limit):.4f} Z{z_end:.4f} F{feed_rate:.4f}\n"
                return current_gcode, True
        else:
            # Normal move - no boundary violation
            current_gcode += f"G1 X{x_output(x_end):.4f} Z{z_end:.4f} F{feed_rate:.4f}\n"
            return current_gcode, False
    
    def add_safe_move(current_gcode, x_target, z_target=None, is_rapid=False, feed_rate=None):
        """Add a move to G-code, ensuring it stays within safety boundaries"""
        move_type = "G0" if is_rapid else "G1"
        feed_str = f" F{feed_rate:.4f}" if feed_rate and not is_rapid else ""
        
        # Check X boundary
        if x_target > x_safe_limit:
            current_gcode += f"(Safety: X move limited from {x_output(x_target):.4f} to {x_output(x_safe_limit):.4f})\n"
            x_target = x_safe_limit
        
        # Check Z boundary if specified
        if z_target is not None:
            if z_target > z_safe_limit:
                current_gcode += f"(Safety: Z move limited from {z_target:.4f} to {z_safe_limit:.4f})\n"
                z_target = z_safe_limit
            current_gcode += f"{move_type} X{x_output(x_target):.4f} Z{z_target:.4f}{feed_str}\n"
        else:
            current_gcode += f"{move_type} X{x_output(x_target):.4f}{feed_str}\n"
        
        return current_gcode

    gcode += f"(===== SAFETY BOUNDARIES =====)\n"
    gcode += f"(X Safe Limit: {x_output(x_safe_limit):.4f})\n"
    gcode += f"(Z Safe Limit: {z_safe_limit:.4f})\n"
    gcode += f"(Intelligent boundary checking: Moves crossing X limit will be truncated)\n"

    for i, x_pos in enumerate(x_positions):
        is_last = (i == len(x_positions) - 1)
        
        # Determine if this is a finishing pass (separate finish pass OR last roughing pass when finish_step = 0)
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
        
        x_safe = x_pos + xz_clearance_val if direction == -1 else x_pos - xz_clearance_val
        z_safe = z_start + abs(xz_clearance_val)

        # Calculate Z for this pass: leave finish_step on the back wall until finishing pass
        if has_separate_finish_pass and is_last:
            z_pass_end = z_end
        else:
            z_finish = abs(finish_step)  # No diameter conversion needed in radius mode
            z_pass_end = z_end + z_finish if z_end < z_start else z_end - z_finish

        # Calculate X finish move for this pass: use safety boundaries intelligently
        if has_separate_finish_pass and is_last:
            x_finish_offset = abs(finish_step)  # No diameter conversion needed in radius mode
            x_finish_raw = x_start + abs(xz_clearance_val) + x_finish_offset
            x_finish = min(x_finish_raw, x_safe_limit)  # Respect safety boundary
        else:
            x_finish = x_safe_limit  # Use safety boundary for roughing passes

        gcode += f"(Pass {i+1}: {pass_type} at X={x_output(x_pos):.4f})\n"
        
        # Update spindle speed if needed for this pass
        if gcode_rpm_mode == 'G96' and i > 0:  # Don't repeat on first pass
            gcode += f"G96 D{max_rpm_val:.4f} S{surface_speed:.4f} (CSS: Surface Speed for {pass_type})\n"
        
        # Safe positioning moves with boundary checks
        gcode += f"G0 Z{z_safe:.4f}\n"
        # Ensure rapid X move respects safety boundary
        x_approach = min(x_pos, x_safe_limit)
        if x_pos > x_safe_limit:
            gcode += f"(Safety: Approach position limited from {x_output(x_pos):.4f} to {x_output(x_safe_limit):.4f})\n"
        gcode += f"G0 X{x_output(x_approach):.4f}\n"
        gcode += f"G1 X{x_output(x_pos):.4f} F{feed:.4f}\n"
        gcode += f"G1 Z{z_start:.4f}\n"

        # --- TAPER LOGIC: CORRECTED FOR OD TURNING ---
        if taper_angle_deg != 0:
            # Calculate X change based on taper angle
            dz = z_pass_end - z_start  # This will be negative for normal turning (-1.0)
            dx = dz * taper_tan  # This will be negative for 15° taper
            # For OD turning: part should get LARGER toward chuck (negative Z direction)
            x_end_pass = x_pos - dx  # Since dx is negative, subtracting it increases x_pos
            
            # The vertex is where taper line meets the END Z position
            vertex_x = x_end_pass  
            vertex_z = z_pass_end  
            
            # Calculate angles for arc geometry
            angle_deg = abs(taper_angle_deg)
            interior_angle = 90 + angle_deg  # 105° for 15° taper
            bisector_angle_deg = interior_angle / 2  # 52.5° for 15° taper
            bisector_angle_rad = math.radians(bisector_angle_deg)
        else:
            x_end_pass = x_pos

        # Debug output after x_end_pass is calculated
        gcode += f"(  x_pos: {x_pos}, x_end_pass: {x_end_pass}, z_pass_end: {z_pass_end})\n"

        cleanup_step = finish_step if (has_separate_finish_pass and is_last) else rough_step
        x_cleanup = x_pos + abs(cleanup_step)
        x_finish = x_start + abs(xz_clearance_val) + (abs(finish_step) if (has_separate_finish_pass and is_last) else 0)

        if corner_radius > 0:
            if taper_angle_deg == 0:
                # No taper - simple 90-degree corner - SIMPLIFIED FOR RADIUS MODE
                arc_start_z = z_pass_end + abs(corner_radius)
                arc_end_x = x_pos + abs(corner_radius)  # Simple addition in radius mode
                arc_end_z = z_pass_end
                
                # Check if arc sequence will violate boundaries
                if arc_end_x > x_safe_limit:
                    gcode += f"(Safety: Arc would exceed boundary, using straight cut to boundary)\n"
                    if not math.isclose(z_start, arc_start_z, abs_tol=1e-6):
                        gcode += f"G1 Z{arc_start_z:.4f}\n"
                    gcode += f"G1 X{x_output(x_safe_limit):.4f} Z{arc_end_z:.4f} F{feed:.4f}\n"
                    gcode += f"(Arc skipped - would exceed safety boundary)\n"
                else:
                    if not math.isclose(z_start, arc_start_z, abs_tol=1e-6):
                        gcode += f"G1 Z{arc_start_z:.4f}\n"
                    
                    gcode += f"(  Arc: Start at {x_output(x_pos):.4f}, {arc_start_z:.4f} to End at {x_output(arc_end_x):.4f}, {arc_end_z:.4f})\n"
                    gcode += f"(  Using R-mode with radius: {abs(corner_radius):.4f})\n"
                    gcode += f"G2 X{x_output(arc_end_x):.4f} Z{arc_end_z:.4f} R{abs(corner_radius):.4f}\n"
                    
                    # Cleanup
                    if is_finish_pass:
                        gcode = add_safe_move(gcode, x_finish, None, False, feed)
                    else:
                        x_cleanup_arc = arc_end_x + abs(cleanup_step)
                        if x_cleanup_arc > x_safe_limit:
                            gcode += f"(Safety: Cleanup limited, retracting to safe position)\n"
                            gcode = add_safe_move(gcode, x_safe_limit, None, False, feed)
                        else:
                            gcode += f"G1 X{x_output(x_cleanup_arc):.4f} F{feed:.4f}\n"
            else:
                # SIMPLIFIED TAPER ARC CALCULATION FOR RADIUS MODE
                if angle_deg > 0:
                    # Calculate arc center - SIMPLIFIED
                    center_distance = corner_radius / math.sin(bisector_angle_rad)
                    arc_center_x = vertex_x + center_distance * math.cos(bisector_angle_rad)  # No diameter scaling
                    arc_center_z = vertex_z + center_distance * math.sin(bisector_angle_rad)
                    
                    # Calculate arc start using 37.5° method - SIMPLIFIED
                    vertex_to_center_dx = arc_center_x - vertex_x
                    vertex_to_center_dz = arc_center_z - vertex_z
                    vertex_center_angle = math.atan2(vertex_to_center_dz, vertex_to_center_dx)
                    
                    # Arc start is at 37.5° from vertex-center line
                    arc_start_angle = vertex_center_angle - math.radians(37.5)
                    x_arc_start = arc_center_x - corner_radius * math.cos(arc_start_angle)  # No diameter scaling
                    z_arc_start = arc_center_z - corner_radius * math.sin(arc_start_angle)
                    
                    # Arc end X must match arc center X position
                    arc_end_x = arc_center_x  # Same X as center
                    arc_end_z = vertex_z  # Z at the vertex level
                else:
                    # Zero angle case - simple 90-degree corner
                    arc_center_x = vertex_x + corner_radius
                    arc_center_z = vertex_z + corner_radius
                    x_arc_start = vertex_x
                    z_arc_start = vertex_z + corner_radius
                    arc_end_x = vertex_x + corner_radius
                    arc_end_z = vertex_z

                expected_radius = corner_radius
                
                # SIMPLIFIED GEOMETRY VALIDATION FOR RADIUS MODE
                arc_distance = math.sqrt((arc_end_x - x_arc_start)**2 + (arc_end_z - z_arc_start)**2)
                max_chord = 2 * corner_radius

                # Radius checks - NO COORDINATE CONVERSION NEEDED
                start_radius = math.sqrt((x_arc_start - arc_center_x)**2 + (z_arc_start - arc_center_z)**2)
                end_radius = math.sqrt((arc_end_x - arc_center_x)**2 + (arc_end_z - arc_center_z)**2)
                
                gcode += f"(Simplified Radius Mode Arc: angle={taper_angle_deg:.1f}°, radius={corner_radius:.4f})\n"
                gcode += f"(Vertex at X={vertex_x:.4f}, Z={vertex_z:.4f})\n"
                gcode += f"(Arc start: X={x_arc_start:.4f}, Z={z_arc_start:.4f})\n"
                gcode += f"(Arc center: X={arc_center_x:.4f}, Z={arc_center_z:.4f})\n"
                gcode += f"(Arc end: X={arc_end_x:.4f}, Z={arc_end_z:.4f})\n"
                gcode += f"(Arc chord distance: {arc_distance:.4f}, max possible: {max_chord:.4f})\n"
                gcode += f"(Start radius check: {start_radius:.4f}, End radius check: {end_radius:.4f})\n"
                
                # Generate actual moves only if geometry is valid
                radius_tolerance = 1e-3
                geometry_valid = (arc_distance <= max_chord and 
                                abs(start_radius - corner_radius) < radius_tolerance and 
                                abs(end_radius - corner_radius) < radius_tolerance and 
                                arc_end_x <= x_safe_limit)
                
                gcode += f"(Geometry valid: {geometry_valid})\n"
                
                if geometry_valid:
                    if not math.isclose(z_start, z_arc_start, abs_tol=1e-6):
                        gcode += f"G1 X{x_output(x_arc_start):.4f} Z{z_arc_start:.4f} F{feed:.4f}\n"
                    gcode += f"G2 X{x_output(arc_end_x):.4f} Z{arc_end_z:.4f} R{expected_radius:.4f}\n"
                    
                    # Cleanup
                    if is_finish_pass:
                        gcode = add_safe_move(gcode, x_finish, None, False, feed)
                    else:
                        x_cleanup_arc = arc_end_x + abs(cleanup_step)
                        gcode = add_safe_move(gcode, min(x_cleanup_arc, x_safe_limit), None, False, feed)
                else:
                    gcode += f"(Safety: Invalid arc geometry - using straight cut)\n"
                    gcode, _ = add_safe_interpolated_move(gcode, x_pos, z_start, x_end_pass, z_pass_end, feed)
        else:
            # No corner radius - handle taper or straight cut
            if taper_angle_deg != 0:
                # Use intelligent interpolation that respects boundaries
                gcode, was_truncated = add_safe_interpolated_move(gcode, x_pos, z_start, x_end_pass, z_pass_end, feed)
            else:
                gcode += f"G1 Z{z_pass_end:.4f}\n"
                gcode += f"G1 X{x_output(x_end_pass):.4f} F{feed:.4f}\n"

        # CRITICAL: Final cut move to x_start + clearance for complete face cutting
        x_final_cut = x_start + abs(xz_clearance_val)
        gcode += f"(Final cut move to X start + clearance for complete face)\n"
        gcode += f"G1 X{x_output(x_final_cut):.4f} F{feed:.4f}\n"

        # Smart retraction to safe position after each pass
        gcode += f"G0 Z{z_safe:.4f}\n"
        
        # Continue with existing retraction logic...
        if i < len(x_positions) - 1:
            next_x = x_positions[i + 1]
            x_safe_next = next_x + xz_clearance_val if direction == -1 else next_x - xz_clearance_val
            # Ensure next position respects safety boundaries
            if x_safe_next > x_safe_limit:
                gcode += f"(Safety: Next position limited to safe boundary)\n"
                x_safe_next = x_safe_limit
            gcode += f"G0 X{x_output(x_safe_next):.4f}\n"
        else:
            # Final pass - retract to ultimate safe position
            gcode += f"(Final retraction to safe boundary)\n"
            gcode += f"G0 X{x_output(x_safe_limit):.4f}\n"

    gcode += "M5 (Spindle stop)\n"
    gcode += "M9 (Coolant off)\n"
    gcode += "M30 (End of program)\n"
    return gcode