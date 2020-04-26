
class App():
  def __init__(self, blinkt_manager):
    self.blinkt = blinkt_manager
    self.blinkt.set_brightness(0.1)
    self.clear()

  def clear(self):
    self.blinkt.clear()

  def busy(self):
    self.clear()
    for i in range(8):
      self.blinkt.set_pixel(i, 255, 0, 0)
      self.blinkt.show()
    


if __name__ == '__main__':
  import blinkt
  import buttonshim
  import signal

  app = App(blinkt)

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, presses):
    app.busy()

  signal.pause()

