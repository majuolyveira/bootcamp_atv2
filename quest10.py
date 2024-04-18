import pandas as pd
import numpy as np


data = {'A': [1, 2, None, 4], 'B': [None, 5, 6, None]}
df = pd.DataFrame(data)

print("Valores Ausentes:")
print(df.isna())

print("\nDataFrame Original: ")
print(df)

df_preenchido = df.fillna(0)
print("\nDataFrame com Valores Ausentes Preenchidos:")
print(df_preenchido)


df_sem_nan_linhas = df.dropna()


df_sem_nan_colunas = df.dropna(axis=1)

print("\nDataFrame Sem Linhas com Valores Ausentes:")
print(df_sem_nan_linhas)

print("\nDataFrame Sem Colunas com Valores Ausentes:")
print(df_sem_nan_colunas)
