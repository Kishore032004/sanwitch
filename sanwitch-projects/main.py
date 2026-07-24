from machine import Pin, PWM

Pin(2, Pin.OUT).value(1)
PWM(Pin(2), freq=1000, duty=512)