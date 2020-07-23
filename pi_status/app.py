import json

class App:
  def __init__(self, led_manager):
    self.color = (168, 168, 168)
    self.mode = "solid"
    self.led_manager = led_manager
    self.update()
  
  def on_message(self, client, user_date, message):
    payload = str(message.payload.decode("utf-8"))
    data = json.loads(payload)
    self.color = eval(data["color"]) or self.color
    self.mode = data["mode"] or self.mode

  def update(self):
    self.led_manager.update_light(self.color, self.mode)
