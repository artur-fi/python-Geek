"""
Conhecidas por Expressões lambdas, são funções sem nome, ou seja, funções anonimas.

# Função em  Python

def soma(a,b):
    return a + b

    # Função em Python


def funcao(x):
    return 34 * x / 2.02


print(funcao(4))

# Expressão Lambda
lambda x: 34 * x / 2.02


calc = lambda x: 34 * x / 2.02
print(calc(4))


# Podemos ter expressões lambdas com multiplas entradas.
nome_completo = (lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title())
print(nome_completo('Artur  ', 'ANTUNES '))


# Em funções Python podemos ter nenhuma ou várias entradas, em lambdas também

amar = lambda: 'Como não amar python'

uma = lambda x: 3 * x * 1
duas = lambda x, y: (x * y) ** 0.00015

print(amar)
print(uma(4))
print(duas(10, 4))

autores = ['issac zma', 'artur antuen', 'mario barta', 'hujujuju jurema', 'sophia berenice', 'sabrina cl',
           'sarah. d. m. s. souza']

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)


"""


# Função Quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função

def geradora_fun_quadratica(x, a, b, c):
    """Retornar a função F(x)= a * x ** 2 + b * x + c"""
    return lambda: a * x ** 2 + b * x + c


teste = geradora_fun_quadratica(0, 2, 3, -5)

print(teste())
