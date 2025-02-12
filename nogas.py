"""
This Raspberry Pi code was developed by newbiely.com
This Raspberry Pi code is made available for public use without any restriction
For comprehensive instructions and wiring diagrams, please visit:
https://newbiely.com/tutorials/raspberry-pi/raspberry-pi-gas-sensor
"""


import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import RPi.GPIO as GPIO
import time

# Set up the GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin for reading the DO output
DO_PIN = 15  # Replace with the actual GPIO pin number
GPIO.setup(DO_PIN, GPIO.IN)

# I2C Interface
i2c = busio.I2C(board.SCL, board.SDA)

# Create the ADS object and specify the gain
ads = ADS.ADS1115(i2c)
ads.gain = 4
chan = AnalogIn(ads, ADS.P0)

try:
    while True:
        # Read the state of the DO pin
        gas_present = GPIO.input(DO_PIN)

        # Determine if gas is present or not
        if gas_present == GPIO.LOW:
            gas_state = "Gas Present"
        else:
            gas_state = "No Gas"
            print(f"Voltage: {chan.voltage}V")
            time.sleep(1)

        # Print the gas state
        print(f"Gas State: {gas_state}")

        time.sleep(0.5)  # Wait for a short period before reading again

except KeyboardInterrupt:
    print("Gas detection stopped by user")

finally:
    # Clean up GPIO settings
    GPIO.cleanup()
