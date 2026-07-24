import time
import dht
from machine import Pin

while True:
    time.sleep_ms(1000)
    _dht = dht.DHT11(Pin(14))
    _dht.measure()
    print("temp", _dht.temperature(), "humidity", _dht.humidity())