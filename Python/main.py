import pandas as pd
import matplotlib.pyplot as plt

# Leitura do arquivo
df = pd.read_csv("DesempenhoEconomico.csv")

# Função para limpar e converter os valores
def converter_valor(valor):
    valor = str(valor).replace(",", ".").replace("%", "").replace("p.p.", "").strip()
    try:
        return float(valor)
    except:
        return None

df["Crescimento_num"] = df["Crescimento"].apply(converter_valor)

# Estilo mais "financeiro"
plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(9,5))

# Linha principal
ax.plot(df["Indicador"], df["Crescimento_num"], 
        color="#003366", linewidth=2.2, marker="o", markersize=7, 
        markerfacecolor="#0055A4", markeredgecolor="black")

# Anotações de cada ponto
for i, valor in enumerate(df["Crescimento_num"]):
    ax.text(i, valor + 0.3, f"{valor:.1f}%", 
            ha="center", fontsize=9, color="black")

# Título e rótulos
ax.set_title("Crescimento Econômico - Lojas Renner", fontsize=15, fontweight="bold", color="#003366")
ax.set_ylabel("Crescimento (%)", fontsize=12)
ax.set_xlabel("Indicadores", fontsize=12)

# Ajuste do eixo X
ax.set_xticks(range(len(df["Indicador"])))
ax.set_xticklabels(df["Indicador"], rotation=30, ha="right")

# Grid suave
ax.grid(axis="y", linestyle="--", alpha=0.5)

# Bordas e fundo mais clean
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()
