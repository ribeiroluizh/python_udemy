<<<<<<< HEAD
# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# # print(a1, a2)
# # print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {** pessoa, **dados_pessoa}

# print(pessoa_completa)

# args se refere aos argumentos não nomeados

#kwargs se referente aos keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados (*args, **kwargs):
    print('NÃO NOMEADOS', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1,2,3 , nome= 'Luiz', idade= 32)

=======
# Empacotamento e desempacotamento de dicionários

a, b = 1, 2
a, b = b, a

# print(a, b)


# (a1, a2), (b1, b2) = pessoa.items()
# # print(a1, a2)
# # print(b1, b2)

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoa_completa = {** pessoa, **dados_pessoa}

# print(pessoa_completa)

# args se refere aos argumentos não nomeados

#kwargs se referente aos keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados (*args, **kwargs):
    print('NÃO NOMEADOS', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1,2,3 , nome= 'Luiz', idade= 32)

>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
mostro_argumentos_nomeados(**pessoa_completa)