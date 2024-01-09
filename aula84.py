# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))

lista = []
for numero in range(10):
    lista.append(numero)

lista = [numero for numero in range(10)]
print(lista)
