import pygame
import time
from random import choice
from Tkinter import *
from arrayinfo import *

def playclip(combo):
    #if pygame.mixer.get_busy() == 0:
    pygame.mixer.Sound(combo[0]+'.ogg').play()
    time.sleep(combo[1])
        
def wholeworkout(rounds, roundtime, resttime, talks, difficulty): #times in seconds!
    pygame.mixer.init()
    #print str(rounds)+", "+str(roundtime)+", "+str(resttime)+", "+str(talks)+", "+str(difficulty)
    roundnumber = 1
    playclip(["StartFinish/Countdown",8])
    return
    while roundnumber <= rounds:
        playround(roundtime, difficulty)
        if roundnumber != rounds:
            playrest(resttime, talks)
        else:
            print "is finish"
        roundnumber += 1

def playround(rotime, diff):
    timer = 0
    while timer < rotime:
        sample = choice(cliparray)
        playclip(sample)
        time.sleep(diff)
        timer += sample[1] + diff
        
    playclip(choice(endarray))

def playrest(retime, talks):
    sample = choice(startarray)
    time.sleep(2)
    restleft = retime-sample[1]
    if talks:
        thisrest = []
        for item in advicearray:
            if item[1] < restleft:
                thisrest.append(item)
        if len(thisrest) > 0:
            pygame.mixer.Sound(choice(thisrest)[0]+'.ogg').play()
    time.sleep(restleft)
    playclip(sample)
        

if __name__=="__main__":
    #wholeworkout(rounds(int), roundtime(secs), resttime(secs), talks(bool), difficulty(seconds))
    #wholeworkout(3, 15, 10, False, 0)
    pass
