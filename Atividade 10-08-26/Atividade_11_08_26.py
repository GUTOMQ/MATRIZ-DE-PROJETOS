from bs4 import BeautifulSoup
import requests
import os

# OS DADOS QUE A NOSSA APLICAÇÃO VAI PEGAR
url = "https://quotes.toscrape.com/"

# ACESSAR O CORPO DA APLICAÇÃO

pagina = requests.get(url)

# LER AS INFORMAÇÕES DO MEU HTML
soup = BeautifulSoup(pagina.content, "html.parser")

# PARÂMETRO PARA APLICAÇÃO PEGAR TODAS AS FRASES
frases = soup.find_all("span", class_="text")

#IMPRIMIR TODAS AS FRASES QUE COLOQUEI COMO PARÂMETRO
for frase in frases:
    print(frase.text)

# SALVAR AS FRASES EM UM ARQUIVO DE TEXTO DENTRO UM ARQUIVO TXT
with open("frases.txt", "w") as arquivo:
    for frase in frases:
        arquivo.write(frase.text + "\n")
        print(frase.text + "\n")
print("Frases salvas com sucesso no arquivo frases.txt")

# CRIAR UN ARQUIVO CSV COM AS FRASES
with open("frases.csv", "w") as arquivo_csv:
    arquivo_csv.write("Frases\n")
    for frase in frases:
        arquivo_csv.write(frase.text + "\n")
print("Frases salvas com sucesso no arquivo frases.csv")