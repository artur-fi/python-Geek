"""
O *args é um parametro utilizado em uma função e coloca os valores informados em uma tupla.

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
    return print(total)


soma(1,46,8,10,20320,9514.040491,0.94914)


def soma1(*args):
    return sum(args) # de forma mais simplificada , já que ele gera uma tupla. so somar a tupla.

print(soma1(1,1,1,1,1,1,1,1))

"""


def verifica_info(*args):
    if 'Artur' in args and 'Antunes' in args:
        return 'Bem vindo Artur Antunes!!!'
    return 'Eu não tenho certeza que é !!!'


print(verifica_info('Artur', False, "123123123123", "antunes"))
print(verifica_info('Antunes', True, 'Poder ', 'Artur'))


def soma(*args):
    return sum(args)


numeros = [1,3,4,5,6,6,8]

print(soma(*numeros)) # o * desempacota a lista fazendo assim a Soma.