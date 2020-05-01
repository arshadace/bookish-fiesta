import random
a= random.randint(1,9)
b=0
c=0
while b != a:
    b = int(input("What's your guess?"))
    c+=1
    if b < a:
        print("Too low")
    elif b > a:
        print("Too high")
    else:
        print("correct")

        print("you took ",c,"tries")
