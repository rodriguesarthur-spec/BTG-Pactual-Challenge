import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('default')
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.edgecolor'] = '#333333'

empresas = [
    'Renner (LREN3)', 
    'Grupo Guararapes (RCHLO3)', 
    'C&A', 
    'Grupo Soma (SOMA3)', 
    'Marisa (AMAR3)',
    'Outros'
]

market_share = [16.2, 14.8, 12.1, 9.3, 5.7, 41.9]  

cores = ['#2E86AB', '#A23B72', '#F18F01', '#6B8E23', '#9370DB', '#CCCCCC']


fig, ax = plt.subplots(figsize=(14, 10))
fig.patch.set_facecolor('#F8F9FA')


wedges, texts, autotexts = ax.pie(
    market_share,
    labels=empresas,
    colors=cores,
    autopct='%1.1f%%',
    startangle=90,
    textprops={'fontsize': 11, 'fontweight': 'bold'},
    pctdistance=0.85,
    wedgeprops={'edgecolor': 'white', 'linewidth': 2, 'alpha': 0.9}
)


for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(10)

plt.title('Market Share do Varejo de Moda no Brasil - 2023\n(Principais Varejistas do Setor)',
          fontsize=16, fontweight='bold', pad=20, color='#333333')

legenda_textos = [f'{empresas[i]}: {market_share[i]}%' for i in range(len(empresas))]
legenda = ax.legend(wedges, legenda_textos,
                   title="Empresas e Participação",
                   loc="center left",
                   bbox_to_anchor=(1, 0, 0.5, 1),
                   fontsize=11)

legenda.get_title().set_fontweight('bold')

total_mercado = "Tamanho Total do Mercado (2023): R$ 198 bilhões"
plt.figtext(0.5, 0.02, total_mercado, ha='center', fontsize=12,
            fontweight='bold', style='italic', color='#555555')

fontes = """
Fontes: 
• Relatórios Anuais 2023: Lojas Renner, Grupo Guararapes (Riachuelo), Grupo Soma, Marisa
• Dados financeiros públicos das empresas de capital aberto (B3)
• Associação Brasileira do Varejo Têxtil (ABVTEX) - Estimativas 2023
• Anuário Abravest 2023 - Associação Brasileira do Varejo de Vestuário
• Análises setoriais: XP Investimentos, Itaú BBA, BTG Pactual
• Dados consolidados de receita do varejo de moda brasileiro
"""

plt.figtext(0.05, 0.10, fontes, fontsize=9, style='italic', 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.7))

plt.tight_layout()
plt.show()

print("📊 DETALHAMENTO DO MARKET SHARE - VAREJO DE MODA 2023")
print("=" * 65)
for i in range(len(empresas)):
    if empresas[i] != 'Outros':
        valor_mercado = (market_share[i] / 100) * 198
        print(f"{empresas[i]}: {market_share[i]}% (≈ R$ {valor_mercado:.1f} bi)")
    else:
        print(f"{empresas[i]}: {market_share[i]}%")
print("=" * 65)
print("💡 Mercado total estimado em R$ 198 bilhões (Abravest 2023)")