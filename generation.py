"""
Generators -> Mais performatico

nomes = ['Carlos', 'Clarisse', 'Camo', 'Vanessa']

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)


# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)


from sys import getsizeof

print(getsizeof('Geek'))  # -> Retorna o tamanho de bytes em memória do elemento passado como parâmetro
print(getsizeof('Artur Antunes pereira da silva souza 88'))

# Gerando uma lista de numero com List comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numero com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numero com dictionary comprehension

dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numero com Generator

gen = getsizeof(x * 10 for x in range(1000))

print(f'=== Para Fazer a mesma tarefa gastamos em memória ===')
print(f'List Comprehension : ..................{list_comp}   bytes')
print(f'Set Comprehension : ...................{set_comp}  bytes')
print(f'Dictionary Comprehension :.............{dic_comp}  bytes')
print(f'Generator : ...........................{gen}    bytes')

lam = lambda x: (x for x in range(1, 100, 1000))
print(list(lam(1)))
"""

# Eu posso iterar com o Generator expression! sim !!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)