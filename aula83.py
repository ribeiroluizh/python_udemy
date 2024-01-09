# Empacotamento e desempacotamento
a, b = 1, 2
a, b = b, a

# print(a, b)

pessoa = {
    'nome': 'Bruna',
    'sobrenome': 'Bastos',
}

dados_pessoa = {
    'idade': 31,
    'altura': 1.58
}

pessoa_completa = {**pessoa, **dados_pessoa}


def mostro_argumentos_nomeados(*args, **kwargs):
    print('não nomeados:', args)
    for chave, valor in kwargs.items():
        print(chave, valor)

mostro_argumentos_nomeados(**pessoa_completa)