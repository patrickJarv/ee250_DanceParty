import sys
import paho.mqtt.client as mqtt
import time
import json
import random
import multiprocessing

sys.path.append('Software/Python/')
sys.path.append('Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

            
def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))

    client.subscribe("raspberrypi/led")
    client.message_callback_add("raspberrypi/led", led_callback)

    client.subscribe("raspberrypi/lcd")
    client.message_callback_add("raspberrypi/lcd", lcd_callback)

def led_callback(client, userdata, message):
    #Process X which controls the LED strobing
    global x
    cut1 = False
    #if another song is playing, stop the strobing
    if(x.is_alive()):
        x.terminate()
    call = str(message.payload, "utf-8")
    data = json.loads(call)
    #run new process with new tempo
    x = multiprocessing.Process(target=strobe, args=(data,))
    x.start()

def lcd_callback(client, userdata, message):
    #Process Y controls the LCD printing names
    global y
    #if another song is playing, stop scrolling the LCD
    if(y.is_alive()):
        y.terminate()
    red = random.randint(50, 255)
    green = random.randint(50, 255)
    blue = random.randint(50, 255)
    setRGB(red, green, blue)
    call = str(message.payload, "utf-8")
    #Start new process with new names
    y = multiprocessing.Process(target=scroll, args=(call,))
    y.start()

def strobe(data):
    global y
    #process the tempo so that the LED knows when to flicker
    temp = (data[0]['tempo'])
    length = (data[0]['duration_ms'])
    secBeat = 6000.0000 / temp
    timer = 0
    pulse = secBeat
    stop = 0
    while (timer < length/10):
        if(timer>pulse):
            stop = 0
            pulse = pulse + secBeat
            grovepi.digitalWrite(4, 1)
        if stop == 20:
            grovepi.digitalWrite(4, 0)
        stop = stop + 1
        timer = timer + 1
        time.sleep(0.008)
    #if the song is over, then clear LCD
    y.terminate()
    setRGB(0, 128, 64)
    setText("")



def scroll(call):
    #Scroll the LCD with the song's name
    index = 0
    index2 = call.find("#%#")
    artist = call[0:index2].upper() + "                "
    artist = artist[0:16]
    song = "                " + call[index2+3:].upper() + "                "
    while True:
        try:
            scrollText = song[index:index+16]
            setText_norefresh(artist + scrollText)
            time.sleep(0.5)
            index = index + 1
            if(len(song) - 15 == index):
                index = 0
        except IOError as ioe:
            if str(ioe) == '121':
                time.sleep(0.25)


#Default message callback. Never Used.
def on_message(client, userdata, msg):
    print("on_message: " + msg.topic + " " + str(msg.payload, "utf-8"))

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message = on_message
    client.on_connect = on_connect
    client.connect(host="eclipse.usc.edu", port=11000, keepalive=60)
    x = multiprocessing.Process()
    y = multiprocessing.Process()
    setRGB(0, 128, 64)
    setText("")
    
    client.loop_start()

    while True:
        time.sleep(1)
