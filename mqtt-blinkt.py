#!/usr/bin/env python3

from sys import exit

import paho.mqtt.client as mqtt
import blinkt
from colour import Color
import demjson

from config import *


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe(mqtt_topic + '/#')

state = [(0,0,0) for i in range(blinkt.NUM_PIXELS)]

def on_message(client, userdata, msg):
    global state

    try:
        topic = msg.topic.split('/')[-1]

        if topic == "clear":
            state = [Color() for i in range(blinkt.NUM_PIXELS)]
            blinkt.clear()
            blinkt.show()
            return

        data = demjson.decode(msg.payload.decode())

        if topic == "set":
            pixelmask = data['mask']
            del data['mask']
            col = Color(**data)

            for x in range(blinkt.NUM_PIXELS):
                if pixelmask & (1<<x) != 0:
                    state[x] = col

    except ValueError:
        print("Malformed message: " + str(demjson.encode(msg)))
        return
    except Exception as e:
        print(e)
        return

    for x in range(blinkt.NUM_PIXELS):
        col = state[x]
        blinkt.set_pixel(x, int(col.red*255), int(col.green*255), int(col.blue*255))
    blinkt.show()


blinkt.set_clear_on_exit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

if mqtt_user is not None and mqtt_pass is not None:
    print("Using username: {un} and password: {pw}".format(un=mqtt_user, pw="*" * len(mqtt_pass)))
    client.username_pw_set(username=mqtt_user, password=mqtt_pass)

client.connect(mqtt_host, mqtt_port, 60)

client.loop_forever()
