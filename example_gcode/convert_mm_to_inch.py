def convert_mm_to_inch(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    with open(output_file, 'w') as f:
        for line in lines:
            if line.startswith('G'):
                parts = line.split()
                new_parts = []
                for part in parts:
                    # Skip empty strings
                    if not part.strip():
                        continue
                    if any(axis in part for axis in ['X', 'Y', 'Z']):
                        axis = part[0]
                        try:
                            value = float(part[1:].strip())
                            inch_value = value / 25.4
                            new_parts.append(f"{axis}{inch_value:.4f}")
                        except ValueError:
                            new_parts.append(part)
                    else:
                        new_parts.append(part)
                f.write('  '.join(new_parts) + '\n')
            else:
                f.write(line)
    print(f"Conversion complete! Output file created: {output_file}")

# Run the conversion
input_file = "conversion_test.ngc"
output_file = "conversion_test_inch.ngc"
convert_mm_to_inch(input_file, output_file)
