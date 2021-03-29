import numpy
import keyboard as k
import pyautogui as p
import time as t
from tkinter import *
toggle = False
quitvar1 = False
clickVar = "click"
def setToggle():
    global toggle
    if toggle:
        toggle = False
    elif not toggle:
        toggle = True
def clicker():
    if toggle and clickVar == 'click':
        p.click()
    elif toggle and clickVar != 'click':
        p.typewrite(clickVar)
def startClicker():
    clicker()
def quitfunc():
    global quitvar1
    quitvar1 = 1
def ON():
    toggle = True
def OFF():
    toggle = False
def guiSetUp():
    global root
    global label
    global button
    global button2
    global typeVal
    global typewritebox
    global clickVal
    root = Tk()
    clickVal = StringVar()
    root.title("Autoclicker")
    root.geometry('330x150')
    label = Label(root, text="Press the button to toggle the Autoclicker").place(x=9,y=0)
    label3 = Label(root, text="Press the off button to turn off the Autoclicker").place(x=9,y=50)
    label2 = Label(root, text="The autoclicker is off").place(x = 9, y = 23)
    button = Button(root, text='On', command = ON).place(x = 168, y = 23)
    button3 = Button(root, text='Off', command = OFF).place(x = 198, y = 23)
    quitButton = Button(root, text='Quit', command = quitfunc).place(x=130, y=23)
    label4 = Label(root, text="What do you want to write on repeat\n(write \"Click\" or nothing if you want autoclicker)?").place(x=9,y=70)
    typewritebox = Entry(root,textvariable = clickVal).place(x=9,y=110)
guiSetUp()
while True:
    if (toggle):
        root.title("Autoclicker (On)")
        root.update()
    else:
        root.title("Autoclicker (Off)")
        root.update()
    if(toggle):
        label2 = Label(root, text="The autoclicker is on").place(x = 9, y = 23)
        root.update()
    else:
        label2 = Label(root, text="The autoclicker is off").place(x = 9, y = 23)
        root.update()
    if clickVar == "click":
        label5 = Label(root, text = 'clicking').place(x = 150, y = 110)
        root.update()
    else:
        label5 = Label(root, text = clickVar).place(x = 150, y = 110)
        root.update()
    if k.is_pressed("enter"):              
        clickVar = clickVal.get()
        print(clickVar)
        root.update()
    clicker()
    if (quitvar1 == 1):
        root.destroy()
        break