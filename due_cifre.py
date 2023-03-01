z=0
global p
p=0
scomp_n = []

cifra_uno = input('cifra uno: ')
cifra_due = input('cifra due: ')
n = int(input('N: '))+1

def zero():
    if str(cifra_uno) in scomp_n or str(cifra_due) in scomp_n:
        global p
        p += 1
        stop = len(scomp_n)
        del scomp_n[0:stop]

for i in range(n):
    i = str(i)
    scomp_n = list(i)
    zero()
    
z = n-int(p)
print(f'Numeri senza {cifra_uno} e {cifra_due} con 0 inziale incluso: {z}')
print(f'Numeri con {cifra_uno} e {cifra_due}: {p}')
