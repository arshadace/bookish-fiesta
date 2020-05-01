a=[]
b=int(input("number of elements in the list:"))

for i in range(b):
    c=int(input("elements in the list:"))
    a.append(c)

print(a)
d=[]
for j in range(b):
    if a[j]%2==0:
        d.append(a[j])
print(d)
