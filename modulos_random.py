"""
Módulo Random e o que são módulos ?

-Em Python, modulos são arquivos Python.

Random -> Possui Funções para geração de números pseudo-aleatórios .
# OBS: Duas formas de usar o random

# Forma 1

import random # Não Recomendado.

# Ao realizar o import de todo o módulo, todas as funções, atributos, classes e propriedades que estiverem
# Dentro do módulo ficarão disponíveis (Ficarão em memoria).
# So importar as funções necessarias.

# OBS: NÃO CONFUNDA A FUNÇÃO RANDOM() COM O PACOTE RANDOM.
print(random.random())

# Forma 2

from random import random

for i in range(1, 10):
    print(random())

from random import uniform

for i in range(10):
    print(uniform(1, 10))

# Gerador de numeros para mega

from random import randint

for i in range(6):
    e = randint(0, 61)
    print(f'Numeros ganhadores da Mega - Sena é {e}')


# Choice() -> mostra um valor aleatório entre um iterável
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))


"""
# shuffle() -> Tem a função de embaralhar dados

from random import shuffle

cartas = ['k', 'q', 'j', 'as', '2', '3', '4', '5', '6']
print(cartas)
shuffle(cartas)
print(cartas.pop())