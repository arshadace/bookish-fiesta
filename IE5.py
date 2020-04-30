a=[]
b=int(input('Enter number of elements in a:'))

for i in range(b):
   c=int(input("Element in a:"))
   a.append(c)
print("a=",a)   
d=[]
e=int(input('Enter number of elements in b:'))

for j in range(e):
   f=int(input("Element in b:"))
   d.append(f)
print("b=",d)

for i in range (b):
    for j in range (e):
        if a[i]==d[j]:
            print(a[i])
