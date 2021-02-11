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
equal = False
storage = float(0)

#functions

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
    global storage
    global equal
    global add
    global mult
    global div
    global sub
    mainscreen.delete(0, END)
    storage = float(0)
    add = False
    mult = False
    div = False
    sub = False
    equal = False
    operation = False
    
def addition():
    global storage
    global add
    global equal
    global sub
    global mult
    global div
    if equal == True and add == False:
        mainscreen.delete(0,END)
        add = True
        equal = False
        print('step1')
    elif equal == False and add == False and sub == False and mult == False and div == False:
        storage = storage + float(mainscreen.get())
        mainscreen.delete(0,END)
        print('storage(addition): ', storage)
        add = True
        print('step2')
    ###functions for applying mult diff operations##
    ## subtraction followed by addition
    if sub == True and add == False:
        storage = storage - float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        sub = False
        add = True
    ## mult followed by addition
    if mult == True and add == False:
        storage = storage * float(mainscreen.get())
        mainscreen.delete(0,END)
        mult = False
        add = True
    ## div followed by addition
    if div == True and add == False:
        storage = storage / float(mainscreen.get())
        mainscreen.delete(0,END)
        div = False
        add = True
        
def subtract():
    global storage
    global sub
    global equal
    global add
    global mult
    global div
        
    if equal == True and sub == False:
        mainscreen.delete(0,END)
        sub = True
        equal = False
        print('step1')
        
    elif equal == False and sub == True:
        storage = storage - float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step3')
        print('first_num(subtraction): ', storage)
        
    elif equal == False and sub == False and add == False and mult == False and div == False:
        storage = float(mainscreen.get()) - storage
        mainscreen.delete(0,END)
        print('first_num(subtraction): ', storage)
        sub = True
        print('step2')
        
    ###functions for applying mult diff operations###
    ## addition followed by sub
    if add == True and sub == False:
        storage = storage + float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        add = False
        sub = True
    ## mult followed by sub
    if mult == True and sub == False:
        storage = storage * float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        mult = False
        sub = True
    ## div folllowed by sub
    if div == True and sub == False:
        storage = storage / float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        div = False
        sub = True
        
def multiply():
    global storage
    global mult
    global equal
    global add
    global sub
    global div
    
    if equal == True and mult == False:
        mainscreen.delete(0,END)
        mult = True
        equal = False
        print('step1')
        
    elif equal == False and mult == True:
        storage = storage * float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step3')
        print('first_num(subtraction): ', storage)
        
    elif equal == False and mult == False and add == False and sub == False and div == False:
        storage = float(mainscreen.get())
        mainscreen.delete(0,END)
        print('first_num(multiplication): ', storage)
        mult = True
        print('step3')
    ####use diff operations####
    #add followed by mult
    if add == True and mult == False:
        storage = storage + float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        add = False
        mult = True
    #sub followed by mult
    if sub == True and mult == False:
        storage = storage - float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        sub = False
        mult = True
    #div followed by mult
    if div == True and mult == False:
        storage = storage / float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        div = False
        mult = True

def divide():
    global storage
    global div
    global equal
    global mult
    global add
    global sub

    if equal == True and div == False:
        mainscreen.delete(0,END)
        div = True
        equal = False
        print('step1')
        
    elif equal == False and div == True:
        storage = storage / float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step3')
        print('first_num(division): ', storage)
        
    elif equal == False and div == False and mult == False and add == False and sub == False:
        storage = float(mainscreen.get())
        mainscreen.delete(0,END)
        print('first_num(division): ', storage)
        div = True
        print('step3')
    ## use diff operations in row
    # add followed by div
    if add == True and div == False:
        storage = storage + float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        add = False
        div = True
    # sub followed by div
    if sub == True and div == False:
        storage = storage - float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        sub = False
        div = True
    # mult followed by div
    if mult == True and div == False:
        storage = storage * float(mainscreen.get())
        mainscreen.delete(0,END)
        print('step4')
        mult = False
        div = True
     
def equal():
    global first_num
    global second_num
    global storage
    global add
    global mult
    global div
    global sub
    global equal
    global operation
    second_num = float(mainscreen.get())
    if add == True:
        storage  = storage + second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, storage)
        add = False
        equal = True
        print('storage(equal):', storage)
        print('step3')
    if sub == True:
        storage  = storage - second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, storage)
        sub = False
        equal = True
        print('second_num: ', second_num)
        print('storage(equal):', storage)
        print('step3')
    if mult == True:
        storage  = storage * second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, storage)
        mult = False
        equal = True
    if div == True:
        storage  = storage / second_num
        mainscreen.delete(0,END)
        mainscreen.insert(0, storage)
        div = False
        equal = True
    
def plus_minus():
    new = (float(mainscreen.get()) * -1)
    mainscreen.delete(0,END)
    mainscreen.insert(0, new)
    
def percentage():
    new = float(mainscreen.get())/100
    mainscreen.delete(0,END)
    mainscreen.insert(0,new) 
    
#make button widgets
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


