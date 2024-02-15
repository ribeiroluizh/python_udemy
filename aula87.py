# List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de itaráveis

#print(list(range(10)))

# lista = []

# for numero in range(10):
#     lista.append(numero)
    
# print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
# ]
# print(lista)

# mapeamento de dados em list comprehension

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

# novos_produtos = [
#     {**produto, 'preco': produto['preco'] *1.05}
#     if produto['preco'] > 20 else {**produto}
#     for produto in produtos
# ]
# print(novos_produtos)
# print(*novos_produtos, sep='\n')
# p(novos_produtos)

# Filtros de dados em list comprehension, o filtro é um item que vem depois do for
# filtro significa que eu não quero incluir determinada coisa se a condição que eu passar seja VERDADEIRA

# O que vem na ESQUERDA do FOR é MAPEAMENTO, o que vai na DIREITA do FOR é FILTRO!!
lista = [    n for n in range(10)     if n < 5    ]
novos_produtos = [
    {**produto, 'preco': produto['preco'] *1.05}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto ['preco'] > 10
]

# List comprehension com mais de um for
lista = []
for x in range(3):
    for y in range(3):
        lista.append((x,y))

lista = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]

lista = [
    [(x, letra) for letra in 'Luiz']
    for x in range(3)
]
# p(lista)


# Há também a possibilidade de utilizar o if antes do for, isso faz com que eu faça um filtro alterando 
# algum dado da lista antiga para a nova lista, por exemplo, quero alterar o numero 6 da lista de 1 a 10

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nova = [
    numero if numero % 2 ==0 #este if, faz com que eu faça um filtro na ADIÇÃO do item na nova lista
    else 600 #neste else, eu estou alterando tudo o que não foi filtrado , quando não entra no if, altera para 600
    # os códigos acima são MAPEAMENTOS ,,, neste caso específico eu não posso omitir esse ELSE
    for numero in lista #aqui estou iterando sobre a lista antiga para inserir na nova lista
    # iteração de onde está vindo o que está MAPEADO
]


###########################
# linhas e colunas

for x in range(1, 11): # criando linhas
    for y in range(1, 6): #criando colunas
        ...

#criando linhas e colunas usando list comprehension
linhas_e_colunas = [
    (x, y)
    if y != 2 else (x * 1000, y * 1000)
    for x in range(1, 11) # linhas
        for y in range (1, 6) # colunas
    if x != 2
]

#####
# trabalhando com strings

nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']

novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}' # é possível utilizar f-string também na list comprehension
    for nome in nomes
]

print(novos_nomes)

