from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Connect Four')

#------------------------------------variables--------------------------------##
count = 0
moves_o = []
moves_x = []
placement_0 = 6
placement_1 = 6
placement_2 = 6
placement_3 = 6
placement_4 = 6
placement_5 = 6
placement_6 = 6

#functions
##----------------------------function to place moves ----------------------##
def enter(num):
    global count
    global placement_0
    global placement_1
    global placement_2
    global placement_3
    global placement_4
    global placement_5
    global placement_6
    
    if num == 0:  
        if count % 2 == 0 and placement_0 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg='red')
            move.grid(row = placement_0, column = num)
            moves_o.append((placement_0, num))
            placement_0 -= 1
            count+=1
        elif count % 2 != 0 and placement_0 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg='blue')
            move.grid(row = placement_0, column = num)
            moves_x.append((placement_0, num))
            placement_0 -= 1
            count+=1
    if num == 1:  
        if count % 2 == 0 and placement_1 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg ='red')
            move.grid(row = placement_1, column = num)
            moves_o.append((placement_1, num))
            placement_1 -= 1
            count+=1
        elif count % 2 != 0 and placement_1 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg ='blue')
            move.grid(row = placement_1, column = num)
            moves_x.append((placement_1, num))
            placement_1 -= 1
            count+=1
    if num == 2:  
        if count % 2 == 0 and placement_2 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg='red')
            move.grid(row = placement_2, column = num)
            moves_o.append((placement_2, num))
            placement_2 -= 1
            count+=1
        elif count % 2 != 0 and placement_2 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg='blue')
            move.grid(row = placement_2, column = num)
            moves_x.append((placement_2, num))
            placement_2 -= 1
            count+=1
    if num == 3:  
        if count % 2 == 0 and placement_3 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg = 'red')
            move.grid(row = placement_3, column = num)
            moves_o.append((placement_3, num))
            placement_3 -= 1
            count+=1
        elif count % 2 != 0 and placement_3 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg='blue')
            move.grid(row = placement_3, column = num)
            moves_x.append((placement_3, num))
            placement_3 -= 1
            count+=1
    if num == 4:  
        if count % 2 == 0 and placement_4 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg='red')
            move.grid(row = placement_4, column = num)
            moves_o.append((placement_4, num))
            placement_4 -= 1
            count+=1
        elif count % 2 != 0 and placement_4 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg='blue')
            move.grid(row = placement_4, column = num)
            moves_x.append((placement_4, num))
            placement_4 -= 1
            count+=1
    if num == 5:  
        if count % 2 == 0 and placement_5 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg ='red')
            move.grid(row = placement_5, column = num)
            moves_o.append((placement_5, num))
            placement_5 -= 1
            count+=1
        elif count % 2 != 0 and placement_5 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg='blue')
            move.grid(row = placement_5, column = num)
            moves_x.append((placement_5, num))
            placement_5 -= 1
            count+=1
    if num == 6:  
        if count % 2 == 0 and placement_6 > 0:
            move = Button(root, text = 'O', height = 5, width = 10, fg ='red')
            move.grid(row = placement_6, column = num)
            moves_o.append((placement_6, num))
            placement_6 -= 1
            count+=1
        elif count % 2 != 0 and placement_6 > 0:
            move = Button(root, text = 'X', height = 5, width = 10, fg='blue')
            move.grid(row = placement_6, column = num)
            moves_x.append((placement_6, num))
            placement_6 -= 1
            count+=1
    print('moves_o:', moves_o)
    print('moves_x:', moves_x)
    if count % 2 == 0:
        win_x()
    else:
        win_o()

##------------------------- o wins--------------------------------------------##
def win_o():
    horizontal_win_1 = []
    horizontal_win_2 = []
    horizontal_win_3 = []
    horizontal_win_4 = []
    vertical_win = []

    #horizontal wins 1
    for r in range(moves_o[-1][1] - 3, moves_o[-1][1]+1):
        horizontal_win_1.append((moves_o[-1][0], r))
        
    
    check =  all(move in moves_o for move in horizontal_win_1)
    if check is True:
        print('O wins 1')
        tkinter.messagebox.showinfo('Winner:','O Wins Horizontally!!!')
        
    #horizontal wins 2
    for r in range(moves_o[-1][1] - 2, moves_o[-1][1] + 2):
        horizontal_win_2.append((moves_o[-1][0], r))
    
    check =  all(move in moves_o for move in horizontal_win_2)
    if check is True:
        print('O wins 2')
        tkinter.messagebox.showinfo('Winner:','O Wins Horizontally!!!')
        
    #horizontal wins 3
    for r in range(moves_o[-1][1] - 1, moves_o[-1][1] + 3):
        horizontal_win_3.append((moves_o[-1][0], r))
        
    
    check =  all(move in moves_o for move in horizontal_win_3)
    if check is True:
        print('O wins 3')
        tkinter.messagebox.showinfo('Winner:','O Wins Horizontally!!!')
    #horizontal wins 4
    for r in range(moves_o[-1][1], moves_o[-1][1] + 4):
        horizontal_win_4.append((moves_o[-1][0], r))
    
    check =  all(move in moves_o for move in horizontal_win_4)
    if check is True:
        print('O wins 4')
        tkinter.messagebox.showinfo('Winner:','O Wins Horizontally!!!')
        
#vertical wins
    for c in range(moves_o[-1][0], moves_o[-1][0] + 4):
        vertical_win.append((c, moves_o[-1][1]))
    
    check =  all(move in moves_o for move in vertical_win)
    if check is True:
        print('O wins vertical')
        tkinter.messagebox.showinfo('Winner:','O Wins Vertically!!!')
#positive diagonals
#negative diagonals
        
########### ---------------------- x wins --------------------------------------
def win_x():
    horizontal_win_1 = []
    horizontal_win_2 = []
    horizontal_win_3 = []
    horizontal_win_4 = []
    vertical_win = []
    positive_win = []

    #horizontal wins 1
    for r in range(moves_x[-1][1] - 3, moves_x[-1][1]+1):
        horizontal_win_1.append((moves_x[-1][0], r))
    
    check =  all(move in moves_x for move in horizontal_win_1)
    if check is True:
        print('X wins 1')
        tkinter.messagebox.showinfo('Winner:','X Wins Horizontally!!!')
        
    #horizontal wins 2
    for r in range(moves_x[-1][1] - 2, moves_x[-1][1] + 2):
        horizontal_win_2.append((moves_x[-1][0], r))
        
    check =  all(move in moves_x for move in horizontal_win_2)
    if check is True:
        print('O wins 2')
        tkinter.messagebox.showinfo('Winner:','X Wins Horizontally!!!')
        
    #horizontal wins 3
    for r in range(moves_x[-1][1] - 1, moves_x[-1][1] + 3):
        horizontal_win_3.append((moves_x[-1][0], r))
        

    print('horizontal moves:', horizontal_win_3)
    
    check =  all(move in moves_x for move in horizontal_win_3)
    if check is True:
        print('O wins 3')
        tkinter.messagebox.showinfo('Winner:','X Wins Horizontally!!!')
    #horizontal wins 4
    for r in range(moves_x[-1][1], moves_x[-1][1] + 4):
        horizontal_win_4.append((moves_x[-1][0], r))
    
    check =  all(move in moves_x for move in horizontal_win_4)
    if check is True:
        print('O wins 4')
        tkinter.messagebox.showinfo('Winner:','X Wins Horizontally!!!')
        
#veritcal wins
    for c in range(moves_x[-1][0], moves_x[-1][0] + 4):
        vertical_win.append((c, moves_x[-1][1]))

        
    check =  all(move in moves_x for move in vertical_win)
    if check is True:
        print('X wins vertical')
        tkinter.messagebox.showinfo('Winner:','X Wins Vertically!!!')
#positive diagonals
    for r in range(moves_x[-1][0] + 3, moves_x[-1][0] - 1, -1):
        for c in range(moves_x[-1][1] - 3, moves_x[-1][1] + 1):
            positive_win.append((r,c))
    print('positive win:',positive_win)
    check =  all(move in moves_x for move in positive_win)
    if check is True:
        print('X wins diagonal')
        tkinter.messagebox.showinfo('Winner:','X Wins Diagonally!!!')
            
#negative diagonals
            

####--------------------------------buttons ---------------------------------###
#buttons
for c in range(0,7):
    if c == 0:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(0))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)
    if c == 1:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(1))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)
    if c == 2:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(2))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)
    if c == 3:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(3))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)
    if c == 4:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(4))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)
    if c == 5:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(5))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)
    if c == 6:
        for r in range(0,7):
            if r == 0:
                entry = Button(root, text = 'Press', height = 5, width = 10, command = lambda: enter(6))
                entry.grid(row = r, column = c)
            else:
                blank = Button(root, text = r, height = 5, width = 10)
                blank.grid(row = r, column = c)


root.mainloop()
    
