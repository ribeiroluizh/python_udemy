<<<<<<< HEAD
"""
Argumentos nomeados e não nomeados em funções python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

#definição da função
def soma(x, y, z):
    print (f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

#chamando a função
soma(1, 2, 3) #argumentos não nomeados
soma(y= 2, x= 1, z = 3) #argumentos nomeados
soma(2, z=1, y = 3) #argumentos nomeados a partir do segundo argumento, neste caso é obrigatório nomear todos os proximos argumentos

=======
"""
Argumentos nomeados e não nomeados em funções python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

#definição da função
def soma(x, y, z):
    print (f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

#chamando a função
soma(1, 2, 3) #argumentos não nomeados
soma(y= 2, x= 1, z = 3) #argumentos nomeados
soma(2, z=1, y = 3) #argumentos nomeados a partir do segundo argumento, neste caso é obrigatório nomear todos os proximos argumentos

>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
