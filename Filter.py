"""
Filter

filter() -> serve para filtrar dados de uma determinada coleção.

valores = 1, 2, 3, 4, 5, 6

media = (sum(valores) / len(valores))
print(media)

import statistics

dados = [1.3, 0.3, 2.7, 41, -0.1]

# Calculando a média dos dados utilizando a função mean() ->  ' Média '
media = statistics.mean(dados)
print(f'Media : {media}.')


res = (filter(lambda x: x < media, dados))
print(list(res))



paises = ['', 'argentina', 'brasil', '', '', 'colombia', 'equador', 'venezuela']
print(paises)

res = filter(None, paises)
res2 = filter(lambda x: len(x) > 0, paises)
res1 = filter(lambda pais: pais != '', paises)

print(f'{list(res1)} Resultado com ! = ')
print(f'{list(res2)} Resultado com Lambda. !')
print(f'{list(res)} Resultado com None.type !')


usuarios = [
{'username': 'samuel', 'tweets': []},
{'username': 'artur', 'tweets': []},
{'username': 'barbara', 'tweets': ['Eu adoro bolos', 'Eu adoro arroz']},
{'username': 'samu', 'tweets': []},
{'username': 'joel', 'tweets': ['Eu adoro bolos', 'Eu adoro mariola']},
{'username': 'sarah', 'tweets': ['Eu adoro bolos']}
]
print(usuarios)

# Filtrar os usuários que estáo inativos no Twitter

# Forma 1
inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
"""
nomes = ['vanessa', 'ana', 'maria']

lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

