import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


data = {
    'Periodo': ['Jan-20', 'Fev-20', 'Mar-20', 'Abr-20', 'Mai-20', 'Jun-20', 'Dez-20', 'Dez-21', 'Dez-22', 'Dez-23', 'Dez-24', 'Jul-25'],
    'LREN3': [28.6, 26.5, 17.5, 21.0, 21.5, 23.0, 25.7, 14.8, 12.9, 17.1, 11.8, 13.5],
    'GUAR3': [18.5, 17.0, 9.0, 11.5, 12.0, 13.5, 16.0, 10.5, 7.5, 8.0, 6.5, 6.8],
    'PETZ3': [8.0, 7.5, 5.0, 7.0, 8.5, 9.5, 18.0, 15.0, 7.0, 8.2, 3.5, 3.8],
    'LJQQ3': [12.0, 11.5, 8.0, 9.0, 10.0, 11.0, 16.0, 10.0, 5.0, 6.0, 4.0, 4.2],
    'ARZZ3': [30.0, 28.0, 18.0, 22.0, 25.0, 28.0, 35.0, 38.0, 45.0, 55.0, 52.0, 60.0]
}
df = pd.DataFrame(data).set_index('Periodo')
df.rename(columns={'LREN3': 'Renner', 'GUAR3': 'Riachuelo', 'PETZ3': 'Petz', 'LJQQ3': 'Quero-Quero', 'ARZZ3': 'Azzas (Arezzo&Co)'}, inplace=True)


df_normalizado = (df / df.iloc[0] * 100)

plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(20, 10), dpi=120, sharex=True, sharey=True)
axes = axes.flatten()

cores = {'Renner': '#003366', 'Riachuelo': '#D90000', 'Petz': '#FF6600', 'Quero-Quero': '#008000', 'Azzas (Arezzo&Co)': '#8A2BE2'}

for i, empresa in enumerate(df_normalizado.columns):
    ax = axes[i]
    ax.plot(df_normalizado.index, df_normalizado[empresa], color=cores[empresa], linewidth=2.5)
    
    ax.set_title(empresa, fontsize=14, weight='bold', color=cores[empresa])
    
    ax.axhline(100, color='grey', linewidth=1, linestyle='--', alpha=0.8)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    if i >= 2: 
        ax.tick_params(axis='x', rotation=45)

axes[-1].set_visible(False)

fig.suptitle('Painel Comparativo de Desempenho de Ações (Base 100 desde Jan-2020)', fontsize=22, weight='bold')
fig.text(0.5, 0.04, 'Período', ha='center', va='center', fontsize=14)
fig.text(0.08, 0.5, 'Índice de Desempenho (Jan-2020 = 100)', ha='center', va='center', rotation='vertical', fontsize=14)

# Ajuste de layout
plt.tight_layout(rect=[0.1, 0.05, 1, 0.95])
plt.show()