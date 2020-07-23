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

if __name__ == '__main__':
  import paho.mqtt.client as mqtt
  import signal
  import sys
  from dotenv import load_dotenv
  from pathlib import Path
  import os

  env_path = Path('.') / '.env'
  load_dotenv(dotenv_path=env_path)

  app = App()

  client = mqtt.Client('pi-status-test')
  client.on_message = app.on_message

  client.connect(os.getenv("MQTT_BROKER"))
  client.subscribe(os.getenv("TOPIC"))

  client.loop_start()

  while True:
    try:
      app.update()
    except KeyboardInterrupt:
      print("keyboard interrupt:")
      print("stopping loop")
      client.loop_stop()
      print("exiting")
      sys.exit()
    except Exception as e:
      print(e)
      client.loop_stop()
      sys.exit()