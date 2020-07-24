import paho.mqtt.client as mqtt
import signal
import sys
from pi_status import App, UnicornManager, MockManager
from dotenv import load_dotenv
from argparse import ArgumentParser
import os

load_dotenv()

choices = ["unicorn-phat", "mock"]
parser = ArgumentParser()
parser.add_argument("--type", "-t", required=True, choices=choices, help="type of hat")
args = parser.parse_args()

led_managers = {
  "unicorn-phat": UnicornManager,
  "mock": MockManager
}

app = App(led_managers[args.type]())

client = mqtt.Client("DEVICE_NAME")
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