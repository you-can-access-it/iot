import serial

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

print("Scan your card.....")

while True:
    data = ser.read(12)
    if data:
        print(data.decode('utf-8').strip())

#400034E6E97B