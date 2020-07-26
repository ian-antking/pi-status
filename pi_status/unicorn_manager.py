import unicornhat as uh
from time import sleep, time
import colorsys

class UnicornManager:
  def __init__(self):
    uh.set_layout(uh.AUTO)
    uh.brightness(0.5)

  def set_light(self, color):
    for x in range(8):
      for y in range(4):
        uh.set_pixel(x, y, *color)
    uh.show()

  def solid(self, color):
    self.set_light(color)
    uh.show()

  def off(self, _):
    off = (0, 0, 0)
    self.set_light(off)

  def blink(self, color):
    self.off(color)
    sleep(1)
    self.set_light(color)
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

  def alert(self, color):
    off = (0, 0, 0)
    for x in range(8):
      for y in range(4):
        pixelColor = color if ((x % 2) == 0 and (y % 2) == 0) or ((x % 2) == 1 and (y % 2) == 1) else off
        uh.set_pixel(x, y, *pixelColor)
    uh.show()

  def update_light(self, color, mode):
    action = getattr(self, mode, self.solid)
    action(color)