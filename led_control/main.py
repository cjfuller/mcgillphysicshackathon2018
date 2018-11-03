import time

import led_control.registry as registry

test_series = [
    (1, 15),
    (1, 14),
    (1, 13),
    (1, 12),
    (1, 11),
    (2, 15),
    (2, 14),
    (2, 13),
    (2, 12),
    (2, 11),
]

def run_test_series():
    for coord in test_series:
        controller = registry.controller_for(coord)
        controller.set_state(coord, 1)
        time.sleep(0.2)
        controller.set_state(coord, 0)

if __name__ == '__main__':
    run_test_series()
