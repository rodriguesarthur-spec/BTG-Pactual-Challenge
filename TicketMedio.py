import matplotlib.pyplot as plt
import numpy as np

anos = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
ticket_medio = [106, 113, 124, 133, 144, 155, 176, 191, 194, 189, 203]  # em R$
ipca_vestuario = [6.24, 8.30, 5.94, 0.22, 2.13, 1.79, -1.41, 5.41, 4.76, 1.30, 2.80]  # em %

variacao_ticket = [0]
for i in range(1, len(ticket_medio)):
    variacao = ((ticket_medio[i] - ticket_medio[i-1]) / ticket_medio[i-1]) * 100
    variacao_ticket.append(round(variacao, 1))

crescimento_total_ticket = ((ticket_medio[-1] - ticket_medio[0]) / ticket_medio[0]) * 100
inflacao_acumulada_setor = (np.prod([1 + i/100 for i in ipca_vestuario]) - 1) * 100
crescimento_real = crescimento_total_ticket - inflacao_acumulada_setor
cagr = ((ticket_medio[-1] / ticket_medio[0]) ** (1/10) - 1) * 100

plt.style.use("seaborn-v0_8-whitegrid")
color_ticket = "#003366"  
color_ipca = "#C99700"     
color_texto = "#222222"

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 11), gridspec_kw={"height_ratios": [2, 1]})

ax1.plot(anos, ticket_medio, color=color_ticket, marker='o', linewidth=3.5, 
         markersize=7, label="Ticket Médio (R$)")
ax1.set_ylabel("Ticket Médio (R$)", color=color_ticket, fontsize=13, fontweight="bold")
ax1.tick_params(axis="y", labelcolor=color_ticket)
ax1.set_ylim(90, 220)

for i, valor in enumerate(ticket_medio):
    ax1.annotate(f"R$ {valor}", (anos[i], ticket_medio[i]),
                 textcoords="offset points", xytext=(0, 8), ha="center",
                 fontsize=9, fontweight="bold", color=color_ticket)

ax1_ipca = ax1.twinx()
ax1_ipca.plot(anos, ipca_vestuario, color=color_ipca, marker='s', linestyle="--", 
              linewidth=2.5, markersize=6, label="IPCA Vestuário (%)")
ax1_ipca.set_ylabel("Inflação Vestuário (%)", color=color_ipca, fontsize=13, fontweight="bold")
ax1_ipca.tick_params(axis="y", labelcolor=color_ipca)
ax1_ipca.set_ylim(-5, 10)
ax1_ipca.axhline(y=0, color="gray", linestyle=":", alpha=0.5)

ax1.set_title("Evolução do Ticket Médio x Inflação do Vestuário (2014–2024)",
              fontsize=16, fontweight="bold", color=color_texto, pad=14)

largura = 0.38
ax2.bar([x - largura/2 for x in anos], variacao_ticket, width=largura, 
        color=color_ticket, alpha=0.85, label="Variação Ticket Médio (%)")
ax2.bar([x + largura/2 for x in anos], ipca_vestuario, width=largura, 
        color=color_ipca, alpha=0.85, label="IPCA Vestuário (%)")

ax2.set_xlabel("Ano", fontsize=12, fontweight="bold", color=color_texto)
ax2.set_ylabel("Variação Percentual (%)", fontsize=12, fontweight="bold", color=color_texto)
ax2.axhline(y=0, color="black", linewidth=0.8, alpha=0.6)
ax2.set_title("Variação Anual Comparativa", fontsize=14, fontweight="bold", color=color_texto, pad=10)

for i, (var_ticket, var_ipca) in enumerate(zip(variacao_ticket, ipca_vestuario)):
    if i > 0:
        ax2.text(anos[i] - largura/2, var_ticket + 0.6, f"{var_ticket}%", 
                 ha="center", fontsize=8, fontweight="bold", color=color_ticket)
        ax2.text(anos[i] + largura/2, var_ipca + 0.6, f"{var_ipca}%", 
                 ha="center", fontsize=8, fontweight="bold", color=color_ipca)

ax2.legend(loc="upper left", fontsize=10, frameon=False)

plt.figtext(0.05, 0.01, 
            f"Fontes: Lojas Renner (Relatórios Anuais) • IBGE (SIDRA – Tabela 7060)\n"
            f"Crescimento Total: +{crescimento_total_ticket:.1f}% • "
            f"CAGR: {cagr:.1f}% a.a. • "
            f"Inflação Acumulada Vestuário: +{inflacao_acumulada_setor:.1f}% • "
            f"Crescimento Real: +{crescimento_real:.1f}%", 
            fontsize=9.5, style="italic", color="gray")

plt.tight_layout()
plt.show()
