# OLEDip.py

# Meant for use with the Raspberry Pi and an Adafruit monochrome OLED display!

# This program interfaces with the OLED display in order to print your current IP address to it! The program trys
# several methods in order to accquire an IP address. For example if you are using a WiFi dongle your IP will be 
# different to when you are using a Ethernet cable. This program tests for both and if it can not detect one prints:
# 'NO INTERNET!' to the display. This code is perfect to run on boot when you want to find your Pi's IP address for
# SSH or VNC!

# This was coded by The Raspberry Pi Guy!

import gaugette.ssd1306
import time
import sys
import socket
import fcntl
import struct
from time import sleep

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


RESET_PIN = 15
DC_PIN    = 16
TEXT = ''
count = 0

led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN)
led.begin()
led.clear_display()


try:
    TEXT = get_ip_address('wlan0') # WiFi address of WiFi adapter. NOT ETHERNET
except IOError:
    try:
        TEXT = get_ip_address('eth0') # WiFi address of Ethernet cable. NOT ADAPTER
    except IOError:
        TEXT = ('NO INTERNET!')


led.clear_display()
intro = 'Hello!'
ip = 'Your IP Address is:'
led.draw_text2(0,25,TEXT,1)
led.draw_text2(0,0,intro,2)
led.draw_text2(0,16, ip, 1)
led.display()
