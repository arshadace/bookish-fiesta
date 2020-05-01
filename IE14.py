a=[]
b=int(input("enter number of elements:"))
for i in range (b):
    c=int(input("element in list:"))
    a.append(c)
a=list(dict.fromkeys(a))
print(a)
