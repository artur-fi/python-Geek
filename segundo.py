import primeiro


def funcao2():
    primeiro.funcao()


if __name__ == '__main__':
    funcao2()
    print("Estamos dentro do Segundo")
else:
    print(f"{__name__} foi importado.")