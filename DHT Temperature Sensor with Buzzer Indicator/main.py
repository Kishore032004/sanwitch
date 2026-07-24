import dht
from machine import Pin, PWM

while True:
    if dht.DHT11(Pin(24)).temperature() == 45:
        _buzz = PWM(Pin(15), freq=2000, duty=512)
        time.sleep_ms(200)
        _buzz.deinit()
    _dht = dht.DHT11(Pin(24))
    _dht.measure()
    print("temp", _dht.temperature(), "humidity", _dht.humidity())