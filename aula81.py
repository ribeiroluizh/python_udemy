# Função lambda em Python
# A função lambda é uma função como qualquer outra em Python. Porém, não funções anônimas que contém
# apenas uma linha. Ou seja, tudo deve ser contido dentro de uma única expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'Ribeiro'},
    {'nome': 'Maria', 'sobrenome': 'Barbosa'},
    {'nome': 'Daniele', 'sobrenome': 'Lira'},
    {'nome': 'Laura', 'sobrenome': 'Fonseca'},
    {'nome': 'Bruna', 'sobrenome': 'Damásio'},
]

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key= lambda item: item['nome'])
l2 = sorted(lista, key = lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)