def function(listname, element):
   if element in listname:
       print("In list")
   else:
       print("Not in list")

a=[]
b=int(input("number of elements:"))
for i in range (b):
    c=int(input("list numbers:"))
    a.append(c)
n=int(input("enter number:"))
function(a,n)
