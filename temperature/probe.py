# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple demo of the MAX31865 thermocouple amplifier.
# Will print the temperature every second.
#import time
import board
import digitalio
import adafruit_max31865


class tempProbe():
    def __init__(self):
        self._spi = board.SPI()
        self._cs = digitalio.DigitalInOut(board.D5)
        self._sensor = adafruit_max31865.MAX31865(self._spi, self._cs)
    
    def getTemp(self):
        return self._sensor.temperature

# Main loop to print the temperature every second.
#while True:
#    # Read temperature.
#    temp = sensor.temperature
#    # Print the value.
#    print("Temperature: {0:0.3f}C".format(temp))
#    # Delay for a second.
#    time.sleep(1.0)
