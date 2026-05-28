import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

csv_data = """ANO,Trimestre,"EBITDA_Ajustado_Milhoes"
2020,1T20,20.1
2020,2T20,35.5
2020,3T20,45.2
2020,4T20,49.6
2021,1T21,60.7
2021,2T21,69.5
2021,3T21,76.0
2021,4T21,73.8
2022,1T22,69.8
2022,2T22,68.0
2022,3T22,71.5
2022,4T22,64.5
2023,1T23,65.7
2023,2T23,63.4
2023,3T23,71.3
2023,4T23,75.5
2024,1T24,68.0
2024,2T24,76.9
2024,3T24,80.1
2024,4T24,82.3
2025,1T25,78.5
2025,2T25,84.2
"""
with open('petz_ebitda.csv', 'w') as f:
    f.write(csv_data)


try:
    df = pd.read_csv('petz_ebitda.csv')
    df.columns = df.columns.str.strip()
    df['Periodo'] = df['Trimestre']


    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(16, 8))

    plt.plot(df['Periodo'], df['EBITDA_Ajustado_Milhoes'], marker='o', linestyle='-', color='#FF6600') 
    
   
    for i, ebitda in enumerate(df['EBITDA_Ajustado_Milhoes']):
        vertical_offset = 12
        plt.annotate(
            f'R$ {ebitda:.1f} M', 
            (df['Periodo'][i], ebitda),
            textcoords="offset points",
            xytext=(0, vertical_offset),
            ha='center',
            fontsize=9
        )

    plt.axhline(0, color='grey', linewidth=0.8, linestyle='--')
    plt.title('Histórico de EBITDA Ajustado - Petz (2020-2025)', fontsize=16, weight='bold')
    plt.xlabel('Período (Trimestre)', fontsize=12)
    plt.ylabel('EBITDA Ajustado (R$ Milhões)', fontsize=12)

    formatter = mticker.FuncFormatter(lambda x, p: f'R$ {int(x):,d}'.replace(',', '.'))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45, ha='right')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Erro: O arquivo 'petz_ebitda.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")