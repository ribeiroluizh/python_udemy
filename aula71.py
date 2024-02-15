<<<<<<< HEAD
"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#Lembre-te de desempacotamento

x, y, *_ = 1, 2, 3, 4
print (x, y, _)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

soma_1_2_3 = soma(1,2,3)

=======
"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
#Lembre-te de desempacotamento

x, y, *_ = 1, 2, 3, 4
print (x, y, _)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

soma_1_2_3 = soma(1,2,3)

>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
print(soma_1_2_3)