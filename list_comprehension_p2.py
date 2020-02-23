"""
List Comprehension

Nos podemos adicionar estrutura condicionais logicas as nossas lista comprehension
"""
# 1

numeros = [1, 2, 3, 4, 5, 6, 7]

pares = [numero for numero in numeros if numero % 2 == 0]
impar = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impar)

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

CPF = input('Digite Seu CPF : "É um campo OBRIGATORIO...." ')
print(f'Have a nice Day {CPF}')
nome = input('e Qual Seu nOmE: ')
print(f'Again , Have a nice day {CPF}, with you number {nome.upper()}')