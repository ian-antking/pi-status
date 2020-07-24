import unicornhat as uh
from time import sleep, time
import colorsys

class UnicornManager:
  def __init__(self):
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)

  def set_light(self, color):
    for x in range(8):
      for y in range(4):
        uh.set_pixel(x, y, *color)

  def solid(self, color):
    self.set_light(color)
    uh.show()

  def blink(self, color):
    off = (0, 0, 0)
    self.set_light(off)
    uh.show()
    sleep(1)
    self.set_light(color)
    uh.show()
    sleep(1)

  def rainbow(self, _):
    spacing = 360.0 / 8.0
    hue = int(time() * 100) % 360
    for x in range(8):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        for y in range(4):
            uh.set_pixel(x, y, r, g, b)
    uh.show()
    sleep(0.005)

  def error(self, _):
    for x in range(8):
      for y in range(4):
        color = (255, 0, 0) if x % 2 == 0 and y % 2 == 2 else (255, 255, 255)
        uh.set_pixel(x, y, *color)

  def update_light(self, color, mode):
    action = getattr(self, mode, self.solid)
    action(color)