import unicornhat as uh

class LedManager:
  def __init__(self):
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)

  def set_light(self, color):
    for x in range(8):
      for y in range(4):
        uh.set_pixel(x, y, *color)

  def update_light(self, color):
    self.set_light(color)
    uh.show()