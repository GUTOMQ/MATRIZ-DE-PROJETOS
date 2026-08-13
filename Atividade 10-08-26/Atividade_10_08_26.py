import matplotlib.pyplot as plt
import seaborn as sns

#DADOS --> GRAFICO DE LINHA -- SEMANAS --- QUANTIDADE DE ALUNOS 

dias = ["Segundo", "Terça", "Quarta", "Quinta", "Sexta"]
alunos = [12,10,10,20,25]

# CRIAR O MEU GRAFICO DE LINHA

sns.lineplot(x=dias, y=alunos, marker="o", color="blue")

# TITULO DO GRAFICO 

plt.title("Quantidade de Alunos por Dia da Semana")

# ROTULO DOS EIXOS 

plt.xlabel("Dias da Semana")
plt.ylabel("Quantidade de Alunos")

# IMPRIMIR OU EXIBIR O GRAFICO
plt.show()

