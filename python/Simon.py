######################################################################################
# Name: Norman Cook
# Date: 7/23/2019
# Description: A rectreation of the four colored game simon using a
#   Raspberry Pi and circuit elements.
######################################################################################
import RPi.GPIO as GPIO
from time import sleep
from random import randint
import pygame

# set to True to enable debugging output
DEBUG = False
score = 0
playspeed = 1
notespeed = 0.5

# initialize the pygame library
pygame.init()

# set the GPIO pin numbers
# the LEDs (from L to R)
leds = [6, 13, 19, 21]
# the switches from L to R)
switches = [20, 16, 12, 16]

# the sounds that map to each LED (from L to R)
sounds = [pygame.mixer.Sound("one.wav"),
          pygame.mixer.Sound("two.wav"),
          pygame.mixer.Sound("three.wav"),
          pygame.mixer.Sound("four.wav") ]

# use the broadcom pin mode
GPIO.setmode(GPIO.BCM)

# setup the output pins
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(leds, GPIO.OUT)

# this function turns the LEDs on
def all_on():
    for i in leds:
        GPIO.output(leds , True)

# this function turns the LEDs off
def all_off():
    for i in leds:
        GPIO.output(leds, False)

# this functions flashes the LEDs a few times when the player loses the game
def lose():
    for i in range(0, 4):
        all_on()
        sleep(0.5)
        all_off()
        sleep(0.5)

# display the score
def scoreboard(n):
    if (n == 0):
        print "You didn't even make it to a sequence!"
        return
    print "You made it to a sequence of {}!".format(n)

# the main part of the program
# initialize the Simon sequence
# each item in the sequence represents an LED (or switch), indexed at 0 thorugh 3
seq = []
# randomly add the first two items to the sequence
seq.append(randint(0,3))
seq.append(randint(0,3))

print "Welcome to Simon!"
print "Try to play the sequence back by pressing the switches."
print "Press Ctrl + C to ext..."

# we'll discuss this later, but this allows us to detect
# when Ctrl + C is pressed to that we can reset the GPIO pins
try:
    # keep going until the user pressses Ctrl+C
    while (True):

        # set the play speed and note speed based on the sequence
        if (score > 12):
            playspeed = 0.6
            notespeed = 0.15
        elif (score > 9):
            playspeed = 0.7
            notespeed = 0.25
        elif (score > 6):
            playspeed = 0.8
            notespeed = 0.3
        elif (score > 4):
            playspeed = 0.9
            notespeed = 0.4

        # randomly add one more item to the sequence
        seq.append(randint(0,3))
        if (DEBUG):
            # display the sequence to the console
            if (seq_len > 3):
                print
            print "seq={}".format(seq)

        # display the sequence using the LEDs
        for s in seq:
            # turn the appropriate LED on
            if (score < 15):
                GPIO.output(leds[s], True)
                
            # play its corresponding sound
            sounds[s].play()
            # wait and turn the LED off again
            sleep(playspeed)
            if (score < 15):
                GPIO.output(leds[s], False)
                
            sleep(notespeed)

        # wait for player input (via the switches)
        # initialize the count of switches pressed to 0
        switch_count = 0
        # keep accepting player input util the number of items in the sequence is reached
        while (switch_count < len(seq)):
            # initially note that no switch is pressed
            # this will help with switch debouncing
            pressed = False
            # so lo0ng as no switch is currently pressed...
            while (not pressed):
                # ...we can check the status of each switch
                for i in range(len(switches)):
                    # if one switch is pressed
                    while (GPIO.input(switches[i]) == True):
                        # note its indes
                        val = i
                        # note that a switch has now been pressed
                        # so that we don't detect any more switch presses
                        pressed = True
            if (DEBUG):
                # display the index of the switch pressed
                print val

            # light the matching LED
            GPIO.output(leds[val], True)
            # play is corresponding sound
            sounds[val].play()
            # wait and turn the LED off again
            sleep(1)
            GPIO.output(leds[val], False)
            sleep(0.25)

            # check to see if this LED is correct in the sequence
            if (val != seq[switch_count]):
                scoreboard(score)
                                
                # player is incorrect; invoke the lose function
                lose()
                
                # reset the GPIO pins
                GPIO.cleanup()
                # exit the game
                exit(0)
            # if the player has this item in the sequence
            # correct, increment the count
            switch_count += 1

        score += 1

# detect Ctrl+C
except KeyboardInterrupt:
    # reset the GPIO pins
    GPIO.cleanup()
    print "\nSionara!"
