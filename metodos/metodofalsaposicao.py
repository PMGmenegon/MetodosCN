from time import time

inicio=time()

#função que retorna um valor absoluto a ser comparado com a condição de parada
def absoluto(x):
     if x<0:
          return x*-1
     else:
          return x

#função dada no problema usada para calcular a raiz
def f(x):
    return (20000 * ((x * ((1 + x)**6)) / (((1 + x)**6) - 1))) - 4000
    

a=0.05
b=0.15

fa=f(a)
fb=f(b)

parada = 0.05
contador = 1
itMAX = 3


# é feita essa verificação pois se o produto entre o
# f(a) e f(b) for maior do que 0 isso significa
# que não existe garantia da existência de uma raiz
# no intervalo e o método não pode ser implementado
if fa * fb > 0:
    print('Erro!')

else:
    # um while True é feito, mas dentro dele existe a condição
    # de parada com um break, se o valor absoluto de f(x) for menor
    # que a parada definida como 0.05, o loop se encerra
    while True:
            x=((a*fb)-(b*fa))/(fb-fa)
            fx=f(x)
            print(f'xn = {x:.5f} | f(xn) = {fx:.5f}')
            if absoluto(fx) < parada or contador == itMAX:
                break
            if fa * fx < 0:
                b = x
                fb = fx
            elif fb * fx < 0:
                a = x
                fa = fx
            contador += 1
    
print(f'O método da Falsa Posição se limitou a dizer que a'
      f' taxa de juros está no intervalo de [{a:.5f},{b:.5f}]')
    
fim = time()

print(f'\nTempo de execução: {fim - inicio:.10f} segundos')
    