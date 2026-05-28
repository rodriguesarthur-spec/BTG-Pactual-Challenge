import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

csv_data = """ANO,Trimestre,"EMBITDA Ajustado(R$ mi )"
2020,1T20,65.9
2020,2T20,-133.4
2020,3T20,87.3
2020,4T20,617.1
2021,1T21,134.7
2021,2T21,348.4
2021,3T21,432.1
2021,4T21,808.1
2022,1T22,321.5
2022,2T22,399.0
2022,3T22,321.5
2022,4T22,918.6
2023,1T23,356.0
2023,2T23,384.6
2023,3T23,356.0
2023,4T23,1010.0
2024,1T24,421.2
2024,2T24,545.8
2024,3T24,682.2
2024,4T24,1000.4
2025,1T25,442.1
2025,2T25,573.5
"""
with open('releaseRenner.csv', 'w') as f:
    f.write(csv_data)


try:
    df = pd.read_csv('releaseRenner.csv')
    df.columns = df.columns.str.strip()
    df.rename(columns={'EMBITDA Ajustado(R$ mi )': 'EBITDA_Ajustado_Milhoes'}, inplace=True)

    def converter_ebitda_corrigido(valor):
        try:
            s_valor = str(valor).strip().replace(',', '.')
            if 'bi' in s_valor:
                return float(s_valor.replace('bi', '')) * 1000
            return float(s_valor)
        except (ValueError, TypeError):
            return pd.NA

    df['EBITDA_Ajustado_Milhoes'] = df['EBITDA_Ajustado_Milhoes'].apply(converter_ebitda_corrigido)
    df.dropna(subset=['EBITDA_Ajustado_Milhoes'], inplace=True)
    df['ANO'] = df['ANO'].astype(int)
    df['Periodo'] = df['Trimestre']



    plt.style.use('seaborn-v0_8-whitegrid')
    plt.figure(figsize=(16, 8))

    plt.plot(df['Periodo'], df['EBITDA_Ajustado_Milhoes'], marker='o', linestyle='-', color='#003366')
    
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
    plt.title('Histórico de EBITDA Ajustado - Lojas Renner (2020-2025)', fontsize=16, weight='bold')
    plt.xlabel('Período (Trimestre)', fontsize=12)
    plt.ylabel('EBITDA Ajustado (R$ Milhões)', fontsize=12)

    formatter = mticker.FuncFormatter(lambda x, p: f'R$ {int(x):,d}'.replace(',', '.'))
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.xticks(rotation=45, ha='right')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

except FileNotFoundError:
    print("Erro: O arquivo 'releaseRenner.csv' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")