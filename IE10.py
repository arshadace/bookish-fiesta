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
c=[x for x in a  if x in d]
print(c)
