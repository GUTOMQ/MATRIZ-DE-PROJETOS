import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv("Base_Varejo.csv", sep=";")
# O 1º código era -> df = pd.read_csv("Base_Varejo.csv")
# Foi trocado, para que o sistema consiga ler e separar todas as colunas do arquivo) 


# Para ver as primeiras 5 linhas
print(df.head())

# Para ver a quantidade de linhas e colunas
print(df.shape)

# Para saber quais são as colunas
print(df.columns)
# COLUNAS
# 1. DATA: Data da compra; 
# 2. CO_ID: Identificação do número de compra (número da nota fiscal); 
# 3. CL_ID: Identificação do cliente (número do cliente); 
# 4. CL_GENERO: Sexo biológico informado pelo cliente; 
# 5. CL_EC: Estado civil do cliente: 
#    1: Casado ou união estával; 
#    2: Divorciado; 
#    3: Separado; 
#    4. Solteiro; 
#    5: Viúvo. 
# 6. CL_FHL: Número de filhos do cliente; 
# 7. CL_SEG: Segmentação econômica do cliente (classe A, B ou C); 
# 8. PR_ID: Código do produto (SKU) adquirido; 
# 9. PR_CAT: Categoria do produto adquirido; 
# 10. PR_NOME: Nome do produto adquirido.


# Quantidade de valores ausentes
print(df.isna().sum())

# para remover linhas (vazias) usamos - >    df.dropna() 
# para remover colunas (vazias) usamos - >    df.dropna(axis=1)
df = df.dropna(axis=1, how="all")