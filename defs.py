from adafruit_hid.keyboard import Keyboard

#from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
#from adafruit_hid.keycode import Keycode
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode

import usb_hid
import time
#import board
#import pwmio

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
#led = pwmio.PWMOut(board.GP25, frequency=5000, duty_cycle=0) #this shit doesnt work



#HERE: create your own commands you want to use 
#(in duckyinpython.py you can see some of the keyboard commands for extending this file)

def DELAYMS(ms):
    time.sleep(ms / 1000)
def DELAYSEC(sec):
    time.sleep(sec)

def STRING(text):
    layout.write(text)
    time.sleep(0.01)

def ENTER():
    kbd.send(Keycode.ENTER)

#def LED(percent):
    #led.duty_cycle = ((percent/100)*65535) #this shit doesnt work

def WINDOWS():
    kbd.send(Keycode.WINDOWS)
def GUI():
    kbd.send(Keycode.GUI)

def BACKSPACE():
    kbd.send(Keycode.Keycode.BACKSPACE)

def CAPS():
    kbd.send(Keycode.Keycode.CAPS_LOCK)
CAPSLOCK = CAPS

def DELETE():
    kbd.send(Keycode.Keycode.DELETE)
def DEL():
    kbd.send(Keycode.Keycode.DELETE)

def TAB():
    kbd.send(Keycode.Keycode.TAB)

def F11():
    kbd.send(Keycode.Keycode.F11)

def UPARROW():
    kbd.send(Keycode.Keycode.UP_ARROW)
def UP():
    kbd.send(Keycode.Keycode.UP_ARROW)

def DOWNARROW():
    kbd.send(Keycode.Keycode.DOWN_ARROW)
def DOWN():
    kbd.send(Keycode.Keycode.DOWN_ARROW)

def RIGHTARROW():
    kbd.send(Keycode.Keycode.RIGHT_ARROW)
def RIGHT():
    kbd.send(Keycode.Keycode.RIGHT_ARROW)

def LEFTARROW():
    kbd.send(Keycode.Keycode.LEFT_ARROW)
def LEFT():
    kbd.send(Keycode.Keycode.LEFT_ARROW)