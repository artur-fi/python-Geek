"""
Sorted = ORDENA do menor para o Maior , e SEMPRE RETORNA UMA LISTA .

OBS: Não confunda, com a função sort(), o sort() só funciona em LISTA.

Podemos Utilizar o SORTED com QUALQUER iterável.

lista = [1, 4, 5, 6, 7, 2, 3, 10, 9]
lista.sort()
print(lista)


lista = {1, 4, 5, 6, 7, 2, 3, 9}

print(sorted(lista)) # Vou Ordenar do Menor para o Maior
print(lista)


lista = [1, 4, 5, 6, 7, 2, 3, 9]
print(sorted(lista, reverse=True)) # Faz a lista ficar de tras para frente .

print(lista)
print(sorted(lista))
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

# Ordena da Menos tocada para a mais tocada
print(sorted(musica, key=lambda musica: musica['tocou']))


# Ordena da Mais Tocada para a menos tocada
print(sorted(musica, key=lambda musica: musica['tocou'], reverse=True))