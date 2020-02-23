"""
Any e All

all() -> Retorna True se todos os elementos do iteravel são verdadeiros ou ainda se o iterável está vazio.
# Exemplo all

print(all([-1, 0, 1, 4, 5, 6, 0,7]))
print(all([]))
print(all([num for num in [1, 4, 6, 7, 8, 123, 4, 6, 7, 901, 80] if num % 2 == 0]))

any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""
# Exemplo any()
print(any([0, 0, 0, 0, 0, 0, 2]))
print(any([False, [], {}, (), 0]))


nomes = ['Carlos', 'Clarisse', 'Camo', 'Vanessa']
print(any([nome[1] == 'a' for nome in nomes]))
print(any([num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] if num % 2 == 0]))