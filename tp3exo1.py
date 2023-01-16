from time import *

a=int(input('nb'))
retour=a
for i in range(a):
    if a==0:
        print(retour)
        break
    else:
        a=a-1
        retour=retour+a
print(retour)

