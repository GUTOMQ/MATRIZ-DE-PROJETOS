import matplotlib.pyplot as plt
from PIL import Image
from urllib.request import urlopen

# CARREGAR A IMAGEM
url = "https://www.gstatic.com/marketing-cms/assets/images/c6/b8/41d4dd1d429685a52ab585ada96f/g-3a-socialshare.png"

# ABRIR A IMAGEM
imagem = Image.open(urlopen(url))

# EXIBIR A IMAGEM
plt.imshow(imagem)

# MOSTRAR O GRÁFICO
plt.show()