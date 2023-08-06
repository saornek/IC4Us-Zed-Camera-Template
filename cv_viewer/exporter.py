"""
Author: saornek
Purpose: Import detect object values from tracking viewer and export to RPi
Notes: The codes written under example are only to see how the code works. They are not apart of the template. You can edit however you like.
"""

# Import Libraries
import serial
import math

# Connect to RPi via Serial
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=3) #comment for test purposes

def values(label, rawVelocity): # example data

    # Example:
    print(label, calVelocity[rawVelocity])

    sendSentence = "I see a " + str(label) + " in my way"  " at a speed of " + str(velocity)
    ser.write(str.encode(sendSentence + "\n")) #comment for test purposes
    #print(sendSentence) #uncomment for test purposes
    
# Example - Process Velocity Value
def calVelocity():
    vel = (int(rawVel[0])^2 + int(rawVel[1])^2 + int(rawVel[2])^2)
    if vel <= 0:
        return 0
    else:
        return round(math.sqrt(vel), 1)