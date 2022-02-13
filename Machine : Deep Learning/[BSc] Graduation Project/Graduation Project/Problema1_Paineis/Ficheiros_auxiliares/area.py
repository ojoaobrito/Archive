import os, sys, csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math as ma
from PIL import Image

if(not os.path.exists("imagens")): os.makedirs("imagens")

dir = os.listdir("annotated_Patches")
area = []

# obter os dados
for i in dir:
    if(i[0]=="."): continue
    im = Image.open("annotated_Patches/" + i)
    width, height = im.size
    area.append(width*height)

# apresentar o gráfico
num_bins = 100
plt.figure(figsize=(12,7))
plt.hist(area, num_bins, facecolor='skyblue', alpha=0.5, edgecolor="k")
plt.title("Area das patches")
plt.xlabel("Area (px)", labelpad=2)
plt.ylabel("Frequencia")

media = (sum(area) / float(len(area)))

# escala vertical
scale = []
for i in range(500,15001,500):
    scale.append(i)

plt.yticks(scale)

# escala horizontal
scale2 = [0]
contador = 0
while(max(area)>max(scale2)):
    contador+=10000
    scale2.append(contador)

plt.xticks(scale2, rotation=35)
axes = plt.gca()
axes.set_xlim([0,max(scale2)])
axes.set_ylim([0,15000])
plt.axvline(media, color='r', linestyle='--')
plt.text(0.91, 0.95,'Media: ' + str(int(media)) + " pixeis", horizontalalignment='center', verticalalignment='center', transform = axes.transAxes)
plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.1)
plt.savefig('imagens/area.png')
plt.show()