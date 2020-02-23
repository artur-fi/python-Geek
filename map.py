"""
Map

com map, fazemos mapeamento de valores para função


import math


def area(r):
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

# Forma 1

raios = [2, 5, 7.1, 0.3, 10, 44]

areas = []

for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2

areas = map(lambda t: math.pi * (t ** 2), raios)
print(list(areas))
print(areas)
print(list(areas))
"""

city = [('Berlim', 29), ('cairo', 40), ('Londres', 100), ['New York', -18.001]]
print(city)

# f = 9/5 * c + 32

# lambda
c_para_f = lambda dados: (dados[0], (9 / 5) * dados[1] + 32)
print(list(map(c_para_f, city)))
