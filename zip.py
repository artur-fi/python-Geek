"""
zip()
lista1 = [1,3,4,11,12]
lista2 = [3,8,9,10,'a']

print(list(zip(lista1,lista2)))
print(tuple(zip(lista1,lista2)))
print(set(zip(lista1,lista2)))
print(dict(zip(lista1,lista2)))

tupla = 1, 2, 3, 4, 5
lista = [1, 3, 6, 7, 10]
dic = {'a': 3, 'b': 5, 'd': 7, 'j': 10}
print(list(zip(tupla, lista, dic.values())))
dados = [(1, 1, 3), (2, 3, 5), (3, 6, 7), (4, 7, 10)]
print(list(zip(*dados)))
"""
prova1 = [80, 98, 99]
prova2 = [70, 84, 111]
alunos = ['maria', 'artur', 'julia']

print(list(zip(alunos,prova2,prova1)))
final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova2, prova1)}
print(final)

# Exemplo com o MAP

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))
print(dict(final))
