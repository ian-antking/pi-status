# Pi-Status

## Getting stated

Turn the pimorono unicorn pHAT into an internet-of-things controlled lamp.

This app connects to a mosquitto broker and listens for messages containing `color` and `mode` properties.

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
python3 __main__.py
```