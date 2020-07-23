import unicornhat as uh

class LedManager:
  def __init__(self):
    uh.set_layout(uh.PHAT)
    uh.brightness(0.5)

  def update_light(self, color):
    for x in range(8):
      for y in range(4):
        uh.set_pixel(x, y, *color)

  def show_light(self):
    uh.show()