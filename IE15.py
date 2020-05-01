a=input("enter the string:")
b=a.split(" ")
c=len(b)
d=c//2
for i in range (d):
    temp=b[i]
    b[i]=b[c-i-1]
    b[c-i-1]=temp
a=" ".join(b)
print(a)
