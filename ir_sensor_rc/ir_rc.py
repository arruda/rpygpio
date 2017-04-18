#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

READING_LIMIT = 940  #could even do some calibration
READING_LIMIT_CM = 32

# 'ignore' noise
SIGMA = READING_LIMIT / READING_LIMIT_CM


def check_inside_area(value, max_value, min_value):
    return min_value < value < max_value


def rc_to_cm(rc_value, rc_max, cm_max):
    conversion_rate = float(cm_max) / rc_max
    cm_value = rc_value * conversion_rate
    return cm_value


def rc_time_with_sigma(rc_pin, sigma):
    current_reading = rc_time(rc_pin)
    last_reading = current_reading
    distance = 0
    while distance < sigma:
        current_reading = rc_time(rc_pin)
        distance = abs(last_reading - current_reading)
        cm_value = rc_to_cm(last_reading, READING_LIMIT, READING_LIMIT_CM)
        print cm_value
        if check_inside_area(cm_value, 30, 20):
            print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
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
        rc_value = rc_time_with_sigma(rc_pin, SIGMA)
        cm_value = rc_to_cm(rc_value, READING_LIMIT, READING_LIMIT_CM)
        print cm_value


if __name__ == '__main__':
    # GPIO.cleanup()
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
