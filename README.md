# morseplay

[![PyPi](https://img.shields.io/pypi/v/morseplay.svg)](https://pypi.org/project/morseplay/)
[![Build Status](https://travis-ci.org/ritiek/morseplay.svg?branch=master)](https://travis-ci.org/ritiek/morseplay)

morseplay is a python library to send and receive morse codes on Raspberry Pi.

## Installation & Usage

```
$ pip install morseplay
```

or if you like to live on the bleeding edge:

```
$ python setup.py install
```

Check out these examples to learn how to use morseplay:

```python
>>> import morseplay
# Let's try sending morse signals from an LED
>>> LED = morseplay.OutputMorse(outpin=17, setmode=GPIO.BCM, delay_unit=0.3)
# This will signal "hello" in morse from LED attached to pin 17
>>> LED.send("hello")
# You can also run the signal in background by returning a Thread instance
>>> signal = LED.send("hello", threaded=True)
>>> signal.start()
# Output custom morse code
>>> LED.send("-.--   ---", morse=True)
# Note that letters are separated by 3 spaces and words are separated
# by 7 spaces
```

## Contributing

Bug reports, feature requests and even documentation improvements are most
welcome!

## License

[![License](https://img.shields.io/github/license/ritiek/morseplay.svg)](https://github.com/ritiek/morseplay/blob/master/LICENSE)
