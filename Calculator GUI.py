from tkinter import *

root = Tk()
root.title('Eddie Calculator')

mainscreen = Entry(root, width=35)
mainscreen.grid(row=0, column=0, columnspan=5)

#variables

add = False
mult = False
div = False
sub = False

#functions:

def button_click(number):
    current = mainscreen.get()
    mainscreen.delete(0, END)
    mainscreen.insert(0, str(current) + str(number))

def decimal():
    current = mainscreen.get()
    mainscreen.delete(0, END)
    mainscreen.insert(0, str(current) + str('.'))
    
def clear_screen():
    global first_num
    mainscreen.delete(0, END)
    first_num = 0
    second_num = 0

def addition():
    global first_num
    global add
    first_num = float(mainscreen.get())
    mainscreen.delete(0,END)
    print('first_num: ', first_num)
    add = True
    
def subtract():
    global first_num
    global sub
    first_num = float(mainscreen.get())
    mainscreen.delete(0,END)
    print('first_num: ', first_num)
    sub = True
    
def multiply():
    global first_num
    global mult
    first_num = float(mainscreen.get())
    mainscreen.delete(0,END)
    print('first_num: ', first_num)
    mult = True
    
def divide():
    global first_num
    global div
    first_num = float(mainscreen.get())
    mainscreen.delete(0,END)
    print('first_num: ', first_num)
    div = True
    
def equal():
    global first_num
    global second_num
    global add
    global mult
    global div
    global sub
    second_num = float(mainscreen.get())
    if add == True:
        answer  = first_num + second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, answer)
        add = False
    if mult == True:
        answer  = first_num * second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, answer)
        mult = False
    if div == True:
        answer  = first_num / second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, answer)
        div = False
    if sub == True:
        answer  = first_num - second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, answer)
        sub = False

def plus_minus():
    new = (float(mainscreen.get()) * -1)
    mainscreen.delete(0,END)
    mainscreen.insert(0, new)
    
def percentage():
    new = float(mainscreen.get())/100
    mainscreen.delete(0,END)
    mainscreen.insert(0,new) 
    
#make a button widget
myButton7 = Button(root, text = '7', width=10, height=5, command = lambda: button_click(7))
myButton7.grid(row=2, column=0)

myButton8 = Button(root, text = '8', width=10, height=5, command = lambda: button_click(8))
myButton8.grid(row=2, column=1)

myButton9 = Button(root, text = '9', width=10, height=5, command = lambda: button_click(9))
myButton9.grid(row=2, column=2)

myButton4 = Button(root, text = '4', width=10, height=5, command = lambda: button_click(4))
myButton4.grid(row=3, column=0)

myButton5 = Button(root, text = '5', width=10, height=5, command = lambda: button_click(5))
myButton5.grid(row=3, column=1)

myButton6 = Button(root, text = '6', width=10, height=5, command = lambda: button_click(6))
myButton6.grid(row=3, column=2)

myButton1 = Button(root, text = '1', width=10, height=5, command = lambda: button_click(1))
myButton1.grid(row=4, column=0)

myButton2 = Button(root, text = '2', width=10, height=5, command = lambda: button_click(2))
myButton2.grid(row=4, column=1)

myButton3 = Button(root, text = '3', width=10, height=5, command = lambda: button_click(3))
myButton3.grid(row=4, column=2)

myButton0 = Button(root, text = '0', width=10, height=5, command = lambda: button_click(0))
myButton0.grid(row=5, column=0)

myButtonC = Button(root, text ='C', width = 10, height=5, command = clear_screen)
myButtonC.grid(row=1, column = 0)

myButtonNegPos = Button(root, text = '+/-', width = 10, height = 5, command = plus_minus)
myButtonNegPos.grid(row = 1, column = 1)

myButtonPercent = Button(root, text = '%', width = 10, height = 5, command = percentage)
myButtonPercent.grid(row = 1, column = 2)

myButtonDiv = Button(root, text = '/', width = 10, height = 5, command = divide)
myButtonDiv.grid(row = 1, column = 3)

myButtonMult = Button(root, text = 'x', width = 10, height = 5, command = multiply)
myButtonMult.grid(row = 2, column = 3)

myButtonAdd = Button(root, text = '+', width = 10, height = 5, command = addition)
myButtonAdd.grid(row = 3, column = 3)

myButtonSub = Button(root, text = '-', width = 10, height = 5, command = subtract)
myButtonSub.grid(row = 4, column = 3)

myButtonEq = Button(root, text = '=', width = 10, height = 5, command = equal)
myButtonEq.grid(row = 5, column = 3)

myButtonPeriod = Button(root, text = ".", width = 10, height = 5, command = decimal)
myButtonPeriod.grid(row = 5, column = 1)

myButtonClr = Button(root, text = "Clr", width = 10, height = 5, command = clear_screen)
myButtonClr.grid(row = 5, column = 2)






root.mainloop()


