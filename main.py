import keyboard as k
import pyautogui as p
import time as t
from tkinter import *
toggle = False
quitvar1 = False
def setToggle():
    global toggle
    if toggle:
        toggle = False
    elif not toggle:
        toggle = True
    t.sleep(0.25)
def clicker():
    if toggle:
        p.click()
    if k.is_pressed("t"):
        setToggle()
def startClicker():
    clicker()
def quitfunc():
    global quitvar1
    quitvar1 = 1
def guiSetUp():
    global root
    global label
    global button
    global button2
    root = Tk()
    root.title("Autoclicker")
    root.geometry('330x150')
    label = Label(root, text="Press the button or press \"t\" to toggle the Autoclicker").place(x=9,y=0)
    label3 = Label(root, text="Press the off button or press \"s\" to turn off the Autoclicker").place(x=9,y=50)
    label2 = Label(root, text="The autoclicker is off").place(x = 9, y = 23)
    button = Button(root, text='On/Off', command = setToggle).place(x = 130, y = 23)
    quitButton = Button(root, text='Quit', command = quitfunc).place(x=190, y=23)
guiSetUp()
while True:
    root.update()
    if (toggle):
        root.title("Autoclicker (On)")
    else:
        root.title("Autoclicker (Off)")
    if(toggle):
        label2 = Label(root, text="The autoclicker is on").place(x = 9, y = 23)
    else:
        label2 = Label(root, text="The autoclicker is off").place(x = 9, y = 23)
    clicker()
    if (quitvar1 == 1):
        root.destroy()
        break
    if k.is_pressed('s'):
        root.destroy()
        break