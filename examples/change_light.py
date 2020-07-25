import paho.mqtt.client as mqtt
from argparse import ArgumentParser
import json

parser = ArgumentParser()
parser.add_argument("--broker", "-b", type=str, required=True, help="address of mqtt broker")
parser.add_argument('--topic', '-t', type=str, required=True, help="mqtt topic to publish to")
parser.add_argument('--color', '-c', type=str, help="tuple containing rgb values, eg: '(255, 255, 255)'")
parser.add_argument('--mode', '-m', type=str, help="mode to switch the lamp to, eg: blink, solid, rainbow")
args = parser.parse_args()

message = {}
if args.color: message["color"] = args.color
if args.mode: message["mode"] = args.mode

message_json = json.dumps(message)

client = mqtt.Client("python_script_runner")
client.connect(args.broker)
client.loop_start()
client.publish(args.topic, message_json)
client.loop_stop()