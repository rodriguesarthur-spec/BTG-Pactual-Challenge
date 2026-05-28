import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# --- Bloco para criar o arquivo CSV com dados da Quero-Quero ---
csv_data = """ANO,Trimestre,"EBITDA_Ajustado_Milhoes"
2020,1T20,10.5
2020,2T20,40.1
2020,3T20,65.8
2020,4T20,78.5
2021,1T21,39.0
2021,2T21,68.9
2021,3T21,56.1
2021,4T21,46.2
2022,1T22,10.2
2022,2T22,25.6
2022,3T22,26.0
2022,4T22,48.0
2023,1T23,28.1
2023,2T23,41.5
2023,3T23,43.2
2023,4T24,66.3
2024,1T24,35.7
2024,2T24,52.1
2024,3T24,55.9
2024,4T24,71.4
2025,1T25,42.3
2025,2T25,58.8
"""
with open('queroquero_ebitda.csv', 'w') as f:
    f.write(csv_data)
# --- Fim do bloco de criação do arquivo ---


# --- 1. Carregamento e Limpeza dos Dados ---
try:
    df = pd.read_csv('queroquero_ebitda.csv')
    df.columns = df.columns.str.strip()
    df['Periodo'] = df['Trimestre']

    # --- 2. Geração do Gráfico ---
    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(16, 8))

    # Cor verde para a identidade visual da Quero-Quero
    plt.plot(df['Periodo'], df['EBITDA_Ajustado_Milhoes'], marker='o', linestyle='-', color='#008000') 
    
    # Adicionar rótulos de dados em cada ponto
    for i, ebitda in enumerate(df['EBITDA_Ajustado_Milhoes']):
        vertical_offset = 12
        plt.annotate(
            f'R$ {ebitda:.1f} M', # Usando 1 casa decimal para maior precisão
            (df['Periodo'][i], ebitda),
            textcoords="offset points",
            xytext=(0, vertical_offset),
            ha='center',
            fontsize=9
        )

    plt.axhline(0, color='grey', linewidth=0.8, linestyle='--')
    plt.title('Histórico de EBITDA Ajustado - Lojas Quero-Quero (2020-2025)', fontsize=16, weight='bold')
    plt.xlabel('Período (Trimestre)', fontsize=12)
    plt.ylabel('EBITDA Ajustado (R$ Milhões)', fontsize=12)

    formatter = mticker.FuncFormatter(lambda x, p: f'R$ {int(x):,d}'.replace(',', '.'))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45, ha='right')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Erro: O arquivo 'queroquero_ebitda.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")