import os

lista = []
while True:
    print('Seleciona uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        produto = input('Insira um produto: ')
        lista.append(produto)
        print ('produto inserido com sucesso')

    elif opcao == 'a':
        os.system('cls')
        apaga_produto = input('Qual item você deseja apagar? : ')

        try: 
            indice = int(apaga_produto)
            del lista[indice]
            print('produto apagado com sucesso')
        except ValueError:
            print ('Por favor, digite o código do item')
        except IndexError:
            print ('Este item não existe')
        except Exception:
            print ('Erro desconhecido')
    
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')
            
        for indice, nome in enumerate(lista):
            print (indice, nome)
    
    else:
        print ('Por favor, escolha uma opção i, a ou l')