"""
Listas Aninhadas ( Nested Lists)

Em algumas linguagens de programação possuem estrutura de dados chamadas de arrays;
    - unidimensionais (arrays/vetores)
    - multidimensionais (matrizes)

Em Python nós temos as Listas;

numeros = [1, 2, 3, 4, 5]

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3 (3 linhas e 3 colunas)

# Como fazemos para acessar os dados?

print(len(listas))
print(listas[2][2])

for para in listas:
    for num in para:
        print(num,end=' ')

[[print(valor, end='/ ')for valor in lista]for lista in listas]
"""
from typing import List
# Gerando um tabuleiro / Matrix 3x3
tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]
print(tabuleiro)

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)]for valor in range(1, 4)]
print(velha)