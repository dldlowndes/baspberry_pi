import pygame
import time
from random import choice
from Tkinter import *
from arrayinfo import *

def playclip(combo):
    #if pygame.mixer.get_busy() == 0:
    pygame.mixer.Sound(combo[0]+'.ogg').play()
    time.sleep(combo[1])
        
def wholeworkout(rounds, roundtime, resttime, talks, difficulty):
    pygame.mixer.init()
    #print str(rounds)+", "+str(roundtime)+", "+str(resttime)+", "+str(talks)+", "+str(difficulty)
    roundnumber = 1
    playclip(["StartFinish/Countdown",8])
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
    if talks == 1:
        print talks
        thisrest = []
        for item in advicearray:
            if item[1] < restleft:
                thisrest.append(item)
        if len(thisrest) > 0:
            pygame.mixer.Sound(choice(thisrest)[0]+'.ogg').play()
    time.sleep(restleft)
    playclip(sample)
        
    
    
root = Tk()
titleframe = Frame(padx=5, pady=5, bd=1, relief=RIDGE)
titleframe.pack(fill=X)
w = Label(titleframe, text="Bas Rutten's Boxing Workout").pack()

roundsframe = Frame(padx=5, pady=5, bd=1, relief=RIDGE)
roundsframe.pack(fill=X)
rounds = [("One", 1),("Two", 2),("Three", 3),("Four", 4),("Five", 5)]
menurounds = IntVar()
menurounds.set(2)
roundslabel = Label(roundsframe, text="Number of Rounds:").pack(side=LEFT)
for title, roundsvalue in rounds:
    br = Radiobutton(roundsframe, text=title, variable=menurounds, value=roundsvalue).pack(side=LEFT)

roundtimesframe = Frame(padx=5, pady=5, bd=1, relief=RIDGE)
roundtimesframe.pack()
roundtimes = [("Test", 4),("30 Seconds", 30),("1 minute", 60),("90 seconds", 90),("2 minutes", 120),("3 minutes", 160)]
menuroundtime = IntVar()
menuroundtime.set(4)
roundtlabel = Label(roundtimesframe, text="Round Duration:").pack(side=LEFT)
for title, roundvalue in roundtimes:
    br = Radiobutton(roundtimesframe, text=title, variable=menuroundtime, value=roundvalue).pack(side=LEFT)

restframe = Frame(padx=5, pady=5, bd=1, relief=RIDGE)
restframe.pack(fill=X)
resttimes = [("Test", 15),("30 Seconds", 30),("1 Minute", 60)]
menuresttime = IntVar()
menuresttime.set(15)
resttlabel = Label(restframe, text="Rest Duration:").pack(side=LEFT)
for title, restvalue in resttimes:
    br = Radiobutton(restframe, text=title, variable=menuresttime, value=restvalue).pack(side=LEFT)
talk = IntVar()
talkbox = Checkbutton(restframe,text="Bas Talks in rests", variable=talk).pack()

difficultyframe = Frame(padx=5, pady=5, bd=1, relief=RIDGE)
difficultyframe.pack(fill=X)
diflabel = Label(difficultyframe, text="Difficulty Level:").pack(side=LEFT)
menudifficulty = IntVar()
menudifficulty.set(1)
difficulties = [("Easy",2),("Normal",1),("Hard",0)]
for title, difficultval in difficulties:
    bd = Radiobutton(difficultyframe, text=title, variable=menudifficulty, value=difficultval).pack(side=LEFT)

buttonframe = Frame(padx=5, pady=5, bd=1, relief=RIDGE)
buttonframe.pack(fill=X)
startbutton = Button(buttonframe, text="START", command=lambda:
                     wholeworkout(menurounds.get(),menuroundtime.get(),menuresttime.get(),talk.get(),menudifficulty.get())
                     ).pack(side=LEFT)
quitbutton = Button(buttonframe, text="QUIT", command=root.quit).pack(side=RIGHT)

root.mainloop()
