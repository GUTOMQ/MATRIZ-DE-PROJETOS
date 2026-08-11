import matplotlib.pyplot as plt

# Dados
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [12000, 15000, 13500, 18000, 22000, 25000]

# Criando o gráfico
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(meses, vendas, linewidth=2, marker="o")

ax.set_title("Vendas mensais")
ax.set_xlabel("Mês")
ax.set_ylabel("Vendas (R$)")

ax.legend(["Loja Centro"])

plt.tight_layout()

# Salva o gráfico como imagem
plt.savefig("vendas.png", dpi=300)

# Mostra o gráfico na tela
plt.show()


# ABAIXO está o código do Senpaio
# import matplotlib.pyplot as plt
# import seaborn as sns

# meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
# vendas = [1800, 1200, 7000, 10000, 8500, 15000, 5000, 4000, 9000, 1500, 5600, 15000]

# fig, ax = plt.subplots(figsize=(8, 5))
# ax.plot(meses, vendas, color='gold', linewidth=2)
# ax.set_title("Vendas Mensais")
# ax.set_xlabel("Mes")
# ax.set_ylabel("Vendas (R$)")
# ax.legend(["Loja Centro"])
# plt.savefig("vendas_ano.png", dpi=300)