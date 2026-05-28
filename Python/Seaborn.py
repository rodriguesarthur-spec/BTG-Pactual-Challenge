import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("DesempenhoRenner_2014_2025.csv")

sns.set_theme(style="whitegrid")  
plt.figure(figsize=(10,6))
ax = sns.lineplot(data=df, x="Ano", y="Ticket_Medio", marker="o")
ax.set_title("Ticket Médio por Ano", fontsize=14)
ax.set_xlabel("Ano")
ax.set_ylabel("Ticket Médio")
plt.tight_layout()
plt.show()
