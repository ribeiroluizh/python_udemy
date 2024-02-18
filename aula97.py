# variavels livres + nonlocal (locals, globals)

# def fora(x):
#     a = x

#     def dentro():
#         print(locals())
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor_final = string_inicial # uma variavel livre freevariable

    def interna(valor_a_concatenar=''):
        nonlocal valor_final # eu posso informar para o python que ela é nonlocal, 
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
c('bc')
c('de')
# print(c('b'))
# print(c('c'))
# print(c('d'))
final = c()
print(final)

