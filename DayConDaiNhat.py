import random
lmax = 0
a = []
ld = []
b = []
for i in range(0, 6):
    n = random.randint(0,15)
    a.append(n)
    b.append(0)
    ld.append(0)

print(a)
ld[0] = 1

for i in range(1, len(a)):
    lmax = 0
    for j in range(0, i):
        if (a[i] > a[j]):
            if (ld[j] > lmax):
                lmax = ld[j]
                b[i] = j
    ld[i] = lmax + 1

print(ld)
print(b)
MAX = 0
for i in range(0,6):
    if (ld[i] > ld[MAX]):
        MAX = i
#print(MAX)
while (True):
    i = MAX
    print(a[i])
    MAX = b[i]
    #print(MAX)
    if b[MAX] == 0:
        print(a[MAX])
        break

