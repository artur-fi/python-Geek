"""
Reversed - > <class 'list_reverseiterator'>

OBS : Não confunda com a função reverse() -> SÓ FUNCIONA COM A LISTAS

Já Função com reversed funciona com qualquer iterável.
"""

# Exemplos

lista = [1, 3, 4, 5, 6, 1, 2, 4]

res = reversed(lista)
print(tuple(reversed(lista)))
print(list(reversed(lista)))
print(set(reversed(lista))) # Set não define Ordem e nem numero repetido.

for letra in reversed ('artur antunes'):
    print(letra, end='')
print('/n')
print(''.join(list(reversed('artur antunes'))))

# Como Fazer isso com o Slice de Strings.

print('Artur Antunes'[::-1])

# Poder usar o Reversed() para fazer um loop For reverso

for n in range(10, -11, -1):
    print(n)