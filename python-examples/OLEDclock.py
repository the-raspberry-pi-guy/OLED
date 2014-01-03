# OLEDclock.py

# This program interfaces with one of Adafruit's OLED displays and a Raspberry Pi (over SPI). It displays the current 
# date (Day, Month, Year) and then scrolls to the current time. The program waits for 2 seconds between scrolls.

# Example code from the py-gaugette library... Commented by The Raspberry Pi Guy

# Imports the necessary modules
import gaugette.ssd1306
import time
import sys

# Sets up our pins again
RESET_PIN = 15
DC_PIN    = 16


led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()

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
