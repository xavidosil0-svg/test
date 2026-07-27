from random import randint
y=randint(0,2)
while True:
    x=int (input("player1, guess between 0 to 2"))  
    if x==y:
        print("you got it correct")
        break
    if x>y:
        print("you did not get it correct")
    if x<y:
        print("you did not get it correct")