from newton import diferencas_divididas, interpolacao_newton, polinomio_simbolico_newton

# Dados da tabela
anos = [1940, 1950, 1960, 1970, 1980]
populacao = [132.165, 151.326, 179.323, 203.302, 226.542]

# Tabela de diferenças divididas
coeficientes = diferencas_divididas(anos, populacao)
print("=== Tabela de diferenças divididas ===")
for i, c in enumerate(coeficientes):
    print(f"  f[x0..x{i}] = {c}")

# a) Polinômio de grau 4 (5 pontos) -> estimar 1965
resultado_1965 = interpolacao_newton(anos, populacao, 1965)
expr = polinomio_simbolico_newton(anos, populacao)
print(f"\na) Estimativa para 1965")
print(f"Polinômio interpolador: P(x) = {expr}")
print(f"População estimada em 1965: {resultado_1965:.3f} milhões")

# b) Precisão: comparar com o valor real de 1930 (extrapolação)
valor_real_1930 = 123.203
resultado_1930 = interpolacao_newton(anos, populacao, 1930)
erro_abs = abs(resultado_1930 - valor_real_1930)
erro_rel = erro_abs / valor_real_1930 * 100

print(f"\nb) Precisão para 1930")
print(f"Valor calculado para 1930: {resultado_1930:.3f} milhões")
print(f"Valor real para 1930: {valor_real_1930} milhões")
print(f"Erro absoluto: {erro_abs:.3f} milhões")
print(f"Erro relativo: {erro_rel:.2f}%")