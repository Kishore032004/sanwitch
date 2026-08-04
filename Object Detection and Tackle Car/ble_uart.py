# ble_uart.py - Simplified BLE UART for MicroPython
import bluetooth
from micropython import const

_ADV_APPEARANCE_GENERIC_COMPUTER = const(128)

class BLEUART:
    def __init__(self, ble, name="mpy-uart", rxbuf=100):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._handle_tx, self._handle_rx),) = self._ble.gatts_register_services((
            (bluetooth.UUID("6E400001-B5A3-F393-E0A9-E50E24DCCA9E"), (
                (bluetooth.UUID("6E400003-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_NOTIFY),
                (bluetooth.UUID("6E400002-B5A3-F393-E0A9-E50E24DCCA9E"), bluetooth.FLAG_WRITE),
            )),
        ))
        self._connections = set()
        self._rx_buffer = bytearray()
        self._handler = None
        self._name = name
        self._advertise()

    def _irq(self, event, data):
        if event == 1: # _IRQ_CENTRAL_CONNECT
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
        elif event == 2: # _IRQ_CENTRAL_DISCONNECT
            conn_handle, _, _ = data
            if conn_handle in self._connections:
                self._connections.remove(conn_handle)
            self._advertise()
        elif event == 3: # _IRQ_GATTS_WRITE
            conn_handle, value_handle = data
            if conn_handle in self._connections and value_handle == self._handle_rx:
                self._rx_buffer.extend(self._ble.gatts_read(self._handle_rx))
                if self._handler: self._handler()

    def any(self):
        return len(self._rx_buffer)

    def read(self, sz=None):
        if not sz: sz = len(self._rx_buffer)
        result = self._rx_buffer[0:sz]
        self._rx_buffer = self._rx_buffer[sz:]
        return result

    def write(self, data):
        for conn_handle in self._connections:
            self._ble.gatts_notify(conn_handle, self._handle_tx, data)

    def _advertise(self, interval_us=500000):
        payload = bytearray(b'\x02\x01\x06')
        payload.append(len(self._name) + 1)
        payload.append(0x09)
        payload.extend(self._name.encode())
        self._ble.gap_advertise(interval_us, adv_data=payload)
