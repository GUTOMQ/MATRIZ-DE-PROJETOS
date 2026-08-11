import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Carregar os dados
df = pd.read_csv("Base_Varejo.csv", sep=";")

# 2. Verificar o tamanho original
print("Tamanho original:", df.shape)

# 3. Verificar valores ausentes
print("\nValores ausentes:")
print(df.isna().sum())

# 4. Remover colunas completamente vazias
df = df.dropna(axis=1, how="all")

# 5. Verificar o resultado da limpeza
print("\nTamanho depois da limpeza:", df.shape)

# 6. Mostrar as colunas restantes
print("\nColunas restantes:")
print(df.columns)