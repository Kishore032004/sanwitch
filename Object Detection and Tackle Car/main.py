import time
from machine import Pin

while True:
    if Pin(4, Pin.IN).value() == 1:
        time.sleep_ms(1000)
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
        Pin(26, Pin.OUT).value(1)
        Pin(27, Pin.OUT).value(0)
    if Pin(4, Pin.IN).value() != 1:
        time.sleep_ms(1000)
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
        Pin(26, Pin.OUT).value(1)
        Pin(27, Pin.OUT).value(0)