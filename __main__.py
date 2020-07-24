import paho.mqtt.client as mqtt
import signal
import sys
from pi_status import App
from dotenv import load_dotenv
from getopt import getopt
import os

load_dotenv()

argv = sys.argv[1:]
opts, args = getopt(argv, "h:", ["hat"])

hat = None

try:
  for opt, arg in opts:
      if opt in ("-h", "--hat"):
        hat = arg

  if not hat:
    raise Exception("--hat option required") 

  if hat == "unicorn":
    from pi_status import UnicornManager
    led_manager = UnicornManager()
  else:
    raise Exception("--hat option must be unicorn") 
except Exception as e:
    print(e)
    sys.exit()

app = App(led_manager)

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