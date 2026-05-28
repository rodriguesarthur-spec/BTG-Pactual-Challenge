import pandas as pd
import matplotlib.pyplot as plt
import locale
import re

try:
    locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
except locale.Error:
    print("Atenção: Localidade 'pt_BR.UTF-8' não encontrada.")

arquivos_empresas = {
    'rennerAcoes.csv': 'LREN3',
    'riachuelloacoes.csv': 'GUAR3',
    'marisaAcoes.csv': 'AMAR3',
    'azzasaçoes.csv': 'AZZA3',
    'grupoSoma.csv': 'SOMA3',
    'azzasCo.csv':'ARZZ3'
}

lista_de_series = []

def limpar_preco(preco):
    preco_str = str(preco).replace('R$', '').strip()
    if ',' in preco_str:
        preco_str = preco_str.replace('.', '').replace(',', '.')
    return pd.to_numeric(preco_str, errors='coerce')

print("Processando arquivos...")
for arquivo, nome_empresa in arquivos_empresas.items():
    try:
        with open(arquivo, 'r', encoding='utf-8') as f:
            linhas = f.readlines()

        linha_inicio = 2 if arquivo == 'rennerAcoes.csv' else 1
        dados_processados = []
        for linha in linhas[linha_inicio:]:
            match = re.search(r'^(.* de \d{4})\s*[,|\t]\s*(R\$.*)$', linha)
            if match:
                dados_processados.append([match.group(1).strip(), match.group(2).strip()])

        if not dados_processados:
            print(f"AVISO: Nenhum dado válido encontrado em '{arquivo}'.")
            continue
            
        df = pd.DataFrame(dados_processados, columns=['Data', 'Preco'])
        
        df['Preco'] = df['Preco'].apply(limpar_preco)
        df['Data'] = pd.to_datetime(df['Data'], format='%B de %Y', errors='coerce')
        df.dropna(subset=['Data', 'Preco'], inplace=True)
        
        df.drop_duplicates(subset='Data', keep='first', inplace=True)
        
        df.set_index('Data', inplace=True)
        
        serie_empresa = df['Preco'].rename(nome_empresa)
        lista_de_series.append(serie_empresa)
        print(f"'{arquivo}' processado com sucesso.")

    except FileNotFoundError:
        print(f"ERRO: O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"ERRO ao processar o arquivo '{arquivo}': {e}")


if len(lista_de_series) > 1:
    dados_combinados = pd.concat(lista_de_series, axis=1)
    dados_combinados.sort_index(inplace=True)
    dados_combinados = dados_combinados.loc['2020-01-01':]
    dados_normalizados = (dados_combinados / dados_combinados.bfill().iloc[0]) * 100
    

    print("Gerando o gráfico...")
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(15, 8))
    dados_normalizados.plot(ax=ax, lw=2.5)

    ax.set_title('Ações das Varejistas', fontsize=18)
    ax.set_xlabel('Ano', fontsize=12)
    ax.set_ylabel('Performance Normalizada(base 100)', fontsize=12)
    ax.axhline(100, color='gray', linestyle='--', linewidth=1)
    ax.legend(title='Empresas', fontsize=11)
    plt.figtext(0.5, 0.01, 'Fonte: Yahoo Finance', ha='center', va='bottom', fontsize=10, color='gray')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
else:
    print("\nMenos de dois arquivos foram processados com sucesso. O gráfico comparativo não pôde ser gerado.")