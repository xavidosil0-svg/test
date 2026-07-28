board: list[list[str]] = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
for X in range (3):
    for j in range (3):
        for i in range (3):
            x=print(board [i][j], end=" ")
        print()
    x=int (input("which row do you want to place a piece in?"))
    y=int (input("which column do you want to place a piece in?"))
    if x > 2 or y > 2 or x and y > 2:
        print("you are going out of bounds. select an integer between 0 and 2.")
    else:
        print("word")
        board [x][y]="X"
    for j in range (3):
        for i in range (3):
            x=print(board [i][j], end=" ")
        print()
