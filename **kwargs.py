"""

-------------------------------------------------------------------------------------------------------
NAS FUNÇÕES, PODEMOS TER ESSA ORDEM

- Parâmetros obrigatorios;
- *args
- Parâmetros default (não obrigatorios)
- **kwargs


def minha_funcao(nome, idade, *args, solteiro=True, **kwargs):
    print(f'{nome} tem {idade} anos !!')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao('Artur', 18,123123,artur='false')


-------------------------------------------------------------------------------------------------------
def mostra_indo(a, b, *args, instrutor='Geek', **kwargs):
    return[a, b, args, instrutor, kwargs]


print(mostra_indo(1,2,3, sobrenome='University', cargo='Instrutor'))
-------------------------------------------------------------------------------------------------------
É um parametro de **kwargs


Este parametros é diferente do *args o **kwargs exige que utilizemos parametros nomeados, e transforma esses parâmetros extra em um dicionario;


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', cero='Amarelo', Pedro='Marrom')
cores_favoritas()
cores_favoritas(artur='Branco')
cores_favoritas()




def comprimento_especiais(**kwargs):
    if 'valor' in kwargs and kwargs['valor'] == 'Python':
        return 'Você recebeu um cumprimento pythônico'
    elif 'valor' in kwargs:
        return f"{kwargs['valor']} Geek!"
    return 'Não tenho certeza quem você é '


print(comprimento_especiais())
print(comprimento_especiais(valor='Python'))
print(comprimento_especiais(valor='especial'))

# desempacotamento de kwargs
def mostra_nomes(**kwargs):
    return f'{kwargs["nome"]} {kwargs["sobrenome"]}'


nomes = {'nome': 'Felicity', 'sobrenome': 'Jhones'}
print(mostra_nomes(**nomes))
"""


def soma(a, b, c):
    print(a + b + c)


lista = [1, 3, 4]
print(soma(*lista))
 