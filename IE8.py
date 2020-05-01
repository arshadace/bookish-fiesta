n=1
while (n):
    a=int(input("player1 1.rock 2.paper 3.scissors:"))
    b=int(input("player2 1.rock 2.paper 3.scissors:"))
    while (a>0 and a<4 and b>0 and b<4):
        if(a+b!=4):
            if(a>b):
                print("player1 wins")
            elif(a<b):
                print("player2 wins")
        else:
            if(a<b):
                print("player1 wins")
            elif(b<a):
                print("player2 wins")
        
        break

    print("\nnew game")
