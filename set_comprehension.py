"""
Set Comprehension

"""
numeros = {num for num in range(1,7)}
print(numeros)

numero = {x ** 2 for x in range(11)}
print(numero)

numero = {x: x ** 2 for x in range(11)}
print(numero)

letras = {letra for letra in 'Geek University'}  # Conjunto nao ordena e não tem repetição .....
print(letras)