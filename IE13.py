a=[1,1]
b=int(input('how many fibonacci numbers?:'))

if b>1:
    for i in range (2,b):
        b=a[i-1]+a[i-2]
        a.append(b)
    print(a)5
elif b==1:
    a.pop(1)
    print(a)
