<<<<<<< HEAD
""" texto = "Python"

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto) """

texto = 'Luiz' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
for letra in texto:
=======
""" texto = "Python"

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto) """

texto = 'Luiz' #iterável
iterador = iter(texto) #iterador

while True:
    try:
        print(next(iterador))
    except StopIteration:
        break
for letra in texto:
>>>>>>> e0f4e53 (Inserindo o restante das aulas que fiz até hoje)
    print(letra)