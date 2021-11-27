import pygame
import time
import random
from Tkinter import *

import WFuncs2 as WF
import myGPIO
import Dials

####################
#Variables for test:
def GetPause():
    return False

RoundTime = 4
RestTime = 20
MaxRounds = 2
Diff = 0
Talks = False # hard set, it's a bit borked at the moment
####################

pygame.mixer.init()

StartList, EndList, TimingList, AdviceList, ClipList = WF.SampleLists()

while True:
    myGPIO.Stop()#Light "Ready" LED
    myGPIO.WaitGo() #wait for "Go" button to be depressed

    Drst, Drnd, Dnum, Ddif = Dials.ShowDials()

    RoundTimes = [10, 120, 180, 240]
    RestTimes = [10, 60, 60, 60]
    NumList = [1,2,3,4]
    DiffList = [-2,0,2]

    RoundTime = RoundTimes[Drnd]
    RestTime = RestTimes[Drst]
    MaxRounds = NumList[Dnum]
    Diff = DiffList[Ddif]

    print "RoundTime", RoundTime
    print "RestTime", RestTime
    print "MaxRounds", MaxRounds
    print "Diff", Diff

    Workout = True
    Timer = 0
    RoundNumber = 0
    while Workout:
        Round = True
        Timer = 0
        RoundNumber += 1
        while Round:
            while GetPause():
                time.sleep(1)
            Sample = random.choice(ClipList)
            print Sample
            WF.PlayClip(Sample)
            time.sleep(Diff)
            Timer += Sample[1] + Diff
            if Timer > RoundTime:
                Round = False
                EndSample = random.choice(EndList)
                print EndSample
                WF.PlayClip(EndSample)

        print RoundNumber, MaxRounds        
        if RoundNumber >= MaxRounds:
            Workout = False
            break

        if Workout: #if the workout is not finished. we need a rest!
            StartSample = random.choice(StartList)
            time.sleep(2)
            RestLeft = RestTime-StartSample[1]
            if Talks:
                ThisRest = []
                for Clip in AdviceList:
                    if Clip[1] < RestLeft:
                        RestLeft -= Clip[1]+5
                        ThisRest.append(Clip)
                for Sample in ThisRest:
                    print Sample
                    WF.PlayClip(Sample)
                    while GetPause():
                        time.sleep(1)
            else:
                while RestLeft > 0:
                    time.sleep(1)
                    RestLeft -= 1
                    while GetPause():
                        time.sleep(1)
            print StartSample
            WF.PlayClip(StartSample)

    myGPIO.Stop()
    
