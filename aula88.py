# Dictionary Comprehension e Set Comprehension

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

#por exemplo iterando em um dicionario usando o for

# for chave, valor in produto: # neste caso vai dar erro, pois estou tentando iterar 2 elementos sobre apenas um item.

# por isso, posso fazer da seguinte forma:

for chave, valor in produto.items(): # aqui consigo acessar tanto a chave e a valor.
    ...

# há outras formas também, chamando produto.values() - para acessar apenas os valores da chave 
# e produtos.keys() para acessar apenas as chaves.
#agora voltamos para list compreension
dc = {
    chave: valor #para pegar a chave e o valor do dicionario
    for chave, valor in produto.items() #pegando ambos os itens do dicionario
}

# Agora vamos inserir mapeamentos (alteração dos valores), no caso utilizando if a esquerda do for.

dc = {
    chave: valor.upper() #digamos que eu quero pegar todos os valores e alterar para letra maiuscula
    # neste caso, terei um problema pois um dos valores é float. por isso devemos tratar com um if.
    if isinstance(valor, str) #verifica se o valor é uma string
    else valor #caso não seja uma string, considere o valor
    for chave, valor in produto.items() #pegando ambos os itens do dicionario
    if chave == 'categoria' #eu também poderia filtrar para não incluir a chave de categoria 
    #detalhe que neste if é o inverso, pois estamos fazendo um filtro apenas para categoria
}

# imagine que tenho uma lista com tuplas, que parece um dicionario

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

#eu poderia criar um dicionário através disso

dc = {
    chave: valor
    for chave, valor in lista
}

##### agora vamos trabalhar o set comprehension #####

s1 = {i for i in range(10)}

