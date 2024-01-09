"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo avançado e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados
Não temos acesso a nomes de escopos internos nos escopos externos
A palavra global faz uma variável do escopo externo ser a mesma no escopo interno
"""
x=1

def escopo ():
    x=130
    y = 2
    def outra_funcao():
        y = 20
        print(x, y)
        def terceira_funcao():
            global x
            y = 319
            x = 2913
            print(x, y)
            x = 1
        terceira_funcao()
    outra_funcao()
    print(x, y)
    

print (f'antes de chamar a função o {x=}')


escopo()
print(f'voltando para o global como fica o x? {x=}')
