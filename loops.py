from random import randint
player1=0
player2=0
while player1<3 and player2<3:
    x=input("player1, do you want to play rock paper sccissors?") 
    y=randint(0,2) 
    if x=="rock" and y==1:
        player1+=1
        print("player1 +1")
    if x=="rock" and y==2:
        player1+=1
        print("player1 +1")
    if x=="paper" and y==0:
        player2+=1
        print("player2 +1")
    if x=="sccissors" and y==0:
        player2+=1
        print("player2 +1")
    if x=="sccissors" and y==1:
        player1+=1
        print("player1 +1")
    if x=="paper" and y==2:
        player2+=1
        print("player2 +1")
    if x==y:
        print("DRAW")