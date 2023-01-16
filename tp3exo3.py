from random import *

a=randint(0,100)
b=102
i=0
while b != a:
    b=int(input("entrer un nombre"))
    if b < a :
        print("trop petit")
        i=i+1
    if b > a:
        print("trop grand")
        i=i+1
print("vous avez mis {} tour".format(i))