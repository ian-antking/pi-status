
class App():
  def __init__(self, blinkt_manager):
    self.blinkt = blinkt_manager
    self.on = True
    self.status = 'idle'

    self.blinkt.set_brightness(0.1)
    self.clear()

  def toggle_on(self):
    print('Setting self.on to %s' % self.on)
    self.on = not self.on

  def clear(self):
    self.blinkt.clear()
    self.blinkt.show()

  def busy(self):
    self.clear()
    self.blinkt.set_all(255, 0, 0)

  def update_leds(self):
    if self.state.on:
      for i in range(8):
        self.blinkt.set_pixel(i, 255, 0, 0)
        self.blinkt.show()
      else:
        self.clear()

  
    


if __name__ == '__main__':
  import blinkt
  import buttonshim
  import signal

  app = App(blinkt)

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, presses):
    app.toggle_on()

  @buttonshim.on_press(buttonshim.BUTTON_B)
  def button_b(button, presses):
    app.busy()

  signal.pause()

