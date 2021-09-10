#Alert For Class

#Imports
from pync import Notifier
from datetime import datetime
import os
#import schedule

class classObject:
    
    def __init__(self, subject, time, day, place):
        self.subject = subject
        self.time = time
        self.day = day
        self.place = place

        
#COSC Courses 
COSC222_L05 = classObject("COSC 222 Lab", "16:00", 0, "Online")
COSC222_L1 = classObject("COSC 222 Lecture", "15:30", 2, "Online")
COSC222_L2 = classObject("COSC 222 Lecture", "15:30", 4, "Online")

#MATH Courses
MATH100_L1 = classObject("MATH 100 Lecture", "11:00", 1, "FIP - 204")
MATH100_L2 = classObject("MATH 100 Lecture", "11:00", 3, "FIP - 204")
MATH100_L27 = classObject("MATH 100 Lab", "09:00", 3, "Online")

#HIST Courses
HIST151_L1 = classObject("HIST 151 Lecture", "12:30", 0, "ART - 214")
HIST151_L2 = classObject("HIST 151 Lecture", "12:30", 2, "ART - 214")

#SPAN Courses
SPAN101_L1 = classObject("SPAN 101 Lecture", "9:00", 0, "Online")
SPAN101_L2 = classObject("SPAN 101 Lecture", "9:00", 2, "Online")
SPAN101_L3 = classObject("SPAN 101 Lecture", "9:00", 4, "Online")

#Array Of Type classObject To Hold All Class Slots
classArray = [COSC222_L05, COSC222_L1, COSC222_L2, MATH100_L1, MATH100_L2, MATH100_L27, HIST151_L1, HIST151_L2, SPAN101_L1, SPAN101_L2, SPAN101_L3]

#Time Obeject
time = datetime.now().time().strftime("%H:%M")
day = datetime.now().weekday()

#Print Out Class Slot Blocks
def getClassSlot(classArray):
    for n in classArray:
        print(n.subject)
        print(n.time)
        print(n.day)
        print(n.place)
        print()

#Notify System
def notify(text):
    Notifier.notify(text, open="https://derkaiser28.github.io/")
    #Notifier.notify(text)

#Script
notify("COSC 222")
        

