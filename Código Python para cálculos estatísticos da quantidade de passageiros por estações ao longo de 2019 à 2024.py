import pandas as pd


# Caminho do arquivo
file_path = '/content/drive/MyDrive/Python/TrensRJ/Dados_Supervia.xlsx'


# Carregar a planilha "Supervia2019_2024"
df = pd.read_excel(file_path, sheet_name='Supervia2019_2024')


# Converter o cabeçalho (que contém as datas no formato DD/MM/AAAA) para datetime, ignorando as colunas não-data
colunas = []
for col in df.columns:
    try:
        colunas.append(pd.to_datetime(col, format='%d/%m/%Y'))
    except (ValueError, TypeError):
        colunas.append(col)  # Se não for uma data, manter como está


df.columns = colunas


# Definir intervalo de datas para filtrar (janeiro/2019 a março/2024)
start_date = pd.to_datetime('2019-01-01')
end_date = pd.to_datetime('2024-03-31')


# Filtrar as colunas que estão no intervalo de datas desejado
colunas_data = [col for col in df.columns if isinstance(col, pd.Timestamp) and start_date <= col <= end_date]


# Criar um DataFrame para armazenar as médias trimestrais
media_trimestral = pd.DataFrame()


# Percorrer cada estação e calcular a média trimestral
for station in df['Estação'].unique():  # Supondo que há uma coluna 'Estação' no DataFrame
    dados_estacao = df[df['Estação'] == station][colunas_data]


    # Converter todos os dados para numérico, valores inválidos serão convertidos para NaN
    dados_estacao = dados_estacao.apply(pd.to_numeric, errors='coerce')


    # Transpor os dados para que cada coluna seja um trimestre
    dados_estacao_transposta = dados_estacao.T
    dados_estacao_transposta.index = pd.to_datetime(dados_estacao_transposta.index)


    # Agrupar os dados por trimestres e calcular a média
    media_trimestre = dados_estacao_transposta.resample('Q').mean()


    # Transpor para ter as médias trimestrais em colunas e adicionar a estação como índice
    media_trimestre_transposta = media_trimestre.T
    media_trimestre_transposta['Estação'] = station


    # Concatenar com o DataFrame de médias trimestrais
    media_trimestral = pd.concat([media_trimestral, media_trimestre_transposta.set_index('Estação')])


# Resetar o índice para exibir a tabela corretamente e ordenar as colunas por data
media_trimestral = media_trimestral.sort_index(axis=1)


# Exibir a tabela completa com as médias trimestrais por estação
print(media_trimestral)


# Opcional: salvar o resultado em um arquivo Excel
media_trimestral.to_excel('/content/drive/MyDrive/Python/TrensRJ/média_trimestral_supervia.xlsx')
