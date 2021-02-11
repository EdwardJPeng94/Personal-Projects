from tkinter import *
root = Tk()
root.title('Tic-tac-toe for 2')

count = 2;
winner_status = False
moves_o = [];
moves_x = [];

#places x's and o's on board
def clickCount(buttonNum, r, c):
    global count
    global moves
    global winner_status
    
    if count % 2 == 0:
        #set button as 'o'
        buttonNum = Button(root, text = 'O', width = 10, height = 5)
        buttonNum.grid(row=r, column=c)
        #add o move to list
        moves_o.append([r,c])
        #wins for o
        if [0,0] in moves_o and [0,1] in moves_o and [0,2] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [1,0] in moves_o and [1,1] in moves_o and [1,2] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [2,0] in moves_o and [2,1] in moves_o and [2,2] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,0] in moves_o and [1,0] in moves_o and [2,0] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,1] in moves_o and [1,1] in moves_o and [2,1] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,2] in moves_o and [1,2] in moves_o and [2,2] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,0] in moves_o and [1,1] in moves_o and [2,2] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [2,0] in moves_o and [1,1] in moves_o and [0,2] in moves_o:
            winner = Label(root, text = 'O wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
    else:
        #set button as 'x'
        buttonNum = Button(root, text = 'X', width = 10, height = 5)
        buttonNum.grid(row=r, column=c)
        #add x move to list
        moves_x.append([r,c])
        #wins for x
        if [0,0] in moves_x and [0,1] in moves_x and [0,2] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [1,0] in moves_x and [1,1] in moves_x and [1,2] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [2,0] in moves_x and [2,1] in moves_x and [2,2] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,0] in moves_x and [1,0] in moves_x and [2,0] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,1] in moves_x and [1,1] in moves_x and [2,1] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,2] in moves_x and [1,2] in moves_x and [2,2] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [0,0] in moves_x and [1,1] in moves_x and [2,2] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
        if [2,0] in moves_x and [1,1] in moves_x and [0,2] in moves_x:
            winner = Label(root, text = 'X wins!', width = 5, height = 5)
            winner.grid(row=3, column= 0, columnspan = 3)
            winner_status = True
            
    count+=1
    
    if count == 11 and winner_status == False:
        tie = Label(root, text = 'Tie!', width = 5, height = 5)
        tie.grid(row=3, column= 0, columnspan = 3)
        
    print('Count: ', count)
    print('Winner_status: ', winner_status)
    print('O moves: ', moves_o)
    print('X moves: ', moves_x)


#determine if there is a win
#a win happens if the first step is called on 0,0 ; 0,1 ; 0,2
    
button0_0 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button0_0, 0, 0))
button0_0.grid(row=0, column=0)

button0_1 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button0_1, 0, 1))
button0_1.grid(row=0, column=1)

button0_2 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button0_2, 0, 2))
button0_2.grid(row=0, column=2)

button1_0 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button1_0, 1, 0))
button1_0.grid(row=1, column=0)

button1_1 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button1_1, 1, 1))
button1_1.grid(row=1, column=1)

button1_2 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button1_2, 1, 2))
button1_2.grid(row=1, column=2)

button2_0 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button2_0, 2, 0))
button2_0.grid(row=2, column=0)

button2_1 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button2_1, 2, 1))
button2_1.grid(row=2, column=1)

button2_2 = Button(root, text = '*', width = 10, height = 5, command = lambda: clickCount(button2_2, 2, 2))
button2_2.grid(row=2, column=2)



root.mainloop()
