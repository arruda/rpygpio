# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)


def main(rc_pin):
    GPIO.setup(rc_pin, GPIO.OUT)
    while True:
        GPIO.output(rc_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(rc_pin, GPIO.LOW)
        time.sleep(0.5)


if __name__ == '__main__':
    print 'will start in 5 seconds.'
    time.sleep(5)
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
