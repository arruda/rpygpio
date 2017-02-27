#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

import RPi.GPIO as GPIO

LED = 22

GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, GPIO.HIGH)

try:
    while True:
        print "acende"
        GPIO.output(LED, GPIO.HIGH)
        time.sleep(1.5)
        print "apage"
        GPIO.output(LED, GPIO.LOW)
        time.sleep(1.5)
except:
    GPIO.cleanup()

