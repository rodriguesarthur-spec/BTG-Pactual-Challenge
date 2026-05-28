import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker


try:
    df = pd.read_csv('releaseRenner.csv')


    df.columns = df.columns.str.strip()


    df.rename(columns={'EMBITDA Ajustado(R$ mi )': 'EBITDA_Ajustado_Milhoes'}, inplace=True)

    def converter_ebitda(valor):
    
        s_valor = str(valor).strip()
        
       
        if 'bi' in s_valor:
        
            num = float(s_valor.replace(' bi', '').replace('.', '')) / 1000 if '.' in s_valor else float(s_valor.replace(' bi', ''))*1000
            return num


        try:
            return float(s_valor)
        except (ValueError, TypeError):
   
            return pd.NA

  
    df['EBITDA_Ajustado_Milhoes'] = df['EBITDA_Ajustado_Milhoes'].apply(converter_ebitda)

    df.dropna(subset=['EBITDA_Ajustado_Milhoes'], inplace=True)

    df['ANO'] = df['ANO'].astype(int)

    df['Periodo'] = df['ANO'].astype(str) + '-' + df['Trimestre'].astype(str)

    plt.figure(figsize=(15, 8))

    plt.plot(df['Periodo'], df['EBITDA_Ajustado_Milhoes'], marker='o', linestyle='-', color='b')

    plt.title('Histórico de EBITDA Ajustado - Lojas Renner (2020-2024)', fontsize=16)
    plt.xlabel('Período (Ano-Trimestre)', fontsize=12)
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