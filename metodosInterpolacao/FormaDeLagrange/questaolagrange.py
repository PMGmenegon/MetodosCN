from lagrange import interpolacao_lagrange, polinomio_simbolico_lagrange

# Dados completos da tabela
tempo_completo = [1, 3, 5, 7, 20]
vel_completo   = [800, 2310, 3090, 3940, 8000]

# a) Grau 3 -> usar 4 pontos mais próximos de t=10
# t=10 está entre 7 e 20, então descartamos t=1 (mais distante)
tempo = [3, 5, 7, 20]
vel   = [2310, 3090, 3940, 8000]

t_estimar = 10
resultado_grau3 = interpolacao_lagrange(tempo, vel, t_estimar)
expr = polinomio_simbolico_lagrange(tempo, vel)

print("a) Polinômio de grau 3 (pontos: 3, 5, 7, 20)")
print(f"Polinômio interpolador: P(t) = {expr}")
print(f"Velocidade estimada em t={t_estimar}s: {resultado_grau3:.4f} cm/s")

# b) Estimativa do erro: comparar com grau 4 (todos os 5 pontos)
resultado_grau4 = interpolacao_lagrange(tempo_completo, vel_completo, t_estimar)
erro = abs(resultado_grau4 - resultado_grau3)

print("\nb) Estimativa do erro")
print(f"Velocidade com grau 4 (todos os 5 pontos): {resultado_grau4:.4f} cm/s")
print(f"Erro estimado |grau4 - grau3|: {erro:.4f} cm/s")
print(f"Erro relativo: {erro/resultado_grau4*100:.2f}%")