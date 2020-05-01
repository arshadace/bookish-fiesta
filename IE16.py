import random
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = "abcdefghijklmnopqrstuvwxyz"
u = "1234567890"
v = "!@#$%_-^&"

sl=1
tl=5
ul=2
vl=1


cap =  "".join(random.sample(s,sl))
small = "".join(random.sample(t,tl))
num="".join(random.sample(u,ul))
sym="".join(random.sample(v,vl))
password=cap+small+num+sym
print(password)
