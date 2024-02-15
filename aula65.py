<<<<<<< HEAD
'''Introdução às funções (def) em Python
Funções são trechos de códigos usados para replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
Por padrão, funções Python retornam None (nada)'''

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}?', end = ' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
=======
'''Introdução às funções (def) em Python
Funções são trechos de códigos usados para replicar determinada ação ao longo do seu código
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico
Por padrão, funções Python retornam None (nada)'''

def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é multiplo de {multiplo}?', end = ' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
multiplo_de(10, 2)