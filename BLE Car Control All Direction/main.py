import bluetooth
from machine import Pin

from ble_uart import BLEUART
import bluetooth
_ble = bluetooth.BLE()
_uart = BLEUART(_ble, name="Sanwitch-ESP32")
while True:
    msg = (_uart.read().decode().strip() if _uart.any() else "")
    if msg == "FRONT :PUSH":
        print("Front  Pressed")
        Pin(26, Pin.OUT).value(1)
        Pin(27, Pin.OUT).value(0)
        Pin(26, Pin.OUT).value(1)
        Pin(27, Pin.OUT).value(0)
    if msg == "STOP :PUSH":
        print("Stop  Pressed")
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(0)
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(0)
    if msg == "BACK:PUSH":
        print("Back Pressed")
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
    if msg == "LEFT:PUSH":
        print("LEFT Pressed")
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
    if msg == "RIGHT:PUSH":
        print("RIGHT Pressed")
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)
        Pin(26, Pin.OUT).value(0)
        Pin(27, Pin.OUT).value(1)