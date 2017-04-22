#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

READING_LIMIT = 900


class PinController(object):
    def __init__(self, rc_pin, max_dist, min_dist, n_samples=5, n_samples_cal=500, rc_time_sleep=0.01):
        super(PinController).__init__()
        self.rc_pin = rc_pin
        self.n_samples = n_samples
        self.n_samples_cal = n_samples_cal
        self.rc_time_sleep = rc_time_sleep
        self.reading_max_limit = 0
        self.reading_min_limit = 0
        self.calibration()

    def calibration(self):
        for i in xrange(5):
            print "Starting MIN calibration in %d..." % i
            time.sleep(1)
        self.reading_min_limit = self.rc_with_samples(self.n_samples_cal)
        for i in xrange(5):
            print "Starting MAX calibration in %d..." % i
            time.sleep(1)
        self.reading_max_limit = self.rc_with_samples(self.n_samples_cal)

        print "Final results: min: %d/ max: %d" % (self.reading_min_limit, self.reading_max_limit)
        time.sleep(1)

    def rc_with_samples(self, n_samples):
        samples = []
        for i in xrange(n_samples):
            samples.append(self.rc_time())
        avg = sum(samples) / len(samples)
        return avg

    def rc_time(self):
            reading = 0
            GPIO.setup(self.rc_pin, GPIO.OUT)
            GPIO.output(self.rc_pin, GPIO.LOW)
            time.sleep(self.rc_time_sleep)

            GPIO.setup(self.rc_pin, GPIO.IN)
            while (GPIO.input(self.rc_pin) == GPIO.LOW) and (reading < READING_LIMIT):
                    reading += 1
            return reading

    def evaluate(self):
        reading = self.rc_with_samples(self.n_samples)
        return self.reading_min_limit > reading < self.reading_max_limit


def main(rc_pin):
    ctrl = PinController(rc_pin=rc_pin, max_dist=55, min_dist=0, n_samples=5, n_samples_cal=500, rc_time_sleep=0.01)
    print "starting"
    while True:
        evaluation = ctrl.evaluate()
        if evaluation:
            print ">>>>>>>>>>>>>"
        else:
            print ""


if __name__ == '__main__':
    try:
        main(18)
    except KeyboardInterrupt:
        GPIO.cleanup()
