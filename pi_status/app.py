import json

class App:
  def __init__(self, led_manager):
    self.color = (0,  0, 168)
    self.mode = "blink"
    self.led_manager = led_manager
    self.connected = False
    self.update()
  
  def on_message(self, client, user_date, message):
    payload = str(message.payload.decode("utf-8"))
    data = json.loads(payload)
    self.color = eval(data.get("color")) if data.get("color") else self.color
    self.mode = data.get("mode") or self.mode
  
  def ok(self):
    self.connected = True
    self.led_manager.update_light((168, 168, 168), "solid")

  def error(self):
    self.led_manager.update_light((168, 0, 0), "blink")

  def update(self):
    self.led_manager.update_light(self.color, self.mode)
