def executa (funcao, *args):
    return funcao(*args)

def soma (x, y):
    return x + y

def cria_multiplicador (multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n*m,
    2
)

print(duplica(5))

print(
    executa(
        lambda x, y: x + y,
        2, 4
    ),
)

print(
    executa(
        lambda *args: sum(args),
        1, 3
    )
)