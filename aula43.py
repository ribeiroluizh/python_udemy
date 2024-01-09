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
    print(letra)