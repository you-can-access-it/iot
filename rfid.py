# sudo apt-get update
# sudo apt-get upgrade
# sudo raspi-config (interface >serial port >disable powershell log in >enable hardware interface >exit)
# reboot
# pip3 install pyserial

# (Board TX) Physical PIN 10    GPIO 15
# (Board VCC) Physical PIN 2    GPIO 3
# (Board GND) Physical PIN 6    GPIO 6

import serial

ser = serial.Serial('/dev/serial0', 9600, timeout=1)

print("Scan your card.....")

while True:
    data = ser.read(12)
    if data:
        print(data.decode('utf-8').strip())

#400034E6E97B
