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
    print("waiting for messages")
    self.color = (168, 168, 168)
    self.mode = "solid"
    self.update()

  def error(self):
    self.color = (168, 0, 0)
    self.mode = "error"
    self.update()

  def update(self):
    self.led_manager.update_light(self.color, self.mode)
