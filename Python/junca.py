import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

full_data = {
    'Empresa': [
        'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner', 'Renner',
        'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo', 'Riachuelo',
        'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz', 'Petz',
        'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero', 'Quero-Quero',
        'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)', 'Azzas (Arezzo&Co)'
    ],
    'Periodo': [
        '1T20', '2T20', '3T20', '4T20', '1T21', '2T21', '3T21', '4T21', '1T22', '2T22', '3T22', '4T22', '1T23', '2T23', '3T23', '4T23', '1T24', '2T24', '3T24', '4T24', '1T25', '2T25'
    ] * 5,
    'EBITDA': [
        # Renner
        65.9, -133.4, 87.3, 617.1, 134.7, 348.4, 432.1, 808.1, 321.5, 399.0, 321.5, 918.6, 356.0, 384.6, 356.0, 1010.0, 421.2, 545.8, 682.2, 1000.4, 442.1, 573.5,
        # Riachuelo
        37.2, -197.1, 94.8, 450.8, 101.3, 262.2, 234.6, 565.1, 100.5, 261.8, 234.8, 442.1, 87.5, 238.8, 183.8, 463.5, 211.0, 360.5, 350.2, 515.4, 258.0, 286.6,
        # Petz
        20.1, 35.5, 45.2, 49.6, 60.7, 69.5, 76.0, 73.8, 69.8, 68.0, 71.5, 64.5, 65.7, 63.4, 71.3, 75.5, 68.0, 76.9, 80.1, 82.3, 78.5, 84.2,
        # Quero-Quero
        10.5, 40.1, 65.8, 78.5, 39.0, 68.9, 56.1, 46.2, 10.2, 25.6, 26.0, 48.0, 28.1, 41.5, 43.2, 66.3, 35.7, 52.1, 55.9, 71.4, 42.3, 58.8,
        # Azzas (Arezzo&Co)
        43.8, 2.5, 63.1, 122.2, 90.3, 81.3, 112.6, 185.3, 113.3, 156.9, 163.1, 190.4, 143.7, 198.0, 212.5, 221.0, 164.1, 203.0, 225.8, 255.1, 427.7, 535.6
    ]
}

df = pd.DataFrame(full_data)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(18, 10), dpi=120)

estilos = {
    'Renner': {'color': '#003366', 'linewidth': 2.5, 'alpha': 1.0, 'zorder': 10},
    'Riachuelo': {'color': '#D90000', 'linewidth': 2.5, 'alpha': 1.0, 'zorder': 9},
    'Azzas (Arezzo&Co)': {'color': '#8A2BE2', 'linewidth': 2.0, 'alpha': 0.8, 'zorder': 8},
    'Petz': {'color': '#FF6600', 'linewidth': 1.5, 'alpha': 0.7, 'zorder': 7},
    'Quero-Quero': {'color': '#008000', 'linewidth': 1.5, 'alpha': 0.7, 'zorder': 6}
}

for empresa in df['Empresa'].unique():
    df_empresa = df[df['Empresa'] == empresa]
    ax.plot(df_empresa['Periodo'], df_empresa['EBITDA'], 
            label=empresa, 
            **estilos[empresa])

for empresa, estilo in estilos.items():
    df_empresa = df[df['Empresa'] == empresa].iloc[-1]
    ax.text(df_empresa['Periodo'], df_empresa['EBITDA'], f' {empresa}', 
            color=estilo['color'], va='center', ha='left', fontsize=11, weight='bold')


ax.annotate('Impacto inicial da Pandemia', 
            xy=('2T20', -197.1), 
            xytext=('4T20', -350),
            arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle="arc3,rad=0.2"),
            fontsize=12, ha='center', bbox=dict(boxstyle="round,pad=0.3", fc="yellow", ec="k", lw=1, alpha=0.7))


fig.suptitle('Desempenho Economico com ebitda como metrica', fontsize=20, weight='bold', ha='center')
ax.set_title('EBITDA Ajustado Trimestral (R$ Milhões) | 2020-2025', fontsize=14, pad=10)

ax.set_xlabel('Período (Trimestre)', fontsize=12)
ax.set_ylabel('EBITDA Ajustado (R$ Milhões)', fontsize=12)

ax.axhline(0, color='grey', linewidth=0.9, linestyle='--')
formatter = mticker.FuncFormatter(lambda x, p: f'R$ {int(x):,d}'.replace(',', '.'))
ax.yaxis.set_major_formatter(formatter)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.grid(axis='x', linestyle=':')
plt.figtext(0.9, 0.01, 'Fonte: Releases de Resultados das companhias.', ha='right', fontsize=10, color='gray')
plt.tight_layout(rect=[0, 0.05, 1, 0.95]) 

plt.show()