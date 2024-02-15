# uma função que pode pausar

def generator (n=0, maximum = 10):
    while True:
        yield n

        n += 1
        if n > maximum:
            return 'Acabou'
    

gen = generator(maximum= 100)
# for n in gen:
#     print(n)


# Yield from
# possibilita dar continuidade de um genetator para outro generator (ex. gen2)
def gen1 ():
    yield 1
    yield 2
    yield 3

def gen2 ():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2(gen1)

for numero in g:
    print(numero)
