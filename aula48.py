lista_a = ['Luiz', 'Maria']

lista_b = lista_a.copy() #salva o valor, copia o valor da lista A, no caso a lista B ficará com o valor anterior da lista A gravado

salva_valor = lista_a[0] # aqui eu salvei o valor do primeiro indice da lista A numa variável
lista_a [0] = 'Fernando' # aqui eu alterei o indice 0 da lista A

lista_a.append(salva_valor) #aqui eu inseri na lista A o valor que eu havia alterado no codigo anterior/
# e salvei numa variavel antes de fazer essa alteração
print(lista_a)
print(lista_b)
print(salva_valor)