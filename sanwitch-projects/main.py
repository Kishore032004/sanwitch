from machine import Pin, PWM

Pin(2, Pin.OUT).value(1)
PWM(Pin(2), freq=1000, duty=512)
_buzz = PWM(Pin(15), freq=2000, duty=512)
time.sleep_ms(200)
_buzz.deinit()