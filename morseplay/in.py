import time
import RPi.GPIO as GPIO
from math import log10, floor

def round_sig(x, sig=1):
    return round(x, sig-int(floor(log10(abs(x))))-1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

GPIO.add_event_detect(23, GPIO.FALLING)
times = []

while not GPIO.event_detected(23):
    time.sleep(0.05)

while True:
    start = time.clock()
    while True:
        time.sleep(0.05)
        if not GPIO.event_detected(23):
            active = time.clock() - start
            print("active - ", round_sig(active))
            break

    start = time.clock()
    while True:
        time.sleep(0.05)
        if GPIO.event_detected(23):
            pause = time.clock() - start
            print("pause  - ", round_sig(pause))
            break

    times.append((round(active*1000, 1), round(pause*1000, 1)))
