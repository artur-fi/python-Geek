"""
------------------------
|python|modulos_builtin|
________________________
 # Posso da apelidos para a função RANDOM , aqui estamos Importanto tudo mas está com apelido de rdm
import random as rdm

print(rdm.random())

# Dessa forma importamos TUDO DA FUNÇÃO BUILTIN mas não precisamos botar randon.random() o * deixa usarmos so o que precisa

from random import *
print(random())

import random
print(random.random())

# Podemos da apelidos para módulos também.
from random import randint as rdi, random as rdm

print(rdm())
print(rdi(5, 89))

https://docs.python.org/3/py-modindex.html
"""

# PADRÃO QUANDO FOR IMPORTAR MULTIPLOS MÓDULOS FAZEMOS UM TUPLA , E CADA MODULO POR LINHA ####
from random import (
    random,
    randint,
    shuffle,
    choice
)
lis = ['1', '2', '3', '4', '5', '6']
lista = ['artur', 'antunes', 'pereria']
print(random())
print(choice(lista))
print(randint(1,100))
shuffle(lis)
print(lis)