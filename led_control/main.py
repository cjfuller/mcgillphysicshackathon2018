import random
import time

import led_control.registry as registry


test_series = [
    (x, y)
    for x in range(1, 7)
    for y in range(15, 10, -1)
]

def run_test_series():
    registry.initialize()
    for coord in test_series:
        controller = registry.controller_for(coord)
        if controller:
            controller.set_state(coord, 1)
            time.sleep(0.2)
            controller.set_state(coord, 0)

def run_random_series():
    while True:
        x = random.randrange(1, 7)
        y = random.randrange(11, 16)
        state = random.randrange(0, 2)
        coord = (x, y)
        controller = registry.controller_for(coord)
        if controller:
            controller.set_state(coord, state)
        time.sleep(0.1)

if __name__ == '__main__':
    #run_test_series()
    run_random_series()
