board: list[list[str]] = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
z=int(1)
for X in range (5):
    for j in range (3):
        for i in range (3):
            x=print(board [i][j], end=" ")
        print()
    if board [0][0]=="O" and board [1][1]=="O" and board [2][2]=="O":
        print ("you won!")
        break
    if board [0][0]=="O" and board [0][1]=="O" and board [0][2]=="O":
        print ("you won!")
        break
    if board [0][0]=="O" and board [1][0]=="O" and board [2][0]=="O":
        print ("you won!")
        break
    if board [0][2]=="O" and board [1][1]=="O" and board [2][0]=="O":
        print ("you won!")
        break
    if board [1][0]=="O" and board [1][1]=="O" and board [1][2]=="O":
        print ("you won!")
        break
    if board [2][0]=="O" and board [2][1]=="O" and board [2][2]=="O":
        print ("you won!")
        break
    if board [0][2]=="O" and board [1][2]=="O" and board [2][2]=="O":
        print ("you won!")
        break
    if board [0][1]=="O" and board [1][1]=="O" and board [2][1]=="O":
        print ("you won!")
        break
    x=int (input("which row do you want to place a piece in?"))
    y=int (input("which column do you want to place a piece in?"))
    if x > 2 or y > 2 or x and y > 2:
        print("you are going out of bounds. select an integer between 0 and 2.")
    else:
        print("turn done")
        if board [x][y]=="O":
            print("spot taken")
        else:
            board [x][y]="X"
    for j in range (3):
        for i in range (3):
            x=print(board [i][j], end=" ")
        print()
    if board [0][0]=="X" and board [1][1]=="X" and board [2][2]=="X":
        print ("you won!")
        break
    if board [0][0]=="X" and board [0][1]=="X" and board [0][2]=="X":
        print ("you won!")
        break
    if board [0][0]=="X" and board [1][0]=="X" and board [2][0]=="X":
        print ("you won!")
        break
    if board [2][2]=="X" and board [1][1]=="X" and board [0][0]=="X":
        print ("you won!")
        break
    if board [1][0]=="X" and board [1][1]=="X" and board [1][2]=="X":
        print ("you won!")
        break
    if board [2][0]=="X" and board [2][1]=="X" and board [2][2]=="X":
        print ("you won!")
        break
    if board [0][2]=="X" and board [1][2]=="X" and board [2][2]=="X":
        print ("you won!")
        break
    if board [0][1]=="X" and board [1][1]=="X" and board [2][1]=="X":
        print ("you won!")
        break
    x=int (input("which row do you want to place a piece in?"))
    y=int (input("which column do you want to place a piece in?"))       
    if x > 2 or y > 2 or x and y > 2:
        print("you are going out of bounds. select an integer between 0 and 2.")
    else:
        print("turn done")
        if board [x][y]=="X":
            print("spot taken")
        else:
            board [x][y]="O"
    if z==9:
        print("draw")
        break