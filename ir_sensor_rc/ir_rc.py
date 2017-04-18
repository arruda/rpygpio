#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

READING_LIMIT = 1200  #could even do some calibration

# 'ignore' noise
SIGMA = READING_LIMIT / 40


def rc_time_with_sigma(rc_pin, sigma):
    current_reading = rc_time(rc_pin)
    last_reading = current_reading
    distance = 0
    while distance < sigma:
        current_reading = rc_time(rc_pin)
        distance = abs(last_reading - current_reading)
    last_reading = current_reading
    return last_reading


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
        print rc_time_with_sigma(rc_pin, SIGMA)


if __name__ == '__main__':
    # GPIO.cleanup()
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
