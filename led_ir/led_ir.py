#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

LED = 12
RECEPTOR = 26


# Define function to measure charge time
def rc_analog(pin):
    counter = 0
    # Discharge capacitor
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    # Count loops until voltage across capacitor reads high on GPIO
    while GPIO.input(pin) == GPIO.LOW:
        counter = counter + 1
    return counter


# def emitter():
#         print "on"
#         GPIO.output(LED, GPIO.HIGH)
#         time.sleep(1.5)
#         print "off"
#         GPIO.output(LED, GPIO.LOW)
#         time.sleep(1.5)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)

    try:
        while True:
            print rc_analog(RECEPTOR)  # Measure timing using GPIO pin
    except:
        pass
    finally:
        print "exit"
        GPIO.cleanup()


if __name__ == '__main__':
    main()
