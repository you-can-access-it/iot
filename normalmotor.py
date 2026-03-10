import RPi.GPIO as GPIO
import time

# Your pins
# EA to BB+
# VCC to BB+
# pi pin 2 to BB+
# gnd to BB- /PI pin 6 (either direct ot througn breadboard)
MOTOR_PIN1 = 17  # Clockwise ; pi pin 11 to A1
MOTOR_PIN2 = 27  # Anti-clockwise; pi pin 13 to A2

# Setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTOR_PIN1, GPIO.OUT)
GPIO.setup(MOTOR_PIN2, GPIO.OUT)

# Initial stop
GPIO.output(MOTOR_PIN1, GPIO.LOW)
GPIO.output(MOTOR_PIN2, GPIO.LOW)


def clockwise(duration=2):
    print(">>> CLOCKWISE")
    GPIO.output(MOTOR_PIN1, GPIO.HIGH)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(duration)


def anticlockwise(duration=2):
    print(">>> ANTICLOCKWISE")
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.HIGH)
    time.sleep(duration)


def stop(duration=1):
    print(">>> STOP")
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    time.sleep(duration)


# Demo sequence
try:
    print("DC motor Demo starting....")

    for i in range(3):
        clockwise(1.5)
        stop(0.5)
        anticlockwise(1.5)
        stop(1)

    print("Demo complete")

except KeyboardInterrupt:
    print("\nStopped by user")

finally:
    GPIO.output(MOTOR_PIN1, GPIO.LOW)
    GPIO.output(MOTOR_PIN2, GPIO.LOW)
    GPIO.cleanup()
    print("GPIO cleaned up")