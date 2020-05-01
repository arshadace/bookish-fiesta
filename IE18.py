import random

s="1234567890"
length=4

n="".join(random.sample(s,length))
d=0
while (length):
    a=input("guess 4 digit number:")
    b=0
    c=0 
    for i in range(len(n)):
        if n[i] ==a[i]:
            b+=1
        else:
            c+=1
    d+=1
    print(b,"cows and",c,"bulls")
