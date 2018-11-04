from typing import Optional, Tuple

import led_control.arduino_controller as ac
import led_control.controller as controller

def debug_hook(pin, state):
    print(f'{pin} -> {state}')

controllers = [
    ac.ArduinoFirmataController(
        device='/dev/tty.usbmodem144401',
        coord_pin_mapping = {
            (1, 15): 2,
            (1, 14): 3,
            (1, 13): 4,
            (1, 12): 5,
            (1, 11): 6,
            (2, 15): 7,
            (2, 14): 8,
            (2, 13): 9,
            (2, 12): 10,
            (2, 11): 11,
            (3, 15): 12,
            (3, 14): 13,
        }
    ),
    ac.ArduinoFirmataController(
        device='/dev/tty.usbmodem144301',
        coord_pin_mapping = {
            (3, 13): 2,
            (3, 12): 3,
            (3, 11): 4,
            (4, 15): 5,
            (4, 14): 6,
            (4, 13): 7,
            (4, 12): 8,
            (4, 11): 9,
            (5, 15): 10,
            (5, 14): 11,
            (5, 13): 12,
            (5, 12): 13,
        }
    ),
    ac.ArduinoFirmataController(
        device='/dev/tty.usbmodem144201',
        coord_pin_mapping = {
            (5, 11): 2,
            (6, 15): 3,
            (6, 14): 4,
            (6, 13): 5,
            (6, 12): 6,
            (6, 11): 7,
        },
        hook_fn=debug_hook
    ),
]

# If we've already found a controller for a given pin, this caches that
# controller, so that we don't have to do a linear time lookup.
known_controller_map = {}

def initialize() -> None:
    for c in controllers:
        c.ensure_device_initialized()

def controller_for(
    coord_xy: Tuple[int, int]
) -> Optional[controller.LEDController]:
    if coord_xy in known_controller_map:
        return known_controller_map[coord_xy]

    for c in controllers:
        if c.can_handle(coord_xy):
            known_controller_map[coord_xy] = c
            return c

    return None
