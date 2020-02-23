"""from random import random

for i in range(1, 10):
    print(random())

Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (build-in). Agora temos que importar e
utilizar esta função a partir do módulo 'functools'

Utilizar o reduce() se você realmente precisar dela. Em todo caso, 99% das vezes um loop for é mais legível.

from functools import reduce

lista = [1, 3,  23, 2, -1, 7, 8, 9, 10]

lambida = lambda x, y: x * y
res = reduce(lambida, lista)
print(res)

"""
lista = [1, 3,  23, 2, -1, 7, 8, 9, 10]

res = 1
for n in lista:
    res = res * n

print(res)
