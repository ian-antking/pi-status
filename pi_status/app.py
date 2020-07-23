import json
from time import sleep

class App():
  def __init__(self):
    self.color = (0,0,0)
  
  def on_message(self, client, user_date, message):
    payload = str(message.payload.decode("utf-8"))
    data = json.loads(payload)
    color = eval(data["color"])
    self.color = color

  def update(self):
    print(self.color)
    sleep(1)
