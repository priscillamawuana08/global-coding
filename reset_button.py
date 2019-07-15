import button
from gpiozero import LED
from time import sleep

from subprocess import call


def print_button_pressed():
    print ("button pressed")

button.when_pressed = print_button_pressed




button = Button(2)
led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)

from gpiozero import LED, Button
from signal import pause

led = LED(17)
button = Button(2)

button.when_pressed = led.on
button.when_released = led.off

pause()










