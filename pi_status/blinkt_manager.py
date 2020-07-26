from blinkt import set_brightness, set_pixel, show
from time import sleep, time
import colorsys

class BlinktManager:
  def __init__(self):
    set_brightness(0.1)

  def set_light(self, color):
    for x in range(8):
      set_pixel(x, *color)
    show()

  def solid(self, color):
    self.set_light(color)
    show()

  def off(self, _):
    off = (0, 0, 0)
    self.set_light(off)

  def blink(self, color):
    self.off(color)
    sleep(1)
    self.set_light(color)
    sleep(1)

  def rainbow(self, _):
    spacing = 360.0 / 16.0
    hue = int(time() * 100) % 360
    for x in range(8):
        offset = x * spacing
        h = ((hue + offset) % 360) / 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        set_pixel(x, r, g, b)
    show()
    sleep(0.001)


  def alert(self, color):
    off = (0, 0, 0)
    for x in range(8):
      pixelColor = color if (x % 2) == 0 else off
      set_pixel(x, *pixelColor)
    show()

  def update_light(self, color, mode):
    action = getattr(self, mode, self.solid)
    action(color)