a=int(input("entrer votre nombre : "))
b=input("entrer la boucle choisie : ")
f=1
retour = 1
if b == 'for':
    print('for')
    for i in range(a):
        retour= retour * f
        f+=1
        print(f-1)

elif b == 'while':
    print('while')
    while a != 0:
        retour = retour * f
        f += 1
        a -= 1
        print(f-1)

print(retour)