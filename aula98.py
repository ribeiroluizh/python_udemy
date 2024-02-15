# Funções decoradoras e decoradores
# Decorar = Adicionar / remover / Restringir / Alterar
# Funções Decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (açúcar sintático)

def criar_funcao(func): # esta é a função decoradora, o trabalho dela é
# receber uma função, criar uma função 
    print('Vou te decorar')
    def interna(*args, **kwargs):

        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Agora voce foi decorada')
        
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def e_string(params):
    print(f'{e_string.__name__}')
    if not isinstance(params, str):
        raise TypeError ('Params devem ser uma string')


invertida = inverte_string("123")
print(invertida)