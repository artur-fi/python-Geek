"""
Degubando com PDB

PDB -> Python Debugger

"""


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        print(f"Error Encontrado {err}")


# breakpoint(), comando novo incorporado no build-in já vem por padrão no Python3.7 em diante
# NÃO PRECISA MAIS IMPORTAR.

# comandos do breakpoint l -> list , n -> next line, p -> print, c ->continue
# Dentro do Breakpoint conseguo ver todos os Steps da função , encontrando o Error e tratando com mais facilidade

def soma(l, n, p, c):
    return l + n + p + c

breakpoint()
print(soma(2, 5, 6, 8))