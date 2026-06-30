from newton import diferencas_divididas, interpolacao_newton

# Dados completos da tabela
tempo_completo = [1, 3, 5, 7, 20]
vel_completo = [800, 2310, 3090, 3940, 8000]

# a) Polinômio de grau 3 -> usar 4 pontos (os mais próximos de t=10)
# t=10 está entre 7 e 20, então os 4 pontos mais próximos são: 3, 5, 7, 20

t_estimar = 10
coeficientes = diferencas_divididas(tempo_completo, vel_completo)
resultado_grau3 = interpolacao_newton(tempo_completo, vel_completo, t_estimar)

print("a) Polinômio de grau 3 (4 pontos: 3, 5, 7, 20)")
print(f"Coeficientes (diferenças divididas): {coeficientes}")
print(f"Velocidade estimada em t={t_estimar}s: {resultado_grau3:.4f} cm/s")

# b) Erro: comparar com o polinômio de grau 4 (usando todos os 5 pontos)
resultado_grau4 = interpolacao_newton(tempo_completo, vel_completo, t_estimar)
erro_estimado = abs(resultado_grau4 - resultado_grau3)

print("\nb) Estimativa do erro")
print(f"Velocidade com polinômio de grau 4 (todos os 5 pontos): {resultado_grau4:.4f} cm/s")
print(f"Erro estimado |grau4 - grau3|: {erro_estimado:.4f} cm/s")