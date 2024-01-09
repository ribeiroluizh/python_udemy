import datetime
from dateutil import parser

print ('primeiro programa')
numerouser = input('Digite um número: ')

if numerouser.isdigit():
    numerouser_int = int(numerouser)
    if (numerouser_int%2 == 0):
        print(f'O número {numerouser} é par')
    else:
        print(f'O número {numerouser} é impar')
else:
    print('Você precisa digitar um numero inteiro.')

print ('segundo programa')
try:
    hora_str = input("Digite a hora atual: ")
    hora_atual = parser.parse(hora_str).hour

    if hora_atual >= 0 and hora_atual < 12:
        print("Bom dia!")
    elif hora_atual >= 12 and hora_atual < 18:
        print("Boa tarde!")
    elif hora_atual >= 18 and hora_atual <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida. Digite um número entre 0 e 23.")
except ValueError:
    print("Entrada inválida. Digite a hora no formato correto.")

print ('terceiro programa')

nome = input ('digite seu nome: ')
qtd_letras = len(nome)

if qtd_letras <= 4:
    print ('seu nome é curto')
if qtd_letras ==5 or qtd_letras ==6:
    print ('seu nome é normal')
else:
    print ('seu nome é muito grande')