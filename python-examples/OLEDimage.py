# OLEDimage.py

# Meant for use with the Raspberry Pi and an Adafruit monochrome OLED display!

# This program takes any image (recommended: landscape) and converts it into a black and white image which is then 
# displayed on one of Adafruit's monochrome OLED displays. 

# To run the code simply change directory to where it is saved and then type: sudo python OLEDimage.py <image name>
# For example: sudo python OLEDimage.py penguins900x600.jpg 
# The image penguins900x600.jpg is included in this repo as an example! Download any image that you want and simply change the
# image name!

# This program was created by The Raspberry Pi Guy

import gaugette.ssd1306
import time
import sys
from PIL import Image

RESET_PIN = 15
DC_PIN    = 16
width = 128
height = 32

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()
image = Image.open(sys.argv[1])
image_r = image.resize((width,height), Image.BICUBIC)
image_bw = image_r.convert("1")

for x in range(width):
        for y in range(height):
                led.draw_pixel(x,y,bool(int(image_bw.getpixel((x,y)))))

led.display()
