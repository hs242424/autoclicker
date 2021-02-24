import keyboard as k
import pyautogui as p
import time as t
toggle = False
def setToggle():
    global toggle
    if toggle:
        toggle = False
    elif not toggle:
        toggle = True
    t.sleep(0.25)
while True:
    if k.is_pressed("s"):
        break
    if toggle:
        p.click()
    if k.is_pressed("t"):
        setToggle()
