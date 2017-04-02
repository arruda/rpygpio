#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO
import time

DEBUG = 1
GPIO.setmode(GPIO.BOARD)

READING_LIMIT = 6000  #could even do some calibration


def rc_time(rc_pin):
        reading = 0
        GPIO.setup(rc_pin, GPIO.OUT)
        GPIO.output(rc_pin, GPIO.LOW)
        time.sleep(0.01)

        GPIO.setup(rc_pin, GPIO.IN)
        while (GPIO.input(rc_pin) == GPIO.LOW) and (reading < READING_LIMIT):
                reading += 1
        return reading


def main(rc_pin):
    print "starting"
    while True:
        print rc_time(rc_pin)


if __name__ == '__main__':
    GPIO.cleanup()
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
