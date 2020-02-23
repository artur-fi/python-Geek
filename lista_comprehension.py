"""
Comprehension

    Podemos gerar novas listas com os dados processados a partir de outro iterável.


numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)
res = [numero / 1.3 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]
print(res)

"""

# List comprehension vs loop

# Loop

numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)
print([numero * 2 for numero in [1, 2, 3, 4, 5]])


nome = "Artur"
print([letra.upper() for letra in nome])


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0])
    return nome


amigos = ['maria','joao','pedros','martha']
print([caixa_alta(amigo).upper() for amigo in amigos])

print([numero * 3 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], '', True, 1, 3.4]])

print([str(numero) for numero in [1, 2, 3, 4]])

print([num])