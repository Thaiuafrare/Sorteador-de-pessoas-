
import random
lista = []
o = len(lista)
n = int(input('Quantos pessoas irão participar: '))
k = 1
for l in range(n):
    num = str(input('Digite o %d° participante: ' %(k)))
    lista.append(num)
    k = k + 1
o = len(lista)
k = random.randint(0,o)
print('A pessoa sorteada foi :',lista[k])
