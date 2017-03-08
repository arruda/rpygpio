#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

LED = 12


def emissor():
        print "on"
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1.5)
        print "off"
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1.5)


def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.cleanup()
    GPIO.setup(LED, GPIO.OUT)
    GPIO.output(LED, GPIO.HIGH)
    try:
        while True:
            emissor()
    except:
        GPIO.cleanup()


if __name__ == '__main__':
    main()
