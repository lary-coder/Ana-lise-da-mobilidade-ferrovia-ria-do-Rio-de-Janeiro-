import geopandas as gpd


# Carregar o arquivo GeoJSON com as estações
estacoes = gpd.read_file('/content/drive/MyDrive/Python/TrensRJ/supervia_stations.geojson')


# Exibir todas as colunas do arquivo de estações
print("Colunas disponíveis no arquivo 'supervia_stations.geojson':")
print(estacoes.columns)


# Carregar o arquivo GeoJSON com as linhas de trem
trens_rj = gpd.read_file('/content/drive/MyDrive/Python/TrensRJ/Trajetos_Trem.geojson.json')


# Exibir todas as colunas do arquivo de trajetos
print("\nColunas disponíveis no arquivo 'Trajetos_Trem.geojson.json':")
print(trens_rj.columns)


# Criar a tabela de estações com as colunas disponíveis
tabela_estacoes = estacoes[['estacao', 'ramal', 'latitude', 'longitude', 'cep', 'geometry']]


# Exibir a tabela de estações
print("\nTabela de estações:")
print(tabela_estacoes)


# Criar uma tabela com as colunas que podem ser relevantes dos trajetos
# Neste caso, não temos 'objectid' ou 'name', mas podemos usar 'ramal'
# Se houver alguma relação entre estações e ramais nos trajetos
tabela_trens = trens_rj[['ramal', 'geometry']]


# Exibir a tabela de trajetos
print("\nTabela de trajetos:")
print(tabela_trens)
