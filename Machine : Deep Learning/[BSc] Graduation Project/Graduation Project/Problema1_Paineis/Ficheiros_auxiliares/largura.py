import os, sys, csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math as ma
from PIL import Image

if(not os.path.exists("imagens")): os.makedirs("imagens")

dir = os.listdir("annotated_Patches")
largura = []

# obter os dados
for i in dir:
    if(i[0]=="."): continue
    im = Image.open("annotated_Patches/" + i)
    width, height = im.size
    largura.append(width)

# apresentar o gráfico
num_bins = 100
plt.figure(figsize=(12,6))
plt.hist(largura, num_bins, facecolor='skyblue', alpha=0.5, edgecolor="k")
plt.title("Largura das patches")
plt.xlabel("Largura (px)", labelpad=2)
plt.ylabel("Frequencia")

media = (sum(largura) / float(len(largura)))

# escala vertical
scale = []
for i in range(500,8001,500):
    scale.append(i)

plt.yticks(scale)

# escala horizontal
scale = [0]
contador = 0
while(max(largura)>max(scale)):
    contador+=15
    scale.append(contador)

plt.xticks(scale, rotation=35)
axes = plt.gca()
axes.set_xlim([0,max(scale)])
plt.axvline(media, color='r', linestyle='--')
plt.text(0.92, 0.95,'Media: ' + str(int(media)) + " pixeis", horizontalalignment='center', verticalalignment='center', transform = axes.transAxes)
plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.1)
plt.savefig('imagens/largura.png')
plt.show()