<<<<<<< HEAD
"""
Valores padrão para parâmetros
Ao definir uma função, os parametros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor será usado.
Refatorar: editar o seu código.
"""

def soma (x, y, z=None): #aqui também se eu defini no parametro Z um algumento, os proximos parametros também deverão ter argumentos.
    if z is not None:
        print (f'{x=} {y=} {z=}', '|', x+y+z)
    else:
        print (f'{x=} {y=}', '|', x+y)

soma(1,2)
soma(3,5)
soma(100,200)
=======
"""
Valores padrão para parâmetros
Ao definir uma função, os parametros podem ter valores padrão. Caso o valor não seja enviado para o parâmetro, o valor será usado.
Refatorar: editar o seu código.
"""

def soma (x, y, z=None): #aqui também se eu defini no parametro Z um algumento, os proximos parametros também deverão ter argumentos.
    if z is not None:
        print (f'{x=} {y=} {z=}', '|', x+y+z)
    else:
        print (f'{x=} {y=}', '|', x+y)

soma(1,2)
soma(3,5)
soma(100,200)
>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
soma(7, 9, 0)