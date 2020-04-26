
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
    self.blinkt.set_all(0, 0, 0)
    self.blinkt.show()

  def busy(self):
    self.blinkt.set_all(255, 0, 0)
    self.blinkt.show()
  
  def working(self):
    self.blinkt.set_all(255, 191, 0)
    self.blinkt.show()

  def available(self):
    self.blinkt.set_all(0, 255, 0)
    self.blinkt.show()

  def update_leds(self):
    self.blinkt.show()
    

if __name__ == '__main__':
  import blinkt
  import buttonshim

  app = App(blinkt)

  @buttonshim.on_press(buttonshim.BUTTON_A)
  def button_a(button, presses):
    app.clear()

  @buttonshim.on_press(buttonshim.BUTTON_B)
  def button_b(button, presses):
    app.busy()

  @buttonshim.on_press(buttonshim.BUTTON_C)
  def button_c(button, presses):
    app.working()

  @buttonshim.on_press(buttonshim.BUTTON_D)
  def button_d(button, presses):
    app.available()

  while True:
    app.update_leds()

