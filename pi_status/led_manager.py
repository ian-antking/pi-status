import unicornhat as uh
from time import sleep

class LedManager:
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


  def update_light(self, color, mode):
    action = getattr(self, mode)
    action(color)