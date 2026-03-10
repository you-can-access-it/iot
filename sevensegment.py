#pip3 install raspberrypi-tm1637
# gnd = pi pin 6
# vcc = pi pin 1/2
# clk = pi pin 40
# dio = pi pin 38

from time import sleep
import tm1637
import time

Display = tm1637.TM1637(21, 20)  # Set the clock and data pins
Display.brightness(1)  # Set brightness to max (optional)

try:
    print("Starting simple clock (press CTRL + C to stop):")

    while True:
        current_time = time.strftime("%H%M")  # Get the current time as HHMM
        Display.show(current_time)  # Show the current time on the display
        sleep(1)

except KeyboardInterrupt:
    print("\nStopped by user")
