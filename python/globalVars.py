from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.core import lib

import subprocess

import libAdvDisplay

from luma.oled.device import sh1106
import RPi.GPIO as GPIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Load default font.
font = ImageFont.load_default()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = 128
height = 64
image = Image.new('1', (width, height))

draw = None

# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

GPIO.setwarnings(False)

serial = spi(device=0, port=0, bus_speed_hz = 8000000, transfer_size = 4096, gpio_DC = 24, gpio_RST = 25)

device = sh1106(serial, rotate=2) #sh1106


def get_ip():
    cmd = "hostname -I | cut -d\' \' -f1"
    return subprocess.check_output(cmd, shell=True)


def get_width():
    return width
