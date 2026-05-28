import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Bloco para criar o arquivo CSV com dados da Riachuelo ---
csv_data = """ANO,Trimestre,"EBITDA_Ajustado_Milhoes"
2020,1T20,37.2
2020,2T20,-197.1
2020,3T20,94.8
2020,4T20,450.8
2021,1T21,101.3
2021,2T21,262.2
2021,3T21,234.6
2021,4T21,565.1
2022,1T22,100.5
2022,2T22,261.8
2022,3T22,234.8
2022,4T22,442.1
2023,1T23,87.5
2023,2T23,238.8
2023,3T23,183.8
2023,4T23,463.5
2024,1T24,211.0
2024,2T24,360.5
2024,3T24,350.2
2024,4T24,515.4
2025,1T25,258.0
2025,2T25,286.6
"""
with open('riachuelo_ebitda.csv', 'w') as f:
    f.write(csv_data)
# --- Fim do bloco de criação do arquivo ---


# --- 1. Carregamento e Limpeza dos Dados ---
try:
    df = pd.read_csv('riachuelo_ebitda.csv')
    df.columns = df.columns.str.strip()
    df['Periodo'] = df['Trimestre'] # O nome do trimestre já é único

    # --- 2. Geração do Gráfico ---

    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(16, 8))

    plt.plot(df['Periodo'], df['EBITDA_Ajustado_Milhoes'], marker='o', linestyle='-', color='#D90000') # Cor vermelha para Riachuelo
    
    # Adicionar rótulos de dados em cada ponto
    for i, ebitda in enumerate(df['EBITDA_Ajustado_Milhoes']):
        vertical_offset = 12 if ebitda >= 0 else -20
        plt.annotate(
            f'R$ {int(ebitda)} M', 
            (df['Periodo'][i], ebitda),
            textcoords="offset points",
            xytext=(0, vertical_offset),
            ha='center',
            fontsize=9
        )

    plt.axhline(0, color='grey', linewidth=0.8, linestyle='--')
    plt.title('Histórico de EBITDA Ajustado - Riachuelo (Guararapes | 2020-2025)', fontsize=16, weight='bold')
    plt.xlabel('Período (Trimestre)', fontsize=12)
    plt.ylabel('EBITDA Ajustado (R$ Milhões)', fontsize=12)

    formatter = mticker.FuncFormatter(lambda x, p: f'R$ {int(x):,d}'.replace(',', '.'))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45, ha='right')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Erro: O arquivo 'riachuelo_ebitda.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")