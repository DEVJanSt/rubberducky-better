from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from board import *
from duckyinpython import *
from defs import *
#from operator import truediv
#from duckyinpython import *
import time
import usb_hid
import board
import digitalio

#Set up Mouse/Keyboard/Layout/LED devices
m = Mouse(usb_hid.devices)
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
cc = ConsumerControl(usb_hid.devices)
led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

#code here: (look in defs.py for the commands, if some important commands are missing, you can build your own)

#example: DELAYMS(420)
#example: GUI()
#example: ENTER()