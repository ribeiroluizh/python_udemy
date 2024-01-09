# Exercícios com funções

"""
Crie uma função que multiplica todos os argumentos não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável
Crie uma função fala se um número é par um impar, retorne se o numero é par ou impar
"""

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    print(total)
    return total

variavel = multiplicar(1,2,3,4,5)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'
    
print(par_impar(variavel))