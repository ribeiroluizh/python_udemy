<<<<<<< HEAD
# Exercício - sistema de Perguntas e respostas


print('Olá, vamos jogar!')
print()

questoes = [
    {
        'Questão': 'Quanto é 2+2?',
        'Opções':['1','3','4','5'],
        'Resposta':'4',
    },
    {
        'Questão': 'Quanto é 5*5?',
        'Opções':['25','33','10','100'],
        'Resposta':'25',
    },
    {
        'Questão': 'Quanto é 10 / 2?',
        'Opções':['8','12','20','5'],
        'Resposta':'5',
    },
]

qtd_acertos = 0 
for questao in questoes:
    print(questao['Questão'])
    print()

    opcoes = questao['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == questao['Resposta']:
                acertou = True
    
    print()
    if acertou:
        print('Acertou 💥 ')
        qtd_acertos += 1
    else: 
        print('Errou ❌ ')

    
    print()

print('Você acertou', qtd_acertos)
=======
# Exercício - sistema de Perguntas e respostas


print('Olá, vamos jogar!')
print()

questoes = [
    {
        'Questão': 'Quanto é 2+2?',
        'Opções':['1','3','4','5'],
        'Resposta':'4',
    },
    {
        'Questão': 'Quanto é 5*5?',
        'Opções':['25','33','10','100'],
        'Resposta':'25',
    },
    {
        'Questão': 'Quanto é 10 / 2?',
        'Opções':['8','12','20','5'],
        'Resposta':'5',
    },
]

qtd_acertos = 0 
for questao in questoes:
    print(questao['Questão'])
    print()

    opcoes = questao['Opções']

    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')
    
    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)
    
    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == questao['Resposta']:
                acertou = True
    
    print()
    if acertou:
        print('Acertou 💥 ')
        qtd_acertos += 1
    else: 
        print('Errou ❌ ')

    
    print()

print('Você acertou', qtd_acertos)
>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
print('de', len(questoes), 'questões')