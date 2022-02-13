import os, sys, csv
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from mpl_toolkits.mplot3d import Axes3D
import natsort 

if(not os.path.exists("imagens")): os.makedirs("imagens")

diretoria = os.listdir("annotated_Patches")
nomes = []
lista = []

diretoria = natsort.natsorted(diretoria,reverse=False)

# obter os dados
for i in diretoria:
    if(i[0]=="."): continue
    aux = (i.split("_")[0] + "_" + i.split("_")[1] + "_" + i.split("_")[2] + "_" + i.split("_")[4])
    if(aux not in nomes):
        nomes.append(aux)
        lista.append([[],[]])

    lista[nomes.index(aux)][0].append(len(lista[nomes.index(aux)][0])+1)
    im = Image.open("annotated_Patches/" + i)
    width, height = im.size
    lista[nomes.index(aux)][1].append(width*height)

# normalizar as áreas
for i in range(0,len(lista),1):
    delta_frames = (max(lista[i][0])-min(lista[i][0]))
    delta_areas = (max(lista[i][1])-min(lista[i][1]))
    minimo_frames = min(lista[i][0])
    minimo_areas = min(lista[i][1])
    for j in range(0,len(lista[i][0]),1): # percorrer as frames/area por frame do individuo
        if(delta_frames!=0):
            lista[i][0][j] = round(((lista[i][0][j]-minimo_frames)/delta_frames),5)
        else:
            for k in range(0,len(lista[i][0]),1): lista[i][0][k] = 1.0 
        
        if(delta_areas!=0):
            lista[i][1][j] = round(((lista[i][1][j]-minimo_areas)/delta_areas),5)
        else:
            for k in range(0,len(lista[i][1]),1): lista[i][1][k] = 1.0 

# exemplo
# plt.plot(lista[8][0],lista[8][1])
# plt.title("Movimento da pessoa " + nomes[8])
# plt.ylabel("Area (normalizada)")
# plt.xlabel("Frames (normalizadas)")
# axes = plt.gca()
# plt.text(0.84, 0.94,"Numero frames: " + str(len(lista[8][0])), horizontalalignment='center', verticalalignment='center', transform = axes.transAxes)
# plt.savefig('imagens/movimento_' + nomes[8].split(" ID ")[0] + nomes[8].split(" ID ")[1] + '.png')
# plt.show()
# sys.exit()

# apresentar o histograma 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = []
y = []
for i in lista: 
    for j in i[0]: x.append(j)
    for j in i[1]: y.append(j)

hist, xedges, yedges = np.histogram2d(x, y, bins=(35,35))
xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:])

xpos = xpos.flatten()/2.
ypos = ypos.flatten()/2.
zpos = np.zeros_like (xpos)

dx = xedges [1] - xedges [0]
dy = yedges [1] - yedges [0]
dz = hist.flatten()

ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')
plt.title("Histograma 3D das Areas")
plt.xlabel ("Frames (normalizadas)")
plt.ylabel ("Area (normalizada)")
plt.gca().invert_yaxis()
plt.savefig('imagens/histograma_3D.png')
plt.show()