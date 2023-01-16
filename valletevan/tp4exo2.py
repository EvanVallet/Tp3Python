nombreEtudiants = int(input("Donnez le nombre d'etudiants : "))
moyenne = 0.0
note=[]

for i in range(nombreEtudiants):
    note.append(int(input("Donnez la moyenne d'etudiants {} : ".format(i))))
    while note[i]<0 or note[i]>20:
        note.append(int(input("Donnez la moyenne d'etudiants {} : ".format(i))))
    moyenne = note[i]+moyenne


moyenne=moyenne/nombreEtudiants
print("Numéro de l’Etudiant | note | ecart a la moyenne")
for i in range (nombreEtudiants):
    b=note[i]-moyenne
    print(i,"|",note[i],"|",round(b,3))


