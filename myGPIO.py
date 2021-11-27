#Controls Red and Green LEDs connected to GPIO
#Go = Green On (Red Off)
#Stop = Red On (Green Off)

import time

import RPi.GPIO as G
G.setwarnings(False)
G.setmode(G.BCM)
G.setup(04,G.OUT, initial=G.HIGH)
G.setup(25,G.OUT, initial=G.LOW)

def Go():
	G.output(25, G.HIGH)
	G.output(04, G.LOW)

def Stop():
	G.output(04, G.HIGH)
	G.output(25, G.LOW)

def FlashGo():
	G.output(25, G.HIGH)
	G.output(04, G.LOW)
	time.sleep(1)
	G.output(04, G.HIGH)
	time.sleep(1)

def FlashStop():
	G.output(04, G.HIGH)
	G.output(25, G.LOW)
	time.sleep(1)
	G.output(25, G.HIGH)
	time.sleep(1)

G.setup(24, G.OUT, initial=G.HIGH)
G.setup(23, G.IN)
def WaitGo():
        G.wait_for_edge(23, G.RISING)
        Go()
        return True

###Pause doesn't work at the moment. Replace physical switch :)
##G.setup(22, G.OUT, initial=G.HIGH)
##G.setup(27, G.IN)
##G.add_event_detect(27, G.RISING)
##def GetPause():
##        if (G.event_detected(27))&(G.input(27)):
##                G.remove_event_detect(27)
##                G.add_event_detect(27, G.FALLING)
##                while not G.event_detected(27):
##                        FlashGo()
##        G.remove_event_detect(27)
##        G.add_event_detect(27, G.RISING)
