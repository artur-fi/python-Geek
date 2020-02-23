"""
Funções com parametros Padrão

- funções onde a passagem de parâmetro seja opcional

Exemplo Opicional:

print('artur')
print()

Exemplo Obrigatorio

def quadrado(numero):
    return numero ** 2


print(quadrado(3)) - > Aqui da o resultado
print(quadrado( )) - > Aqui da TypeError

def exponencial(numero=1, potencia=3): # Potencia = 2, se o usuario nao passar o numero para elevar ele faz por padrão ao²
    return numero ** potencia


print(exponencial(2, 3))  # 2*2*2
print(exponencial(3, 4))  # 3*3*3*3
print(exponencial(4))

O PARAMETRO DEFAULT ( COM VALOR DEFINIDO NA FUNÇÃO ) DEVE SER O ULTIMO.
A NÃO SER QUE OS DOIS TENHAM VALORES PADRAO.

def mostra(nome='Artur', instrutor=False):
    if nome == 'Artur' and instrutor:
        return "Bem Vindo, Instrutor"
    elif nome == 'Artur':
        return 'Achei que você era o instrutor'
    return f'{nome}, Seja Bem Vindo.'


print(mostra())
print(mostra('Artur Antunes'))
print(mostra(instrutor=True))


instrutor = 'Geek'   # Variavel Global.


def diz_oi():
    instrutor = 'Python' # Variavel local sobrepoem variaveis globais.
    return print(f'Oi {instrutor}')

# Variavel local só é chamada dentro do escopo !
diz_oi()



total = 0


def incrementa():
    global total # tem que declarar a função para valer ( chamar ela por ser uma variavel global )
    total = total - 5
    return total


print(incrementa())

"""


def fora():
    contador = 10

    def dentro():
        nonlocal contador  # nonlocal -> estamos trazendo a variavel contador da função de cima Igual ao comando global
        contador = contador + 1
        return contador

    return dentro()


print(fora())
