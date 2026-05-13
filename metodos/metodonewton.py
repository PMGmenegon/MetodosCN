from time import time

inicio = time() # variável para calcular o tempo de execução

# a função absoluto retorna o valor absoluto de algum
# x dado como parâmetro.
def absoluto(x):
    if x < 0:
        return -x
    return x

# função dada pela questão já substituindo os valores dados
def f(x):
    return (20000 * ((x * ((1 + x)**6)) / (((1 + x)**6) - 1))) - 4000

# função para calcular a derivada da função
def derivada(x):
    h = 0.0001
    return (f(x + h) - f(x)) / h

xn = 0.1 # x0 será considerado como o ponto médio do intervalo [0.05, 0.15]
contador = 0 # contador para limitar as iterações
intMAX = 3 # limite de iterações dado pela questão
parada = 0.05 # parada dada pela questão

while contador < intMAX and absoluto(f(xn)) > parada:
    
    fx = f(xn)
    dfx = derivada(xn)

    print(f'xn = {xn:.5f} | f(xn) = {fx:.5f} | f\'(xn) = {dfx:.5f}')

    xn -= fx / dfx

    contador += 1

print(f'Taxa de juros = {xn:.5f}')

fim = time()

print(f'\nTempo de execução: {fim - inicio:.10f} segundos')
