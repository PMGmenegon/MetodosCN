from lagrange import interpolacao_lagrange, polinomio_simbolico_lagrange

# Dados da tabela (Ano -> População em milhões)
anos = [1940, 1950, 1960, 1970, 1980]
populacao = [132.165, 151.326, 179.323, 203.302, 226.542]

# a) Estimar a população em 1965
ano_estimar = 1965
resultado = interpolacao_lagrange(anos, populacao, ano_estimar)
print('a) Estimar a população em 1965:\n')
print(f'Polinômio interpolador (forma expandida) : P(x) = {polinomio_simbolico_lagrange(anos, populacao)}\n')
print(f"População estimada em {ano_estimar}: {resultado:.3f} milhões")

# b) Comparar com o valor real de 1930 (para avaliar precisão -- extrapolação)
ano_real = 1930
valor_real = 123.203
resultado_1930 = interpolacao_lagrange(anos, populacao, ano_real)
erro = abs(resultado_1930 - valor_real)
erro_relativo = erro / valor_real * 100

print('b) Comparar com o valor real de 1930 (para avaliar precisão -- extrapolação)\n')
print(f"\nValor calculado para {ano_real}: {resultado_1930:.3f} milhões")
print(f"Valor real para {ano_real}: {valor_real} milhões")
print(f"Erro absoluto: {erro:.3f}")
print(f"Erro relativo: {erro_relativo:.2f}%")