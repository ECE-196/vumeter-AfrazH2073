import board
from digitalio import DigitalInOut, Direction
from analogio import AnalogIn
from time import sleep

# setup pins
microphone = AnalogIn(board.IO1)

status = DigitalInOut(board.IO17)
status.direction = Direction.OUTPUT

led_pins = [
    board.IO21,
    board.IO26, # type: ignore
    board.IO47,
    board.IO33, # type: ignore
    board.IO34, # type: ignore
    board.IO48,
    board.IO35,
    board.IO36,
    board.IO37,
    board.IO38,
    board.IO39
]

leds = [DigitalInOut(pin) for pin in led_pins]

for led in leds:
    led.direction = Direction.OUTPUT

max_volume = 40000

def normalize(volume, max_volume, num_leds):
    return int((volume / max_volume * num_leds))

while True:
    volume = microphone.value
    num_leds_on = normalize(volume, max_volume, len(leds))
    
    # Turn on correct number of LEDs
    for i, led in enumerate(leds):
        led.value = i < num_leds_on

    sleep(0.2)

    # instead of blinking,
    # how can you make the LEDs
    # turn on like a volume meter?
