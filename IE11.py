def prime(a):
    if a==1:
        print("unique")
    elif a==2:
        print("prime")
    else:
        for i in range (2,a):
            if (a%i==0):
                print ("not prime")
                break
        if (i==a-1):
            print("prime")    
        
a=int(input("enter the number:"))
prime(a)
