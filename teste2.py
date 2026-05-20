import matplotlib.pyplot as plt

labels = ['Outras Varejistas', 'Lojas Renner', 'Riachuelo (Guararapes)', 'C&A', 'Marisa']
sizes = [88.1, 5.3, 3.4, 2.5, 0.7]

colors = ['#d9d9d9', '#003f5c', '#2f6fa6', '#7a9cc9', '#9e9e9e']

explode = (0.01, 0.08, 0.10, 0.12, 0.2)

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'Verdana', 'DejaVu Sans']

fig, ax = plt.subplots(figsize=(14, 10))
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

wedges, texts, autotexts = ax.pie(
    sizes,
    colors=colors,
    explode=explode,
    autopct=lambda pct: f'{pct:.1f}%' if pct > 2 else '',
    startangle=120,
    pctdistance=0.82,
    wedgeprops=dict(width=0.35, edgecolor='white', linewidth=2.5)
)

ax.text(
    0, 0.05,
    'R$ 259,5 Bi',
    ha='center', va='center',
    fontsize=26, fontweight='bold', color='#1a1a1a'
)
ax.text(
    0, -0.18,
    'Mercado de Moda (2024)',
    ha='center', va='center',
    fontsize=13, color='#555555'
)

fig.suptitle(
    'Market Share do Varejo de Moda no Brasil',
    fontsize=24, fontweight='bold', color='#1a1a1a',
    ha='center'
)
ax.set_title(
    'Análise Consolidada | Fonte: RI das Empresas & IEMI',
    fontsize=12, color='#666666', pad=20
)

ax.legend(
    wedges,
    [f'{label} — {size:.1f}%' for label, size in zip(labels, sizes)],
    title="Participação de Mercado (2024)",
    title_fontsize=13,
    loc="lower center",
    bbox_to_anchor=(0.5, -0.15),
    fontsize=12,
    frameon=False,
    ncol=2
)

plt.setp(autotexts, size=11, weight="bold", color="white")

fig.text(
    0.5, 0.02,
    "Obs: valores estimados a partir de relatórios públicos e IEMI (2024).",
    ha='center', fontsize=10, color="#777777"
)

ax.axis('equal')
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()
