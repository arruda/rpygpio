#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO
import time

DEBUG = 1
GPIO.setmode(GPIO.BOARD)


def rc_time(rc_pin):
        reading = 0
        GPIO.setup(rc_pin, GPIO.OUT)
        GPIO.output(rc_pin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(rc_pin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(rc_pin) == GPIO.LOW):
                reading += 1
        return reading


def main(rc_pin):
    while True:
        print rc_time(rc_pin)     # Read RC timing using pin #18


if __name__ == '__main__':
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
