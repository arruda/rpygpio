# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
rc_pin = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(rc_pin, GPIO.OUT)


def main():
    while True:
        GPIO.output(rc_pin, GPIO.HIGHT)
        time.sleep(0.5)
        GPIO.output(rc_pin, GPIO.LOW)
        time.sleep(0.5)


if __name__ == '__main__':
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
