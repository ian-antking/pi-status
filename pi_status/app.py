import json
from time import sleep

class App:
  def __init__(self, led_manager):
    self.color = (0,0,0)
    self.led_manager = led_manager
  
  def on_message(self, client, user_date, message):
    payload = str(message.payload.decode("utf-8"))
    data = json.loads(payload)
    color = eval(data["color"])
    self.color = color
    self.led_manager.update_light(color)

  def update(self):
    self.led_manager.show_light() 
