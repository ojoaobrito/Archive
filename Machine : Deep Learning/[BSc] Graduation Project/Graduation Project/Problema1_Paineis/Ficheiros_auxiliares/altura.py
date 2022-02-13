import os, sys, csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math as ma
from PIL import Image

if(not os.path.exists("imagens")): os.makedirs("imagens")

dir = os.listdir("annotated_Patches")
altura = []

# obter os dados
for i in dir:
    if(i[0]=="."): continue
    im = Image.open("annotated_Patches/" + i)
    width, height = im.size
    altura.append(height)

# apresentar o gráfico
num_bins = 100
plt.figure(figsize=(12,6))
plt.hist(altura, num_bins, facecolor='skyblue', alpha=0.5, edgecolor="k")
plt.title("Altura das patches")
plt.xlabel("Altura (px)", labelpad=2)
plt.ylabel("Frequencia")

media = (sum(altura) / float(len(altura)))

# escala vertical
scale = []
for i in range(500,7001,500):
    scale.append(i)

plt.yticks(scale)

# escala horizontal
scale = [0]
contador = 0
while(max(altura)>max(scale)):
    contador+=25
    scale.append(contador)

plt.xticks(scale, rotation=35)

axes = plt.gca()
axes.set_xlim([0,max(scale)])
plt.axvline(media, color='r', linestyle='--')
plt.text(0.92, 0.95,'Media: ' + str(int(media)) + " pixeis", horizontalalignment='center', verticalalignment='center', transform = axes.transAxes)
plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.1)
plt.savefig('imagens/altura.png')
plt.show()