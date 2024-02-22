import subprocess

# Run an ADB command to get the device's display metrics
adb_command = "adb shell dumpsys display"
output = subprocess.check_output(adb_command, shell=True, universal_newlines=True)

# Search for lines containing display density information
density_line = None

for line in output.split('\n'):
    if 'Display DPI:' in line:
        density_line = line
        break

if density_line is not None:
    # Parse the density value
    density_dpi = int(density_line.split(' ')[-1])
    print(f"Display Density (DPI): {density_dpi}")
else:
    print("Display density information not found in the output.")
