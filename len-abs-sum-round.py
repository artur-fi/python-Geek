"""
Len, Abs, Sum, Round

#Len

len() -> Retorna o tamanho

print(len('Artur Antunes '))
print(len([1,2,3,4,56,]))
print(len((1,3,4,5,6,7,8)))
print(len({1, 2, 3, 4, 5, 7, 8, }))
print(len(range(0, 10)))
print(len({'a': 1, 'n': 3, 'b': 5, 'toalhas': 7}))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:


# Função DUNDER LEN ( dois underline )
print('Artur'.__len__())

# ABS -> Muito util para retorna valores positivos para a função
abs() -> Ela retorna o Valor Absoluto de um numero .

# Exeplos de abs

print(abs(-5))
print(abs(5))
print(abs(3.15))
print(abs(-3.14))

sum() -> soma os valores
# Exemplo

print(sum([1,2,4,54,6,7], 10))
print(sum([3.412341241, 12309120391.10293019]))
print(sum({'a': 1, 'b': 3, 'c': 4, 'd': 10}.values(), 10))

round() -> Retorna um número arredondado
"""
# Retorna tanto numero inteiro quanto numero real.
print(round(10.2))
print(round(10.5))
print(round(1.123123123123, 1))
print(round(1.2999, 1))
