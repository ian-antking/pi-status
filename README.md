# Pi-Status

## Getting stated

Turn the pimoroni unicorn PHAT/HAT or Blinkt into an internet-of-things controlled lamp.

This app connects to a mosquitto broker and listens for messages containing `color` and `mode` properties. This project requires access to a mqtt broker. You can find instructions on how to do this [here](https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi) 

Clone this repo onto your raspberry pi: 

```bash
git clone https://github.com/ian-antking/pi-status.git
```

Install the dependencies: 
```bash
python -m pip install -r pi-status/requirements.txt
```

## Running the app

Paste the following script into your terminal. Make sure to replace the variables:
```bash
BROKER=<BROKER ADDRESS> #the address or ip of your mqtt broker
TOPIC=<CONSUMER TOPIC> #the topic that your lamp will subscribe to, eg: status/ian
NAME=<DEVICE NAME> #the name of your lamp, eg: ian-status-lamp
Light=<LIGHT HAT> #the type of light you have connected to your raspberry pi. Currently unicorn and blinkt are supported
python3 pi-status --light $LIGHT --broker $BROKER --topic $TOPIC --name $NAME
```

If you want the app to continue running after you close the terminal, add `nohup` to the start of the command:

```bash
nohup python3 pi-status --light $LIGHT --broker $BROKER --topic $TOPIC --name $NAME
```

The app will connect to the mqtt broker and listen for messages from the set topic. The LEDs will light up white when the app is ready to start recieving messages.

## Controlling the lamp

The lamp is controlled by messages published to the app's topic. [Mqtt Explorer](http://mqtt-explorer.com/) can be used to send messages to your mqtt broker.

Messages sent to the app's topic should be in JSON format, and can have either a `color` or `mode` property, or both:

This message will instruct the app to display white light
```json
{
  "color": "(255, 255, 255)",
  "mode": "solid"
}
```

This message will cause the app to display blinking red light
```json
{
  "color": "(255, 0, 0)",
  "mode": "blink"
}
```

Sending only one of `color` or `mode` will leave the other property unchanged:

This message will cause the light to blink, while leaving the color the same as what it was before
```json
{
  "mode": "blink"
}
```

The current option for `mode` are:
  - solid
  - blink
  - rainbow
  - off
  - alert
