"""
Utilizamos para tratar error que podem ocorrer no nosso código.

try:
    //execução
except:
    // o que deve ser feito em caso de problema

# Exemplo 1
try:
    geek()
except:
    print('Deu algum error!!')

# Exemplo 2
try:
    geek()
except NameError: <- Podemos passar o erro expecífico
    print('Deu algum error!!')

# Exemplo 3
try:
    geek()
except NameError as err:
    print(f'Deu algum error do tipo {err}!!')

# Exemplo 4
try:
    print('geek'[5])
except NameError as erra:
    print(f'Deu algum error do tipo {erra}!!')
except TypeError as errb:
    print(f'Deu Typeerror: {errb}')
except:
    print(f'deu um erro de ')
"""


# Exemplo 5

def pegar_valor(dicionario, valor):
    try:
        return dicionario[valor]
    except:
        return None


dic = {'nome': 'Artur'}

print(pegar_valor(dic, 'nome2'))
