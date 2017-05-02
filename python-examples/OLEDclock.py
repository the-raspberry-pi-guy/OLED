# OLEDclock.py

# This program interfaces with one of Adafruit's OLED displays and a Raspberry Pi (over SPI). It displays the current 
# date (Day, Month, Year) and then scrolls to the current time. The program waits for 2 seconds between scrolls.

# Example code from the py-gaugette library... Commented by The Raspberry Pi Guy

# Imports the necessary modules
import gaugette.ssd1306
import gaugette.platform
import gaugette.gpio
import time
import sys

# Define which GPIO pins the reset (RST) and DC signals on the OLED display are connected to on the
# Raspberry Pi. The defined pin numbers must use the WiringPi pin numbering scheme.
RESET_PIN = 15 # WiringPi pin 15 is GPIO14.
DC_PIN = 16 # WiringPi pin 16 is GPIO15.

spi_bus = 0
spi_device = 0
gpio = gaugette.gpio.GPIO()
spi = gaugette.spi.SPI(spi_bus, spi_device)

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
led = gaugette.ssd1306.SSD1306(gpio, spi, reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=32, cols=128) # Change rows & cols values depending on your display dimensions.
led.begin()
led.clear_display()
led.display()
led.invert_display()
time.sleep(0.5)
led.normal_display()
time.sleep(0.5)

offset = 0 # flips between 0 and 32 for double buffering

# While loop has bulk of the code in it!

while True:

    # write the current time to the display on every other cycle
    if offset == 0:
        text = time.strftime("%A")
        led.draw_text2(0,0,text,2)
        text = time.strftime("%e %b %Y")
        led.draw_text2(0,16,text,2)
        text = time.strftime("%X")
        led.draw_text2(0,32+4,text,3)
        led.display()
        time.sleep(1)
    else:
        time.sleep(1)

    # vertically scroll to switch between buffers
    for i in range(0,32):
        offset = (offset + 1) % 64
        led.command(led.SET_START_LINE | offset)
        time.sleep(0.01)
