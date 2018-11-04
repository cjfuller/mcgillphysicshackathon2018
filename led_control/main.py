import random
import time

import led_control.registry as registry


test_series = [
    (x, y)
    for x in range(7, 10)
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

def run_prod():
    registry.initialize()
    filename = "/Users/colin/mcgillphysicshackathon2018/led.txt"
    while True:
        try:
            with open(filename, 'r') as f:
                data = [line.strip() for line in f if line]

            for line in data:
                x, y, state = map(int, line.split(' '))
                coord = (x + 1, 15 - y)
                controller = registry.controller_for(coord)
                if controller:
                    controller.set_state(coord, state)
        except Exception as e:
            print(e)
        time.sleep(1)

if __name__ == '__main__':
    #run_test_series()
    #run_random_series()
    run_prod()
