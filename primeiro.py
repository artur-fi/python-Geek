def funcao():
    print("Geek University")


if __name__ == '__main__':
    funcao()
    print("primeiro.py esta sendo executado diretamente")
else:
    print(f'{__name__} Importado com sucesso')
