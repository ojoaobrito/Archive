import os, sys
import natsort
import cv2
from shutil import rmtree

width_global = 60
height_global = 100

# redimensionar todas as imagens para um tamanho fixo

# VALIDACAO (AFASTA)
path = "grupos_redimensionados/validacao/afasta"
diretoria = os.listdir(path)

aux = 1
contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

for i in diretoria:
    if(i[0]=="."): continue
    sequencia = os.listdir(path + "/" + i)
    sequencia = natsort.natsorted(sequencia,reverse=False)
    print("REDIMENSIONAR - VALIDACAO - AFASTA (" + str(aux) + "/" + str(contador) + ")")
    aux += 1
    for j in sequencia:
        if(j[0]=="." or j=="1escolha.txt"): continue
        try:
            imagem_original = cv2.imread(path + "/" + i + "/" + j, cv2.IMREAD_COLOR)
            height, width, _ = imagem_original.shape
            # caso ideal
            if (width == width_global and height == height_global): continue
            # usar os algoritmos mais otimizados para aumentar e diminuir o tamanho da imagem original
            if ((width * height) < (width_global * height_global)):
                imagem_alterada = cv2.resize(imagem_original, (width_global, height_global), interpolation=cv2.INTER_CUBIC)
            else:
                imagem_alterada = cv2.resize(imagem_original, (width_global, height_global), interpolation=cv2.INTER_AREA)
            cv2.imwrite(path + "/" + i + "/" + j, imagem_alterada)
        except:
            rmtree(path + "/" + i)
            break

print("REDIMENSIONAR - VALIDACAO - AFASTA (DONE!)")

# VALIDACAO (APROXIMA)
path = "grupos_redimensionados/validacao/aproxima"
diretoria = os.listdir(path)

aux = 1
contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

for i in diretoria:
    if(i[0]=="."): continue
    sequencia = os.listdir(path + "/" + i)
    sequencia = natsort.natsorted(sequencia,reverse=False)
    print("REDIMENSIONAR - VALIDACAO - APROXIMA (" + str(aux) + "/" + str(contador) + ")")
    aux += 1
    for j in sequencia:
        if(j[0]=="." or j=="1escolha.txt"): continue
        try:
            imagem_original = cv2.imread(path + "/" + i + "/" + j, cv2.IMREAD_COLOR)
            height, width, _ = imagem_original.shape
            # caso ideal
            if (width == width_global and height == height_global): continue
            # usar os algoritmos mais otimizados para aumentar e diminuir o tamanho da imagem original
            if ((width * height) < (width_global * height_global)):
                imagem_alterada = cv2.resize(imagem_original, (width_global, height_global), interpolation=cv2.INTER_CUBIC)
            else:
                imagem_alterada = cv2.resize(imagem_original, (width_global, height_global), interpolation=cv2.INTER_AREA)
            cv2.imwrite(path + "/" + i + "/" + j, imagem_alterada)
        except:
            rmtree(path + "/" + i)
            break

print("REDIMENSIONAR - VALIDACAO - APROXIMA (DONE!)")

# VALIDACAO (LATERAL)
path = "grupos_redimensionados/validacao/lateral"
diretoria = os.listdir(path)

aux = 1
contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

for i in diretoria:
    if(i[0]=="."): continue
    sequencia = os.listdir(path + "/" + i)
    sequencia = natsort.natsorted(sequencia,reverse=False)
    print("REDIMENSIONAR - VALIDACAO - LATERAL (" + str(aux) + "/" + str(contador) + ")")
    aux += 1
    for j in sequencia:
        if(j[0]=="." or j=="1escolha.txt"): continue
        try:
            imagem_original = cv2.imread(path + "/" + i + "/" + j, cv2.IMREAD_COLOR)
            height, width, _ = imagem_original.shape
            # caso ideal
            if (width == width_global and height == height_global): continue
            # usar os algoritmos mais otimizados para aumentar e diminuir o tamanho da imagem original
            if ((width * height) < (width_global * height_global)):
                imagem_alterada = cv2.resize(imagem_original, (width_global, height_global), interpolation=cv2.INTER_CUBIC)
            else:
                imagem_alterada = cv2.resize(imagem_original, (width_global, height_global), interpolation=cv2.INTER_AREA)
            cv2.imwrite(path + "/" + i + "/" + j, imagem_alterada)
        except:
            rmtree(path + "/" + i)
            break

print("REDIMENSIONAR - VALIDACAO - LATERAL (DONE!)")
print("REDIMENSIONAR - VALIDACAO (DONE!)")
