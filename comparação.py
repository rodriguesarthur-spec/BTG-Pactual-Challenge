import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("desempenho_varejistas_historico_parcial.csv")

df['Ano'] = df['Periodo'].str.extract(r'(\d{4})').astype(float)
df = df.dropna(subset=['Ano'])
df['Ano'] = df['Ano'].astype(int)


df_long = pd.melt(
    df,
    id_vars=['Empresa', 'Ano'],
    value_vars=['Receita_Liquida_R$mi', 'Lucro_Liquido_R$mi'],
    var_name='Métrica',
    value_name='Valor'
)

sns.set_theme(style="ticks")
palette = sns.color_palette("rocket_r")


g = sns.relplot(
    data=df_long,
    x="Ano", y="Valor",
    hue="Empresa", size="Métrica", col="Métrica",
    kind="line", size_order=['Receita_Liquida_R$mi', 'Lucro_Liquido_R$mi'],
    palette=palette,
    height=5, aspect=.75,
    facet_kws=dict(sharex=False)
)

g.set_titles("align = {col_name}")
g.set_axis_labels("Ano", "Valor (R$ mi)")
plt.show()
