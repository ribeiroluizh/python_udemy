<<<<<<< HEAD
cpf = input('Digite um CPF: ')
#resultado digito 1
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0

#resultado digito 2
dez_digitos = cpf[:10]
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int (digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0

# validador
if (str(digito_1) == cpf[-2]) and (str(digito_2) == cpf[-1]):
    print ('É um CPF válido')
else:
=======
cpf = input('Digite um CPF: ')
#resultado digito 1
nove_digitos = cpf[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <=9 else 0

#resultado digito 2
dez_digitos = cpf[:10]
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int (digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <=9 else 0

# validador
if (str(digito_1) == cpf[-2]) and (str(digito_2) == cpf[-1]):
    print ('É um CPF válido')
else:
>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
    print ('É um CPF inválido')