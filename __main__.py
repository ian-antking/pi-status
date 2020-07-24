import paho.mqtt.client as mqtt
import sys
from pi_status import App, UnicornManager, MockManager
from argparse import ArgumentParser
from time import sleep


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

def on_connect(client, userdata, flags, rc):
  if not rc == 0:
    app.error()
    print('connection request returned with code %s' % rc)
  else:
    print('connection to broker established')
    client.subscribe(args.topic)
    app.ok()

def handle_exception(e):
  print(e)
  client.loop_stop()
  app.error()
  sleep(10)
  sys.exit(1)

client = mqtt.Client(args.name)
client.on_connect = on_connect
client.on_message = app.on_message
client.loop_start()

try:
  client.connect(args.broker)
except Exception as e:
  handle_exception(e)

while not app.connected:
  print('connecting...')
  sleep(1)

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
    handle_exception(e)