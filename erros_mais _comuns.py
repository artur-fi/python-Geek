"""
Erros Mais comuns

SyntaxError -> Erro de sintaxe, escreveu errado e o python não reconhece

Ex:

def funcao:  SyntaxError: invalid syntax Faltou o () na declaração da função.

    print('Artur')

None = 1 SyntaxError: can't assign to keyword


"""

a = 2

if a > 11:
    msg = 'Maior que o numero Maximo'
else:
    msg = 'Menor que o numero maximo'

print(msg)

minhalista = ['artur', 'antunes', 'pereira']
x = '#'.join(minhalista)

print(x)

dic = {'name': 'Artur', 'Country': 'BRAZIL'}
separator = 'TEST'
x = separator.join(dic.values())
print(x)
print(dic)
print(f'Hello {dic["name"].upper()}, I never meet anyone From {dic["Country"].title()}.')