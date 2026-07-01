from lagrange import interpolacao_lagrange, polinomio_simbolico_lagrange

# Dados da tabela
anos = [1940, 1950, 1960, 1970, 1980]
populacao = [132.165, 151.326, 179.323, 203.302, 226.542]

# a) Estimar a população em 1965 com polinômio de grau 4 (5 pontos -> grau 4)
resultado_1965 = interpolacao_lagrange(anos, populacao, 1965)
print("a) Estimativa para 1965")
print(f"População estimada em 1965: {resultado_1965:.3f} milhões")

expr = polinomio_simbolico_lagrange(anos, populacao)
print(f"Polinômio interpolador: P(x) = {expr}\n")

# b) Precisão: comparar com o valor real de 1930 (extrapolação)
valor_real_1930 = 123.203
resultado_1930 = interpolacao_lagrange(anos, populacao, 1930)
erro_abs = abs(resultado_1930 - valor_real_1930)
erro_rel = erro_abs / valor_real_1930 * 100 

print("b) Precisão para 1930")
print(f"Valor calculado para 1930: {resultado_1930:.3f} milhões")
print(f"Valor real para 1930:      {valor_real_1930} milhões")
print(f"Erro absoluto: {erro_abs:.3f} milhões")
print(f"Erro relativo: {erro_rel:.2f}%")