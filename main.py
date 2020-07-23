import paho.mqtt.client as mqtt
import signal
import sys
from pi_status import App
from dotenv import load_dotenv
import os

load_dotenv()

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