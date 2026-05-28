import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --- Configuração Estética Global ---
plt.style.use('default')
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams['font.family'] = 'DejaVu Sans'

# --- Dados ---
anos = [2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
ticket_medio = [106, 113, 124, 133, 144, 155, 176, 191, 194, 189, 203]
ipca_vestuario = [6.24, 8.30, 5.94, 0.22, 2.13, 1.79, -1.41, 5.41, 4.76, 1.30, 2.80]

# --- Criando Figura ---
fig, ax1 = plt.subplots(figsize=(14, 8))
fig.patch.set_facecolor('white')
ax1.set_facecolor('white')

# --- Paleta ---
cor_ticket = '#1F77B4'
cor_ipca = '#7F7F7F'
cor_texto = '#222222'

# --- Plot Ticket Médio (Eixo Esquerdo) ---
ax1.plot(anos, ticket_medio, color=cor_ticket, linewidth=3, marker='o',
         markersize=7, markerfacecolor='white', markeredgewidth=2,
         label='Ticket Médio (R$)', zorder=5)

for ano, valor in zip(anos, ticket_medio):
    ax1.text(ano, valor + 4, f'R$ {valor}', ha='center', va='bottom',
             fontsize=10, color=cor_ticket, fontweight='semibold')

ax1.set_ylabel('Ticket Médio (R$)', fontsize=13, color=cor_texto, labelpad=12)
ax1.tick_params(axis='y', labelcolor=cor_texto, labelsize=11)
ax1.tick_params(axis='x', labelcolor=cor_texto, labelsize=11)
ax1.set_ylim(90, 220)
ax1.set_xlim(2013.5, 2024.5)

# --- Plot IPCA Vestuário (Eixo Direito) ---
ax2 = ax1.twinx()
ax2.plot(anos, ipca_vestuario, color=cor_ipca, linewidth=2.2, linestyle='--',
         marker='D', markersize=6, markerfacecolor='white', markeredgewidth=1.5,
         label='IPCA Vestuário (%)', zorder=4)

ax2.set_ylabel('Variação IPCA Vestuário (%)', fontsize=13, color=cor_texto, labelpad=12)
ax2.tick_params(axis='y', labelcolor=cor_texto, labelsize=11)
ax2.set_ylim(-5, 10)

ax2.axhline(y=0, color='#BBBBBB', linestyle=':', linewidth=1)

# --- Título e Subtítulo ---
fig.suptitle("Ticket Médio da Lojas Renner: Crescimento Real Acima da Inflação do Setor",
             fontsize=18, fontweight='bold', color=cor_texto, ha='left', x=0.1, y=0.97)
ax1.set_title("Evolução do ticket médio X variação do IPCA do vestuário (2014-2024)",
              fontsize=14, color='#555555', loc='left', pad=12, style='italic')


# --- LEGENDA (MODIFICADA PARA FICAR FORA DO GRÁFICO) ---
# Coletamos as informações das duas linhas
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
# Criamos uma legenda a nível da "figura" (fig) em vez do "eixo" (ax1)
# bbox_to_anchor=(0.5, 0.89) -> posiciona a legenda centralizada horizontalmente (0.5) e logo abaixo do título (0.89)
# ncol=2 -> coloca os itens lado a lado
fig.legend(lines1 + lines2, labels1 + labels2, loc='upper center',
           bbox_to_anchor=(0.5, 0.89), ncol=2, fontsize=11, frameon=False)


# --- Layout Minimalista ---
for spine in ['top', 'right']:
    ax1.spines[spine].set_visible(False)
    ax2.spines[spine].set_visible(False)
ax1.spines['left'].set_color('#DDDDDD')
ax1.spines['bottom'].set_color('#DDDDDD')
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)

ax1.yaxis.grid(True, linestyle='--', linewidth=0.6, color='#DDDDDD', alpha=0.7)
ax1.xaxis.grid(False)
ax2.grid(False)

# --- Estatísticas ---
crescimento_total = ((ticket_medio[-1] - ticket_medio[0]) / ticket_medio[0]) * 100
inflacao_acumulada = np.prod([1 + i/100 for i in ipca_vestuario]) - 1
stats_text = f'Crescimento do Ticket: +{crescimento_total:.1f}%   |   Inflação acumulada no setor: +{inflacao_acumulada*100:.1f}%'

plt.figtext(0.125, 0.06, stats_text,
            fontsize=12, fontweight='semibold', color=cor_texto)

# --- Fonte ---
plt.figtext(0.125, 0.025, 'Fontes: Lojas Renner (Relatórios Anuais) • IBGE/SIDRA Tabela 7060',
            fontsize=9.5, style='italic', color='#777777')

# --- Ajuste Final ---
# O rect foi ajustado para garantir que o título e a legenda não se sobreponham
plt.tight_layout(rect=[0, 0.08, 1, 0.92])
plt.show()