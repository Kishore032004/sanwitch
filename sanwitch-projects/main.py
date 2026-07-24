from machine import Pin, PWM

while True:
    if Pin(24, Pin.IN).value() == 1:
        _buzz = PWM(Pin(15), freq=2000, duty=512)
        time.sleep_ms(200)
        _buzz.deinit()
    if Pin(24, Pin.IN).value() != 1:
        _buzz = PWM(Pin(15), freq=0, duty=512)
        time.sleep_ms(200)
        _buzz.deinit()