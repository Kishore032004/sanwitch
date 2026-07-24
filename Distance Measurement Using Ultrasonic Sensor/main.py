import time
from machine import Pin, time_pulse_us

def read_ultrasonic_cm(trig_pin, echo_pin):
    trig = Pin(trig_pin, Pin.OUT)
    echo = Pin(echo_pin, Pin.IN)
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    duration = time_pulse_us(echo, 1, 30000)
    return duration / 58

while True:
    print(read_ultrasonic_cm(5, 18))