#!/usr/bin/env python
# -*- coding: utf-8 -*-


import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)


def main(rc_pin):
    GPIO.setup(rc_pin, GPIO.IN)
    print "starting"
    while True:
        if GPIO.input(rc_pin) == GPIO.HIGH:
            print ">>>>>>>>>>>>>"
        else:
            print ""


if __name__ == '__main__':
    try:
        main(18)
    except Exception as e:
        print e.message
        GPIO.cleanup()

