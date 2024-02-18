from functools import reduce

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def funcao_do_reduce( acumulador, produto):
    print('acumulador', acumulador)
    print('produto', produto)
    print()
    return acumulador + produto['preco']

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print(type(total))




print(sum(
    p['preco'] for p in produtos
))
# print_iter(produtos)
# print_iter(novos_produtos)