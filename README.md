# Pi-Status

## Getting stated

Turn the pimorono unicorn pHAT into an internet-of-things controlled lamp.

This app connects to a mosquitto broker and listens for messages containing `color` and `mode` properties. This project requires access to a mqtt broker. You can find instructions on how to do this [here](https://appcodelabs.com/introduction-to-iot-build-an-mqtt-server-using-raspberry-pi) 

Currently this project is only compatible with the unicorn pHAT. There are plans to add unicorn HAT and blinkt.

Clone this repo onto your raspberry pi: 

```
git clone https://github.com/ian-antking/pi-status.git
```

Install the dependencies: 
```
cd pi-status && python -m pip install -r requirements.txt
```

Run the app:
```
python3 pi-status --light unicorn-phat --broker <address of mqtt broker> --topic <mqtt topic to subscribe to> --name <name of device>
```