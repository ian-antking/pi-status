# Pi-Status

## Getting stated

Turn the pimorono unicorn pHAT into an internet-of-things controlled lamp.

This app connects to a mosquitto broker and listens for messages containing `color` and `mode` properties. This project requires access to a mqtt broker. You can find instructions on how to do this [here](https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi) 

Currently this project is only compatible with the unicorn pHAT. There are plans to add unicorn HAT and blinkt.

Clone this repo onto your raspberry pi: 

```bash
git clone https://github.com/ian-antking/pi-status.git
```

Install the dependencies: 
```bash
cd pi-status && python -m pip install -r requirements.txt
```

Run the app:
```bash
python3 pi-status --light unicorn-phat --broker <address of mqtt broker> --topic <mqtt topic to subscribe to> --name <name of device>
```

The app will connect to the mqtt broker and listen for messages from the set topic. The LEDs will light up white when the app is ready to start recieving messages.

Messages sent to that topic should be in JSON format, and can have either a `color` or `mode` property, or both:

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