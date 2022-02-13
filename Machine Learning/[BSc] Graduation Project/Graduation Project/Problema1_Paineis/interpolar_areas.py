import os, sys
import numpy as np
from PIL import Image
import shapely.geometry as SG
import natsort
import matplotlib.pyplot as plt

## FICHEIRO QUE GUARDA NUM .TXT AS ÁREAS NORMALIZADAS OCUPADAS POR CADA INDIVÍDUO
########################################################################################################################
nomes = []
lista = []
representantes = 25
contador = 1.0
interpolada = []

diretoria = os.listdir("Patches/Elements/Datasets/Surveillance/BIODI/patches_constantProp/")
diretoria = natsort.natsorted(diretoria,reverse=False)

# obter os dados das patches
for i in diretoria:
    if(i[0]=="."): continue
    aux = (i.split("_")[0] + "_" + i.split("_")[1] + "_" + i.split("_")[2] + "_" + i.split("_")[4])
    if(aux not in nomes):
        nomes.append(aux)
        lista.append([])

    im = Image.open("Patches/Elements/Datasets/Surveillance/BIODI/patches_constantProp/" + i)
    width, height = im.size
    lista[nomes.index(aux)].append(width*height)

print("INTERPOLAR - NORMALIZAR")
# normalizar as áreas
for i in range(0,len(lista),1):
    delta_areas = (max(lista[i])-min(lista[i]))
    minimo_areas = min(lista[i])
    for j in range(0,len(lista[i]),1): # percorrer as frames/area por frame do individuo
        if(delta_areas!=0):
            lista[i][j] = round(((lista[i][j]-minimo_areas)/delta_areas),5)
        else:
            for k in range(0,len(lista[i]),1): lista[i][k] = 1.0 

print("INTERPOLAR - INTERPOLAR")
# interpolar as áreas
for i in lista:
    interpolada.append([])

    # casos em que o indivíduo aparece menos que "representante" frames (falta informação, vamos tentar obtê-la)
    if(len(i)<representantes):
        # mudar a forma dos arrays (-1 quer dizer "o número de linhas é o que tiver de ser" e o 1 quer dizer "1 coluna")
        aux = []
        if(len(i)==1):
            for j in range(0,representantes,1): aux.append(i[0])
            interpolada[len(interpolada)-1] = aux
            aux = []

        else:
            for j in range(0,len(i),1): aux.append(len(aux)+1)
            X = np.array(aux).reshape(-1, 1)
            Y = np.array(i).reshape(-1, 1)
            line = SG.LineString(list(zip(X,Y)))

            for j in range(0,representantes,1):
                if(j==0): x0 = 1.0
                else: x0 = round(contador+((len(aux)-1)/float(representantes-1)),5)
                if(x0>float(len(i)) or round(x0,1)==float(len(i))): x0 = float(len(i))
                contador = x0
                xline = SG.LineString([(x0, 0), (x0, max(Y))])
                coords = np.array(line.intersection(xline))
                interpolada[len(interpolada)-1].append(round(coords[1],5))
            '''
            fig = plt.figure()
            fig.suptitle("Dados artificiais")
            ax = plt.subplot(111)
            ax.plot(i,"bo",linestyle='-', marker='o', color='b',label='Original')
            ax.plot(interpolada[len(interpolada)-1],linestyle='-', marker='o', color='r', label="Expandido")
            ax.legend()
            plt.xlabel('Frames')
            plt.ylabel('Area (normalizada)')
            plt.savefig("/home/socialab/Desktop/interpolada.png")
            plt.show()
            sys.exit()
            '''
            contador = 1.0
            aux = []

    # caso ideal
    elif(len(i)==representantes):
        interpolada[len(interpolada)-1] = i

    # temos mais que "representantes" frames (vamos escolher "representantes" frames)  
    else:
        contador = 0.0
        for j in range(0,representantes,1):
            if(int(round(contador,5))==len(i)): contador = (len(i)-1)
            interpolada[len(interpolada)-1].append(round(i[int(round(contador,5))],5))
            contador += (len(i)/float(representantes-1))
        aux = []
        contador = 1.0

print("INTERPOLAR - NORMALIZAR")
# normalizar as áreas outra vez (para garantir que os intervalos interpolados ficam no intervalo [0,1])
for i in range(0,len(interpolada),1):
    delta_areas = (max(interpolada[i])-min(interpolada[i]))
    minimo_areas = min(interpolada[i])
    for j in range(0,len(interpolada[i]),1): # percorrer as frames/area por frame do individuo
        if(delta_areas!=0):
            interpolada[i][j] = round(((interpolada[i][j]-minimo_areas)/delta_areas),5)
        else:
            for k in range(0,len(interpolada[i]),1): interpolada[i][k] = 1.0 

# guardar tudo num ficheiro
f = open("areas_interpoladas.txt","w")
for i in range(0,len(interpolada),1):
    f.write(nomes[i] + " --- ")
    f.write(', '.join(map(str,interpolada[i])))
    f.write('\n')
########################################################################################################################
