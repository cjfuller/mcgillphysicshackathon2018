import atexit
from typing import Dict, Optional, Tuple

import pymata_aio.pymata3 as pym
import pymata_aio.constants as c

import led_control.controller as controller

PinLookup = Dict[Tuple[int, int], str]

class ArduinoFirmataController(controller.LEDController):
    """An LED controller that talks firmata to an arduino."""
    def __init__(self, device: str, coord_pin_mapping: PinLookup):
        self._pin_lookup = coord_pin_mapping
        self._device = device
        self._initialized_device: Optional[pym.PyMata3] = None

    def can_handle(self, coord_xy: Tuple[int, int]) -> bool:
        return coord_xy in self._pin_lookup

    def set_state(self, coord_xy: Tuple[int, int], on: bool) -> None:
        if not self.can_handle(coord_xy):
            return
        self._ensure_device_initialized()
        assert self._initialized_device is not None, (
            "_ensure_device_initialized() failed to set up device")
        pin = self._pin_lookup[coord_xy]
        self._initialized_device.digital_write(pin, int(on))

    def _ensure_device_initialized(self) -> None:
        if self._initialized_device is not None:
            return

        self._initialized_device = pym.PyMata3(
            com_port = self._device)

        for pin in self._pin_lookup.values():
            self._initialized_device.set_pin_mode(pin, c.Constants.OUTPUT)
            self._initialized_device.digital_write(pin, 0)

        atexit.register(lambda: self._shutdown())

    def _shutdown(self) -> None:
        if self._initialized_device is None:
            return
        self._initialized_device.shutdown()
