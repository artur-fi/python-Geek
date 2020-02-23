"""
Tratar os erros de ENTRADA NO SISTEMA

# Executado Somente se não ocorrer um error
num = 0
try:
    num = int(input('Informe um Numero'))
except ValueError:
    print('Valor Errado')
else:
    print(f'Você digitou {num}')



# Finallu

try:
    num = int(input("Informe um numero : "))
except ValueError:
    print('Valor Errado:')
else:
    print(f'Você digitou o numero {num} :')
finally:
    print('Executando o finally')

# OBS o bloco finally é sempre executado, no erro ou no acerto

# Geralmente é utilizado para fechar ou desalocar recursos.

"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        print("Valor Incorreto")


num1 = input("Informe o Primeiro Valor :")
num2 = input("Informe o Segundo valor :")

print(dividir(num1, num2))