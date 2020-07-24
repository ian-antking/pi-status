import paho.mqtt.client as mqtt
import sys
from pi_status import App, UnicornManager, MockManager
from argparse import ArgumentParser
import os


led_managers = {
  "unicorn-phat": UnicornManager,
  "mock": MockManager
}

choices = list(led_managers.keys())
parser = ArgumentParser()
parser.add_argument("--light", "-l", type=str, required=True, choices=choices, help="type of hat")
parser.add_argument("--broker", "-b", type=str, required=True, help="address of mqtt broker")
parser.add_argument('--name', '-n', type=str, required=True, help="name of device")
parser.add_argument('--topic', '-t', type=str, required=True, help="mqtt topic to subscribe to")
args = parser.parse_args()

app = App(led_managers[args.light]())

client = mqtt.Client(args.name)
client.on_message = app.on_message

client.connect(args.broker)
client.subscribe(args.topic)

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