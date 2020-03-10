###########################################################################################
# Name: Norman Cook
# Date: 06-28-2019
# Description: Continuously blink an LED at 0.5 s intervals and change the
#   interval to 0.1 s if a switch is closed using a Raspberry Pi.
################################################################################

# import necessary libraries
import RPi.GPIO as GPIO
from time import sleep

# set the button and led pin numbers
led = 17
button = 25

# setup the led and buttion with the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# blink the LED 
while (True):
    GPIO.output(led, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    sleep(0.5)
    while (GPIO.input(button) == GPIO.HIGH):
        GPIO.output(led, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        sleep(0.1)

