import pandas as pd
import numpy as np

dados = {
        "id": [1,2,3,4,5],
        "nome": ["Ana Souza", "ana souza", "Bruno Lima", "Carla Dias", "Diego Alves" ],
        "idade": [34,34,np.nan,178,29],
        "cidade": ["Recife","Recife","Salvador" ,"Curitiba","manaus"],
        "salario":[ 2500, 2500, 3200, 4100, 3800],
        "data_Cadastro": ["2023-01-15", "2023-01-15", "2023-02-20", "2023-03-10", "2023-04-05"],
}

df = pd.DataFrame(dados)
print(df)

print("\nValores Ausente por colunas")
print(df.isna().sum())

# # Remove qualquer linha com pelo menos 1 valor ausente
df.dropna()
print(df.dropna())

# # Removendo linhas com valores ausentes na coluna 'idade'
df.dropna(subset=['salario'])

# # Remove colunas inteiras com valores ausentes
# df.dropna(axis=1)           # 0 - Ação vertical, pois percorre as linhas de cima pra baixo
# print(df.dropna(axis=1))    # 1 - Ação horizontal, pq percorre as colunas da equerda p/ direita

# # Marca true nas linhas repetidas
# df.duplicated()
# print ("\n Linhas repetidas: ")
# print (df.duplicated())

# # Conta quantas linhas são duplicadas
# df.duplicated().sum()
# print ("\n Valores duplicados: ")
# print (df.duplicated().sum())

# Criando uma coluna auxiliar com os nomes padronizados
df["nome_padronizado"] = df["nome"].str.strip().str.lower()

# Identificando nomes duplicados
duplicadas = df.duplicated(
    subset=["nome_padronizado"],
    keep=False
)

print("Linhas duplicadas pelo nome:")
print(df[duplicadas])