import ctypes

# Constants for display settings
DM_PELSWIDTH = 0x80000
DM_PELSHEIGHT = 0x100000
DM_DISPLAYFREQUENCY = 0x400000

# Change these values to your desired width, height, and refresh rate
width, height = 1920, 1080
refresh_rate = 60

# Get the primary display device
device = ctypes.windll.user32.EnumDisplayDevicesW(0, 0, 0)

# Set display settings
settings = ctypes.c_uint32()
ctypes.windll.user32.EnumDisplaySettingsW(device, 0, ctypes.byref(settings))
settings.dmFields = DM_PELSWIDTH | DM_PELSHEIGHT | DM_DISPLAYFREQUENCY
settings.dmPelsWidth = width
settings.dmPelsHeight = height
settings.dmDisplayFrequency = refresh_rate

# Apply the new settings
ctypes.windll.user32.ChangeDisplaySettingsW(ctypes.byref(settings), 0)
