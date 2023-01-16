from time import *

b=int(input())
a=b
for i in range(b+1):
    sleep(0.2)
    print(a)
    a-=1

while b != -1:
    print(b)
    b-=1
    sleep(0.2)
