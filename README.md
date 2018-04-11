A simple Python script from Pimoroni's sample code for Blinkt -- a Raspberry Pi add-on with 8 RGB LEDs in a strip.

https://github.com/pimoroni/blinkt

I wrote this before realising it'd already been done more than once before, eg. the JS-based https://github.com/pinkkis/mqtt_blinkt

This script takes a configuration file for an MQTT host (see `config.py.dist` and customise) and subscribes to the topic given;  in particular, the sub-topics `/clear` and `/set`.

It passes the parameters for `/set` through `demjson` (ie. loose JSON) and passes the result to the `Color()` constructor for the Python `colour` module.  In addition, it takes a `mask` parameter from that result first and uses it as a bitmask for the LEDs.

So, send:
```
mosquitto_pub -h mqtt.home -t /actuator/blinkt1/set -m '{mask:255,red:1,blue:1,green:0}'
```
and you should see bright magenta.

This way, simple rules can be built in Node-RED and piped direct to a Raspberry Pi Zero W sitting in the corner of the room with a Blinkt plugged in; a very simple but powerful notification.

In time I may add fading, animation, etc.  Saying that, such a thing can be scripted in Node-RED and passed using MQTT, albeit less efficiently.
