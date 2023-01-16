
'''
a = []
g = 10
while g != 0:
    b = int(input())
    if 0 < b < 20 or b == 20 or b == 0:
        a.append(b)
        print(a)
        g=g-1


retourpetit = 0
retourgrand = 0
retourtresgrand = 0
i = 0
for i in range(10):
    if a[i] < 10:
        retourpetit += 1
    if 10 <= a[i] < 15:
        retourgrand += 1
    if a[i] >= 15:
        retourtresgrand += 1
print("tres grand ", retourtresgrand)
print("grand ", retourgrand)
print("petit " , retourpetit)
'''
retourpetit = 0
retourgrand = 0
retourtresgrand = 0

i=0
while i != 10:
    a=int(input())
    if 0 < a < 20 or a == 20 or a == 0:
        if a< 10:
            retourpetit += 1
            i = i + 1
        if 10 <= a < 15:
            retourgrand += 1
            i = i + 1
        if a >= 15:
            retourtresgrand += 1
            i=i+1


print("tres grand ", retourtresgrand)
print("grand ", retourgrand)
print("petit " , retourpetit)