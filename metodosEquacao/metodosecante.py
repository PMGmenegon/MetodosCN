from time import time

inicio = time() # variável para calcular o tempo de execução

# função dada pela questão com valores já substituídos
def f(x):
    return 20000 * ((x * (1+x)**6) / ((1+x)**6 - 1)) - 4000

# função que implementa o método da secante,
# que respeita o limite de iterações dada pela
# questão e utiliza o intervalo [0.05, 0.15] também dado.
def secante(f, x0=0.05, x1=0.15):
    for c in range(0,3):
        x2 = x1 - (f(x1)*(x1 - x0)) / (f(x1) - f(x0))
        print(f'xn = {x2:.5f}')
        if abs(x2 - x1) < 0.05:
            break
        x0 = x1
        x1 = x2
    print(f'Taxa de juros = {x2:.5f}')

secante(f)

fim = time()

print(f'\nTempo de execução: {fim - inicio:.10f} segundos')