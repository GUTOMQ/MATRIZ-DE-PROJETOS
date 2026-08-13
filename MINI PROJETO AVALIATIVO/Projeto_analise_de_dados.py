# ============================================================
# PROJETO: ANÁLISE EXPLORATÓRIA - BASE VAREJO
# Autor: Gustavo Queiroga
# ============================================================

import pandas as pd

# ============================================================
# 1. CARREGAMENTO DA BASE
# ============================================================

# Caminho do arquivo CSV
arquivo = "Base_Varejo.csv"

# Carregando a base
df = pd.read_csv(arquivo)

print("=" * 60)
print("1. INFORMAÇÕES INICIAIS DA BASE")
print("=" * 60)

# Número de registros e colunas
print(f"\nNúmero de registros: {df.shape[0]}")
print(f"Número de colunas: {df.shape[1]}")

print("\nNome das colunas:")
print(df.columns.tolist())

print("\nTipos de dados:")
print(df.dtypes)
