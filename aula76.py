''' 
Dicionários em Python (tipo dict)
Dicionários são estruturas de dados do tipo par de 'chave' e 'valor'.
Chaves podem ser consideradas como 'indice' que vimos na lista e podem ser de tipos imutáveis
como: str, int, float, bool, tuple, etc..
O valor pode ser de qualquer tipo, incluindo outro dicionário.
usamos as chaves - {} -  ou a classe dict para criar dicionários.
Imutáveis: str, int, float, bool, tuple
mutável: dict, list.
pessoa = {
    'nome': 'Luiz otávio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.7,
    'endereços': [
        {'rua': 'tal tal', 'numero': 123},
        {'rua': 'outra rua', 'numero': 321},
    ]
}
print(pessoa, type(pessoa))
pessoa = dict(nome='Luiz Otavio', sobrenome='Miranda')
'''



# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
p1 = {
    'nome': 'Luiz',
    'sobrenome': 'Miranda',
}
# print(p1['nome'])
# print(p1.get('nome', 'Não existe'))

# nome = p1.pop('nome')
# print(nome)
# print(p1)
# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)
# p1.update({
#     'nome': 'novo valor',
#     'idade': 30,
# })
# p1.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))

print(p1)

p1.update(nome='Novo valor')

print(p1)