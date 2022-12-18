z=0
global p
p=0
scomp_n = []

cifra = input('cifra: ')
n = input('N: ')


def zero():
    if str(cifra) in scomp_n:
        global p
        p += 1
        stop = len(scomp_n)
        del scomp_n[0:stop]

for i in range(n+1):
    i = str(i)
    scomp_n = list(i)
    zero()
    
z = n-p
print(p)

