"""
Levantando os proprios erros com raise

Ex:

def color(texto, cor):
    if type(texto) is not str:
        raise TypeError('Somente letras são aceitadas no campo Texto')
    if type(cor) is not str:
        raise TypeError('Cor so aceita letraaaaas:')
    print(f'O Seu texto {texto}, sera impresso na cor {cor}.!.')

color('marron', 'preto')
"""

def color(texto, cor):
    cores = ('azul', 'preto', 'amarelo', 'vermelho')
    if type(texto) is not str:
        raise TypeError('Somente letras são aceitadas no campo Texto')
    if type(cor) is not str:
        raise TypeError('Cor so aceita letraaaaas:')
    if cor not in cores:
        raise ValueError(f'A Cor precisa ser uma dessa {cores}')
    print(f'O Seu texto {texto}, sera impresso na cor {cor}.!.')

color('geek', 'roxo')