a=input()
n=len(a)
i=n//2
k=0
for j in range(i):
    if(a[j]==a[n-j-1]):
        k=k+1
if k==i:
    print("string is a palindrome ")
    
else:
    print(" string is not a palindrome")
