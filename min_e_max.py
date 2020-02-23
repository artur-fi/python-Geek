"""
Min e min

min() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

# Exemplo de min
from typing import List

lista = [1, 3, 4, 5, 6, 10, 100]
print(min(lista))

tupla = (1, 3, 4, 5, 6, 10, 100)
print(min(tupla))

conjunto = {1, 3, 4, 5, 6, 10, 100}
print(min(conjunto))

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 19, 'e': 10}
print(min(dicionario))

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 19, 'e': 10}
print(min(dicionario.values()))

lista = [1, 3, 4, 5, 6, 10, 100]
print(min(lista))

tupla = (1, 3, 4, 5, 6, 10, 100)
print(min(tupla))

conjunto = {1, 3, 4, 5, 6, 10, 100}
print(min(conjunto))

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 19, 'e': 10}
print(min(dicionario))

dicionario = {'a': 1, 'b': 4, 'c': 8, 'd': 19, 'e': 10}
print(min(dicionario.values()))
val1 = int(input('Informe o Primeiro Valor :'))
val2 = int(input('Informe o Segundo Valor :'))
a = min(val1, val2)
print(f'O Maior Valor é {a}.')

"""
musica = [
    {'titulo': 'Maria', 'tocou': 3},
    {'titulo': 'mas', 'tocou': 12},
    {'titulo': 'dar', 'tocou': 30},
    {'titulo': 'ferna', 'tocou': 13},
    {'titulo': 'eliche', 'tocou': 233},
    {'titulo': 'Artur', 'tocou': 35},
    {'titulo': 'Denais', 'tocou': 9},
    {'titulo': 'Apple', 'tocou': 10}
]

print(max(musica, key=lambda musica: musica['tocou'])['titulo'])
print(min(musica, key=lambda musica: musica['tocou'])['titulo'])

max = 0 # declaro a variavel com valor 0
for er in musica: # para (for) er (variavel) em(in) musica (dicionario a cima) :(faça)
    if er['tocou'] > max: # Se(if) er['tocou'](variael na chave 'tocou') for maior que o max(valor com 0 inicial)
        max = er['tocou'] # o Maximo vai Valer o Maior Valor.

print(max)

min = 9999999999999999999 # Valor Grande para que não exista algum maior que esse
for ir in musica: # Para ir em musica faça.
    if ir['tocou'] < min: # se ir na chave "tocou" for menor que o min:
        min = ir['tocou'] # Min vai receber o menor valor do dicionario na chave ['tocou']
print(min)
teste = 3*100000000
print(teste)