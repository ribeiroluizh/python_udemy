# lista = [
#     {'nome': 'Luiz', 'sobrenome': 'Ribeiro'},
#     {'nome': 'Laura', 'sobrenome': 'Bastos'},
#     {'nome': 'Bruna', 'sobrenome': 'Bastos'},
#     {'nome': 'Maria', 'sobrenome': 'Barbosa'},
#     {'nome': 'Marina', 'sobrenome': 'Santos'},
#     {'nome': 'Daniele', 'sobrenome': 'Moreira'},
# ]

# def exibir(lista):
#     for item in lista:
#         print(item)

# l1 = sorted(lista, key=lambda item: item['nome'])
# l2 = sorted(lista, key=lambda item: item['sobrenome'])


# for item in l1:
#     print(item)

# print()

# for item in l2:
#     print(item)

# lambda é uma função normal, porém que é escrita em apenas 
# uma linha de código. ela é criada na própria linha, não existe o 'def' no caso


# função lambda é anomina, ou seja, não possui nome nessa função

# lista = [4,32,1,34,5,6,6,21]
# lista.sort()
# print(lista)

#sorted(lista) ele cria uma copia da lista ordenada, diferente do lista.sort() que ordena a lista original

# def executa(funcao, *args):
#     return funcao(*args)


# def soma(x, y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica



# print (
#     executa(
#         lambda x, y: x + y,
#         2,3
#     )
# )


# print(
#     executa(
#         lambda *args: sum(args),
#         1, 2, 3, 4, 5, 6, 7
#     )
# )