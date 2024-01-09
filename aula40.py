while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*): ')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0


    try: 
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print ('Um ou ambos os números são inválidos')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print ('Operador Inválido')
        continue

    if len(operador) > 1:
        print ('Digite apenas um operador')
        continue

    if operador == '+':
        res_soma = num_1_float + num_2_float
        print (f'O resultado de {numero_1} + {numero_2} é igual a {res_soma:.2f}')
    elif operador == '-':
        res_sub = num_1_float - num_2_float
        print (f'O resultado de {numero_1} - {numero_2} é igual a {res_sub:.2f}')
    elif operador == '*':
        res_vez = num_1_float * num_2_float
        print (f'O resultado de {numero_1} * {numero_2} é igual a {res_vez:.2f}')
    elif operador == '/':
        res_div = num_1_float / num_2_float
        print (f'O resultado de {numero_1} / {numero_2} é igual a {res_div:.2f}')
    
    else:
        print ('nunca deveria chegar aqui')



    sair = input ('Quer Sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break