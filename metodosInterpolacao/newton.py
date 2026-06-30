"""
Interpolação Polinomial - Forma de Newton (Diferenças Divididas)
Cálculo Numérico

A forma de Newton constrói o polinômio interpolador usando diferenças
divididas, na seguinte forma encaixada (estilo Horner):

    P(x) = f[x0] + (x - x0)*f[x0,x1] + (x - x0)(x - x1)*f[x0,x1,x2] + ...

onde f[x0, x1, ..., xk] são as diferenças divididas, calculadas
recursivamente por:

    f[x_i] = y_i
    f[x_i, ..., x_{i+k}] = (f[x_{i+1}, ..., x_{i+k}] - f[x_i, ..., x_{i+k-1}])
                            / (x_{i+k} - x_i)

A principal vantagem da forma de Newton é que, ao adicionar um novo ponto
à tabela, não é necessário recalcular o polinômio inteiro: basta acrescentar
um novo termo.
"""


def diferencas_divididas(pontos_x, pontos_y):
    """
    Monta a tabela de diferenças divididas e retorna os coeficientes
    f[x0], f[x0,x1], f[x0,x1,x2], ... usados no polinômio de Newton.

    Parâmetros:
        pontos_x (list[float]): abscissas dos pontos conhecidos
        pontos_y (list[float]): ordenadas dos pontos conhecidos

    Retorna:
        list[float]: coeficientes do polinômio de Newton (uma diferença
                      dividida por nível, começando em f[x0])
    """
    if len(pontos_x) != len(pontos_y):
        raise ValueError("As listas pontos_x e pontos_y devem ter o mesmo tamanho.")

    if len(set(pontos_x)) != len(pontos_x):
        raise ValueError("Os valores de x não podem se repetir (divisão por zero).")

    n = len(pontos_x)
    # tabela[k][i] guarda a diferença dividida f[x_i, ..., x_{i+k}]
    tabela = [[0.0] * n for _ in range(n)]

    # Nível 0: a própria função (y)
    for i in range(n):
        tabela[0][i] = pontos_y[i]

    # Níveis seguintes: diferenças divididas progressivas
    for k in range(1, n):
        for i in range(n - k):
            tabela[k][i] = (tabela[k - 1][i + 1] - tabela[k - 1][i]) / \
                           (pontos_x[i + k] - pontos_x[i])

    # Os coeficientes do polinômio são a primeira linha de cada nível: tabela[k][0]
    coeficientes = [tabela[k][0] for k in range(n)]
    return coeficientes


def interpolacao_newton(pontos_x, pontos_y, x):
    """
    Calcula o valor interpolado P(x) usando a forma de Newton com
    diferenças divididas, avaliando o polinômio no formato de Horner.

    Parâmetros:
        pontos_x (list[float]): abscissas dos pontos conhecidos
        pontos_y (list[float]): ordenadas dos pontos conhecidos
        x (float): ponto onde se deseja estimar o valor interpolado

    Retorna:
        float: valor de P(x), o polinômio interpolador avaliado em x
    """
    coeficientes = diferencas_divididas(pontos_x, pontos_y)
    n = len(coeficientes)

    # Avaliação no formato de Horner (de trás para frente)
    resultado = coeficientes[n - 1]
    for k in range(n - 2, -1, -1):
        resultado = resultado * (x - pontos_x[k]) + coeficientes[k]

    return resultado


def polinomio_simbolico_newton(pontos_x, pontos_y):
    """
    (Opcional) Monta uma representação simbólica do polinômio interpolador
    de Newton usando a biblioteca sympy, útil para visualizar a expressão
    final expandida em termos de x.

    Parâmetros:
        pontos_x (list[float]): abscissas dos pontos conhecidos
        pontos_y (list[float]): ordenadas dos pontos conhecidos

    Retorna:
        sympy.Expr: expressão simbólica do polinômio interpolador, expandida
    """
    import sympy as sp

    x = sp.symbols('x')
    coeficientes = diferencas_divididas(pontos_x, pontos_y)
    n = len(coeficientes)

    polinomio = coeficientes[0]
    produto_acumulado = 1
    for k in range(1, n):
        produto_acumulado *= (x - pontos_x[k - 1])
        polinomio += coeficientes[k] * produto_acumulado

    return sp.expand(polinomio)


if __name__ == "__main__":
    # Exemplo de uso (mesma tabela usada no arquivo lagrange.py, para comparação)
    pontos_x = [1, 2, 4, 5]
    pontos_y = [0, 1, 1.386294, 1.609438]  # aproximações de ln(x)

    x_avaliar = 3

    coeficientes = diferencas_divididas(pontos_x, pontos_y)
    resultado = interpolacao_newton(pontos_x, pontos_y, x_avaliar)

    print(f"Pontos conhecidos: x = {pontos_x}, y = {pontos_y}")
    print(f"Coeficientes (diferenças divididas): {coeficientes}")
    print(f"P({x_avaliar}) = {resultado:.6f}")

    # Caso queira ver o polinômio expandido (requer sympy instalado)
    try:
        expr = polinomio_simbolico_newton(pontos_x, pontos_y)
        print(f"Polinômio interpolador (forma expandida): P(x) = {expr}")
    except ImportError:
        print("Instale a biblioteca 'sympy' para visualizar o polinômio simbólico.")