import pandas as pd
import numpy as np

# carregar o CSV

df = pd.read_csv("clientes.csv")

#remover as colunas duplicadas

df = df.drop_duplicates()

#tratar dados ausentes

df["salario"]= df["salario"].fillna(df["salario"].median())

#remover as outliers de idade

df = df [df["idade"].between(0,100)]

#criar faixa salarial
df["faixa_salarial"] = pd.cut(
    df["salario"],
    bins=[0, 2000, 5000, 10000, np.inf],
    labels=["Baixa", "Média", "Alta", "Muito Alta"],
    include_lowest=True
)
# salvar as informações tratadas em um novo arquivo CSV
df = df.to_csv("clientes_tratados.csv", index=False)
                                     
print("Arquivo 'clientes_tratados.csv' criado com sucesso!")
print(df)                                            
                                                                   