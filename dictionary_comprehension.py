"""
Dictionary Comprehension


numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)


# Exemplos

numeros = (1, 2, 3, 4, 5, 1, 3, 7)
asi = {valor:valor ** 2.5 for valor in numeros}
print(asi)

chave = 'sdfghjkloiuy'
valor = [1, 2, 3, 4, 5, 6, 7,8,9,0,11,12]
print(len(chave))


mistura = {chave[i]: valor[i] for i in range(0, len(chave))}
quadrado = {key: value ** 2 for key, value in mistura.items()}
half = {key: value / 1.5 for key, value in quadrado.items()}
print(mistura)
print(quadrado)
print(half)
"""
numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrado)


# Exemplos

numeros = (1, 2, 3, 4, 5, 1, 3, 7)
asi = {valor:valor ** 2.5 for valor in numeros}
print(asi)

chave = 'keywordgti'
valor = [1, 2, 3, 4, 5, 6, 7,8,9,0,11,12]
print(len(chave))


mistura = {chave[i]: valor[i] for i in range(0, len(chave))}
quadrado = {key: value ** 2 for key, value in mistura.items()}
half = {key: value / 1.5 for key, value in quadrado.items()}
print(mistura)
print(quadrado)
print(half)

# Exemplos com logica condicional

numeros = [1, 2, 4, 5, 6, 7, 6]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}
print(res)