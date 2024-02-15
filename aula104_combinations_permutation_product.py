# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# permutação - ordem importa
# produto - ordem importa e repete valores únicos
from itertools import combinations
from itertools import permutations
from itertools import product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'joao', 'joana', 'luiz', 'leticia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unissex'],
    ['algodao', 'dry-fit']
]

print_iter(combinations(pessoas,2)) # aqui eu chamo a função, combinations (lista, qnt de grupos)
# caso o argumento de qnt de grupos seja maior que a qtd de itens na lista, ele não imprime nada
# o combinations também não mostra as combinações possíveis, ou seja a ordem de não importa, (luiz e leticia, leticia e luiz)
# ele vai mostrar apenas (luiz e leticia) e ponto.

print_iter(permutations(pessoas, 2))

print_iter(product(*camisetas))