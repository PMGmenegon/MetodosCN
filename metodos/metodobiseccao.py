from time import time
from math import log10

inicio = time() # variável para calcular o tempo de execução

# a função absoluto retorna o valor absoluto de algum
# x dado como parâmetro.
def absoluto(x):
    if x < 0:
        return -x
    return x

# a função f é a função modelada pelo problema 
# e que vai ser usada para calcular sua raíz
def f(x):
    return (20000 * ((x * ((1 + x)**6)) / (((1 + x)**6) - 1))) - 4000


a = 0.05
b = 0.15

fa = f(a)
fb = f(b)

parada = 0.05
contador = 1
itMAX = 3


# é feita essa verificação pois se o produto entre o
# f(a) e f(b) for maior do que 0 isso significa
# que o TVI não está garantido e logo não pode 
# aplicar o método
if fa * fb > 0:
    print('Erro! O intervalo não obedece ao TVI')

else:

    # um while True é feito, mas dentro dele existe a condição
    # de parada com um break, se o valor absoluto de f(x) for menor
    # que a parada definida como 0.05, o loop se encerra
    while True: 

        x = (a + b) / 2
        fx = f(x)

        print(f'xn = {x:.5f} | f(xn) = {fx:.5f}')

        if absoluto(fx) < parada or contador == itMAX:
            break

        if fa * fx < 0:
            b = x
            fb = fx
        if fb * fx < 0:
            a = x
            fa = fx
    
        contador += 1

print(f'O método da bisseção se limitou a dizer que a'
      f' taxa de juros está no intervalo de [{a:.5f},{x:.5f}]')
    
fim = time()

print(f'\nTempo de execução: {fim - inicio:.10f} segundos')
    