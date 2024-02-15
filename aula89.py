# isinstance para saber se objeto é de um determinado tipo

lista = [
    'a', 1, 1.1, True, [0,1,2,3], (1,2),
    {0,1}, {'nome': 'Luiz'}
] #aqui tenho uma lista com diversos tipos de dados diferentes

# é importante sempre procurar utilizar dentro de uma estrutura de dados (listas, tuplas, etc) o mesmo tipo de 
#dado, por exemplo, procure sempre criar uma lista de numeros e inserir nesta lista apenas numeros, não string, etc.. 

#porém para verificar o tipo do objeto de uma lista, é possível utilizar o método isinstance

for item in lista:
    #isinstance significa: esta checando se alguma coisa é uma instancia daquela classe
    if isinstance(item, set):
        print('SET')
        item.add(5)
        #print(item, isinstance(item, set)) #checando qual é o objeto da classe set

    #também é muito comum verificar se um item é numero, 
    if isinstance(item, (int, float)): # neste caso, devemos usar um () para definir mais de um tipo de verificação
        print('NUM')
        print(item, item * 2)



