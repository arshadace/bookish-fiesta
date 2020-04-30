a=[]
b=int(input('Enter number of elements in a:'))

for i in range(b):
   c=int(input("Element in a:"))
   a.append(c)
for j in a:
    if j<5:
        print(j)
