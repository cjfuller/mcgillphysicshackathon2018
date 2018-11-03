from typing import Optional, Tuple

import led_control.arduino_controller as ac
import led_control.controller as controller

controllers = [
    ac.ArduinoFirmataController(
        device='/dev/tty.usbmodem14501',
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
        }
    )
]

# If we've already found a controller for a given pin, this caches that
# controller, so that we don't have to do a linear time lookup.
known_controller_map = {}

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
