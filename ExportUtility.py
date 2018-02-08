import os
import platform
import re
import subprocess
import sys
import time
import datetime
from bs4 import BeautifulSoup
from PIL import Image, PILLOW_VERSION, ImageDraw, ImageFont

VIEWPORT_SIZE = (1024, 5000)

def save_screenshot(browser, name=''):
    # Browser object provides GetUserData/SetUserData methods
    # for storing custom data associated with browser. The
    # "OnPaint.buffer_string" data is set in RenderHandler.OnPaint.

    buffer_string = browser.GetUserData("OnPaint.buffer_string")
    if not buffer_string:
        raise Exception("buffer_string is empty, OnPaint never called?")
    image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string,
                            "raw", "RGBA", 0, 1)
    width, height = image.size

    draw = ImageDraw.Draw(image)
    text = "[WebNinja] Time Stamp: " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    font = ImageFont.truetype('arial.ttf', 12)
    textwidth, textheight = draw.textsize(text, font)
    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text, font=font)

    image.save('C:/Users/lchan1/Desktop/wax/imdb/cache/' + name + '.png', "PNG")