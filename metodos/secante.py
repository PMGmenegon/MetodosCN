def f(x):
    return 20000 * ((x * (1+x)**6) / ((1+x)**6 - 1)) - 4000
def secante(f, x0=0.05, x1=0.15):
    for c in range(0,3):
        x2 = x1 - (f(x1)*(x1 - x0)) / (f(x1) - f(x0))
        print(x2)
        if abs(x2 - x1) < 0.05:
            break
        x0 = x1
        x1 = x2
    print(f'Juros é {x2}')
secante(f)