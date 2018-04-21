import morse_talk as mtalk
import RPi.GPIO as GPIO
import time

outpin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(outpin, GPIO.OUT)

class OutputMorse:
    def __init__(self, outpin, delay_unit=0.3):
        self.outpin = outpin
        self.delay_unit = delay_unit

    def send(self, data, morse=False, threaded=False):
        if not morse:
            data = mtalk.encode(data)
        self._out(data)

    def _out(self, text):
        for code in text:
            if code in ('-', '.'):
                _outcode(code)
            else:
                time.sleep(delay_unit*2)

    def _outcode(self, code):
        GPIO.output(outpin, GPIO.HIGH)

        if code == '.':
            time.sleep(delay_unit)
        elif code == '-':
            time.sleep(delay_unit*3)

        GPIO.output(outpin, GPIO.LOW)
        time.sleep(delay_unit)

