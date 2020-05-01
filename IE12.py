a=[]
def inputlist(a):
    
    b=int(input('Enter number of elements in a:'))

    for i in range(b):
        c=int(input("Element in a:"))
        a.append(c)
inputlist(a)
d=[a[0],a[len(a)-1]]
print(d)
