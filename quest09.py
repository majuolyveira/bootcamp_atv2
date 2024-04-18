import pandas as pd



df = pd.read_csv('/home/pc/Área de Trabalho/bootcamp/vscode/atividade2/data/california_housing_test.csv')

print(df.head())

coluna_longitude = df['longitude']
print("Coluna Longitude:")
print(coluna_longitude)

condicao = df['housing_median_age'] > 50
linhas_filtradas = df.loc[condicao]
print("\nLinhas filtradas com idade média de habitação maior que 60:")
print(linhas_filtradas)