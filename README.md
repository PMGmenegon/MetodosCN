# 📐 MetodosCN

Implementações de métodos numéricos para encontrar raízes de funções, desenvolvidas como atividade prática da disciplina de **Cálculo Numérico** na UFPB.

---

## 📋 Sobre o Projeto

O repositório resolve um problema financeiro clássico: **calcular a taxa de juros mensal** de um financiamento de R$ 20.000,00 em 6 parcelas de R$ 4.000,00, modelado pela equação:

$$f(x) = 20000 \cdot \frac{x(1+x)^6}{(1+x)^6 - 1} - 4000 = 0$$

A taxa de juros (`x`) é procurada no intervalo **[0,05 ; 0,15]**, com critério de parada **ε = 0,05** e no máximo **3 iterações**, conforme especificação da questão.

---

## 🗂️ Estrutura do Repositório

```
MetodosCN/
├── metodos/
│   ├── metodobiseccao.py        # Método da Bisseção
│   ├── metodonewton.py          # Método de Newton-Raphson
│   └── metodosecante.py         # Método da Secante
│   └── metodofalsaposicao.py    # Método da Falsa Posição
├── QuestaoImplementada.png      # Enunciado da questão
└── README.md
```

---

## ⚙️ Métodos Implementados

### 🔹 Bisseção (`metodobiseccao.py`)
Divide o intervalo `[a, b]` ao meio iterativamente, verificando em qual subintervalo a raiz está garantida pelo **Teorema do Valor Intermediário (TVI)** (`f(a) · f(b) < 0`). O método retorna um intervalo de confiança para a taxa de juros.

### 🔹 Newton-Raphson (`metodonewton.py`)
Usa a tangente à curva no ponto atual para convergir à raiz. A derivada `f'(x)` é aproximada numericamente com diferença finita (`h = 0.0001`). O ponto inicial é `x₀ = 0.1` (ponto médio do intervalo).

### 🔹 Secante (`metodosecante.py`)
Similar ao Newton-Raphson, mas sem calcular derivadas — usa dois pontos anteriores para estimar a inclinação. Pontos iniciais: `x₀ = 0.05` e `x₁ = 0.15`.

### 🔹 Falsa Posição (`metodofalsaposicao.py`)
Similar à bisseção, mas em vez de usar o ponto médio do intervalo, traça uma reta entre os pontos (a,f(a)) e (b,f(b)). A interseção dessa reta com o eixo x é usada como nova aproximação da raiz.

Todos os scripts exibem o tempo de execução ao final.

---

## ▶️ Como Executar

**Pré-requisito:** Python 3.x instalado.

```bash
# Clone o repositório
git clone https://github.com/PMGmenegon/MetodosCN.git
cd MetodosCN

# Execute o método desejado
python metodos/metodobiseccao.py
python metodos/metodonewton.py
python metodos/metodosecante.py
python metodos/metodofalsaposicao.py
```

Nenhuma dependência externa é necessária — apenas a biblioteca padrão do Python (`math`, `time`).

---

## 👤 Autores

**edu-gouvea** -[GitHub](https://github.com/edu-gouvea)

**PMGmenegon** — [GitHub](https://github.com/PMGmenegon)

**RobertoHonoratoSF** - [GitHub](https://github.com/RobertoHonoratoSF)

---

## 📄 Licença

Distribuído sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
