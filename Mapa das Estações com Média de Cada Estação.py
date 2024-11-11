import geopandas as gpd
import matplotlib.pyplot as plt
import contextily as ctx
import numpy as np

# Carregar o arquivo GeoJSON com as estações
estacoes = gpd.read_file('/content/drive/MyDrive/Python/TrensRJ/supervia_stations.geojson')

# Carregar o arquivo GeoJSON com as linhas de trem
trens_rj = gpd.read_file('/content/drive/MyDrive/Python/TrensRJ/Trajetos_Trem.geojson.json')

# Criar a tabela de estações com as colunas disponíveis
tabela_estacoes = estacoes[['estacao', 'ramal', 'latitude', 'longitude', 'cep', 'geometry']]

# Adicionando uma coluna de média aleatória para simular dados
np.random.seed(0)  # Para reprodutibilidade
tabela_estacoes['media'] = np.random.rand(len(tabela_estacoes)) * 1000  # Média aleatória entre 0 e 1000

# Criar um GeoDataFrame a partir da tabela de estações
gdf_estacoes = gpd.GeoDataFrame(tabela_estacoes)

# Criar um mapa base com tamanho máximo
fig, ax = plt.subplots(figsize=(16, 12))  # Aumente o tamanho da figura
trens_rj.plot(ax=ax, color='blue', linewidth=1, alpha=0.7)

# Adicionar as estações ao mapa, coloridas pela média
gdf_estacoes.plot(ax=ax, column='media', cmap='viridis', legend=True,
                  markersize=100, alpha=0.6, edgecolor='k')

# Definir limites do eixo para maximizar a área visível do mapa
ax.set_xlim(gdf_estacoes.geometry.x.min() - 0.01, gdf_estacoes.geometry.x.max() + 0.01)
ax.set_ylim(gdf_estacoes.geometry.y.min() - 0.01, gdf_estacoes.geometry.y.max() + 0.01)

# Adicionar um fundo de mapa usando Contextily
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron, crs=gdf_estacoes.crs.to_string())

# Adicionar título e legendas
plt.title('Mapa das Estações com Média de Cada Estação')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

# Exibir o mapa
plt.tight_layout()  # Ajustar layout para evitar sobreposição
plt.show()
