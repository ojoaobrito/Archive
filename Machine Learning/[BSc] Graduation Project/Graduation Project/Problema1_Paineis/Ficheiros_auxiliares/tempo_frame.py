import os, sys, csv
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import math as ma
import natsort 

if(not os.path.exists("imagens")): os.makedirs("imagens")

diretoria = os.listdir("annotated_Patches")
individuos = {}

# obter os dados
for i in diretoria:
    if(i[0]=="."): continue
    aux = (i.split("_")[0] + "_" + i.split("_")[1] + "_" + i.split("_")[2] + "_" + i.split("_")[4])
    if(aux not in individuos):
        individuos.update({aux: 1})
    else:
        individuos.update({aux: individuos.get(aux)+1})

lista = []
for i,j in individuos.items(): lista.append(j)

# apresentar o gráfico
num_bins = int(ma.sqrt(len(lista)))
plt.figure(figsize=(12,6))
plt.hist(lista, num_bins, facecolor='skyblue', alpha=0.5, edgecolor="k")
plt.title("Tempo dos individuos em cena")
plt.xlabel("Frames", labelpad=2)
plt.ylabel("Frequencia")

media = (sum(lista) / float(len(lista)))

# escala vertical
scale = []
for i in range(0,1351,50):
    scale.append(i)

plt.yticks(scale)
axes = plt.gca()
axes.set_ylim([0,1350])

# escala horizontal
scale = [0]
contador = 0
while(max(lista)>max(scale)):
    contador+=100
    scale.append(contador)

plt.xticks(scale, rotation=35)
axes = plt.gca()
axes.set_xlim([0,max(scale)])
plt.axvline(media, color='r', linestyle='--')
plt.text(0.91, 0.94,"Media: " + str(int(media)) + " frames\nTotal: " + str(len(lista)) + " individuos", horizontalalignment='center', verticalalignment='center', transform = axes.transAxes)
plt.subplots_adjust(left=0.08, right=0.95, top=0.95, bottom=0.1)
plt.savefig('imagens/tempo_frame.png')
plt.show()