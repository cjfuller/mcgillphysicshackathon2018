import time

import led_control.registry as registry


test_series = [
    (x, y)
    for x in range(1, 5)
    for y in range(15, 10, -1)
]

def run_test_series():
    registry.initialize()
    for coord in test_series:
        controller = registry.controller_for(coord)
        controller.set_state(coord, 1)
        time.sleep(0.2)
        controller.set_state(coord, 0)

if __name__ == '__main__':
    run_test_series()
