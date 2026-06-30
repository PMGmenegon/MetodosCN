"""
Interpolação Polinomial - Forma de Lagrange
Cálculo Numérico

A forma de Lagrange constrói o polinômio interpolador como uma combinação
linear de polinômios de base L_i(x), de modo que:

    P(x) = sum_{i=0}^{n} y_i * L_i(x)

onde cada polinômio de base é definido por:

    L_i(x) = produto_{j=0, j!=i}^{n} (x - x_j) / (x_i - x_j)

Cada L_i(x) vale 1 em x_i e 0 nos demais pontos x_j (j != i), garantindo
que P(x_i) = y_i para todos os pontos da tabela.
"""

def lagrange_base(i, x, pontos_x):
    """
    Calcula o valor do i-ésimo polinômio de base de Lagrange L_i(x).

    Parâmetros:
        i (int): índice do ponto base
        x (float): ponto onde o polinômio de base será avaliado
        pontos_x (list[float]): lista com as abscissas (x_0, x_1, ..., x_n)

    Retorna:
        float: valor de L_i(x)
    """
    n = len(pontos_x)
    resultado = 1.0
    for j in range(n):
        if j != i:
            resultado *= (x - pontos_x[j]) / (pontos_x[i] - pontos_x[j])
    return resultado


def interpolacao_lagrange(pontos_x, pontos_y, x):
    """
    Calcula o valor interpolado P(x) usando a forma de Lagrange.

    Parâmetros:
        pontos_x (list[float]): abscissas dos pontos conhecidos
        pontos_y (list[float]): ordenadas dos pontos conhecidos
        x (float): ponto onde se deseja estimar o valor interpolado

    Retorna:
        float: valor de P(x), o polinômio interpolador avaliado em x
    """
    if len(pontos_x) != len(pontos_y):
        raise ValueError("As listas pontos_x e pontos_y devem ter o mesmo tamanho.")

    if len(set(pontos_x)) != len(pontos_x):
        raise ValueError("Os valores de x não podem se repetir (divisão por zero).")

    n = len(pontos_x)
    soma = 0.0
    for i in range(n):
        soma += pontos_y[i] * lagrange_base(i, x, pontos_x)
    return soma


def polinomio_simbolico_lagrange(pontos_x, pontos_y):
    """
    (Opcional) Monta uma representação simbólica do polinômio interpolador
    usando a biblioteca sympy, útil para visualizar a expressão final
    expandida em termos de x.

    Parâmetros:
        pontos_x (list[float]): abscissas dos pontos conhecidos
        pontos_y (list[float]): ordenadas dos pontos conhecidos

    Retorna:
        sympy.Expr: expressão simbólica do polinômio interpolador, expandida
    """
    import sympy as sp

    x = sp.symbols('x')
    n = len(pontos_x)
    polinomio = 0
    for i in range(n):
        termo = 1
        for j in range(n):
            if j != i:
                termo *= (x - pontos_x[j]) / (pontos_x[i] - pontos_x[j])
        polinomio += pontos_y[i] * termo
    return sp.expand(polinomio)


if __name__ == "__main__":
    # Exemplo de uso
    # Tabela de pontos conhecidos (x, y)
    pontos_x = [1, 2, 4, 5]
    pontos_y = [0, 1, 1.386294, 1.609438]  # aproximações de ln(x)

    x_avaliar = 3

    resultado = interpolacao_lagrange(pontos_x, pontos_y, x_avaliar)
    print(f"Pontos conhecidos: x = {pontos_x}, y = {pontos_y}")
    print(f"P({x_avaliar}) = {resultado:.6f}")

    # Caso queira ver o polinômio expandido (requer sympy instalado)
    try:
        expr = polinomio_simbolico_lagrange(pontos_x, pontos_y)
        print(f"Polinômio interpolador (forma expandida): P(x) = {expr}")
    except ImportError:
        print("Instale a biblioteca 'sympy' para visualizar o polinômio simbólico.")