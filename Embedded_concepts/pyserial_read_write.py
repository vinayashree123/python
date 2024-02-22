import serial

# Define serial port settings
ser = serial.Serial(
    port='COM5',  # Adjust to your specific serial port
    baudrate=9600,        # Match the device's baud rate
    bytesize=8,
    parity='N',           # No parity
    stopbits=1,
    timeout=1             # Read timeout in seconds
)

# Send data to the device
ser.write(b'Hello, device!')

# Read data from the device
response = ser.readline()
print(response)

# Close the serial port when done
ser.close()
