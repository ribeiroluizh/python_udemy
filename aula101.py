# Exercicio - Unir Listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas listas na ordem
# Use todos os valores da menor lista.
# Ex.:
# ['salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [ ('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG)]
from itertools import zip_longest

def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [
        (l1[i], l2[i]) for i in range(intervalo)
    ]

cidades = ['salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cidades, estado)), sep='\n')
print()
print(list(zip_longest(cidades, estado, fillvalue = 'Sem Cidade')))
