import os, sys, csv, cv2
from PIL import Image
import math
import natsort
from shutil import copyfile
import random

from get_carateristicas import get_carateristicas
from get_carateristicas import distancia_carateristicas

def mesma_sequencia(dir1,dir2):

    if(dir1==dir2): return(True)

    if("_" in dir1):
        if(dir1.split("_")[0]==dir2): return(True)
    
    if("_" in dir2):
        if(dir2.split("_")[0]==dir1): return(True)
 
    if("_" in dir1 and "_" in dir2):
        if((dir1.split("_")[0])==(dir2.split("_")[0])): return(True)

    return(False)

def esqueleto(imagem1, imagem2): # função que calcula a distância euclidiana em termos de esqueleto

    distancia = 0.0

    for i in range(0,len(imagem1),1):
        distancia += (math.sqrt(((imagem1[i][0]-imagem2[i][0])**2) + ((imagem1[i][1]-imagem2[i][1])**2)))

    return(distancia)

def distancia(imagem1, imagem2): # função que calcula a distância euclidiana em termos de cor de roupa
    
    distancia = 0.0

    for i in range(0,len(imagem1),1):
        distancia += (math.sqrt(((imagem1[i][0]-imagem2[i][0])**2) + ((imagem1[i][1]-imagem2[i][1])**2) + ((imagem1[i][2]-imagem2[i][2])**2)))

    return(distancia)

def melhor_individuo(nome_original, path, diretoria_original):

    # variáveis principais
    peso_cor = 80
    peso_extras = 20
    num_amostras = 3 # número de imagens de um indivíduo usadas para determinar a distância em termos de cor
    final = []
    distancia_cor = []
    distancia_extras = []
    carateristicas = get_carateristicas(nome_original) # lista com as carateristicas da imagem original

    imagem1_cor = []

    ## OBTER AS INFORMAÇÕES DE COR DA IMAGEM ORIGINAL
    ##############################################################################################################################################

    # obter a informação de cor da imagem original
    imagem_info = Image.open(path + diretoria_original + "/" + path.split("/")[2] + "-" + diretoria_original + ")" + nome_original + ".jpg")
    pix = imagem_info.load()

    try:
        contador = 1
        with open("Poses/Elements/Datasets/Surveillance/BIODI/pose_patches_constantProp/" + nome_original + ".csv") as ficheiro:
            reader = list(csv.reader(ficheiro,delimiter=','))
            # obter a informação de cor
            for i in range(0,len(reader),1):
                # obter pontos intermédios (se forem proveitosos)
                if(not(contador==3 or contador==6 or contador==8 or contador==9 or contador==10 or contador==13 or contador==16)):
                    valores = (pix[int((int(float(reader[i][0])) + int(float(reader[i+1][0])))/2),int((int(float(reader[i][1])) + int(float(reader[i+1][1])))/2)])
                    valores_aux = []
                    valores_aux.append(valores[0])
                    valores_aux.append(valores[1])
                    valores_aux.append(valores[2])
                    imagem1_cor.append(valores_aux)
                    
                # pontos normais
                valores = (pix[int(float(reader[i][0])),int(float(reader[i][1]))])
                valores_aux = []
                valores_aux.append(valores[0])
                valores_aux.append(valores[1])
                valores_aux.append(valores[2])
                imagem1_cor.append(valores_aux)
                contador += 1
    except:
        return(["ERRO",0])
    ##############################################################################################################################################

    imagem_atual = 1
    contador = 0
    carateristicas_aux = []
    imagem_cor = []
    erro = False
    stop = False

    ## OBTER AS DISTÂNCIAS DE COR DE ROUPA E EXTRAS DE CADA INDIVÍDUO
    ##############################################################################################################################################
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)

    for i in diretoria:
        if(not stop):
            if(i[0]=="." or "X" in i or "_" in i): continue
            # print("Original: " + diretoria_original + " Atual: " + i + " " + str(mesma_sequencia(i,diretoria_original)))
            if(mesma_sequencia(i,diretoria_original)==True): continue
            # print(str(imagem_atual))
            imagem_atual += 1

            sequencias = os.listdir(path + i)
            sequencias = natsort.natsorted(sequencias, reverse=False)

            distancia_cor.append([path + i,0.0])
            distancia_extras.append([path + i,0.0])

            tamanho = 0

            for j in sequencias:
                if(j[0]!="."): tamanho += 1

            # escolher as imagens a analisar
            imagens_interpoladas = []
            for j in range(0,num_amostras,1): imagens_interpoladas.append(int(round(j*((tamanho-1)/(num_amostras-1)),0)))
            
            # percorrer as imagens
            for j in imagens_interpoladas:
                if((sequencias[j])[0]!="."):

                    # ainda não chegámos ao painél desejado
                    if(((((sequencias[j]).split(")")[1]).split("_")[0])[0]).upper()<((nome_original.split("_")[0])[0]).upper()):
                        erro = False
                        contador = 0
                        break

                    # todos os painéis que estão por ser analisados não interessam
                    if((((((sequencias[j]).split(")")[1])).split("_")[0])[0]).upper()>((nome_original.split("_")[0])[0]).upper()): 
                        stop = True
                        distancia_cor = distancia_cor[:-1]
                        distancia_extras = distancia_extras[:-1]
                        break

                    try:
                        # painéis diferentes
                        if(((((sequencias[j]).split(")")[1])).split("_")[0])!=(nome_original.split("_")[0])): raise Exception

                        carateristicas_aux = get_carateristicas((((sequencias[j]).split(")")[1])).split(".")[0])
                        
                        # géneros diferentes
                        if(carateristicas_aux[0][0]!=carateristicas[0][0]): raise Exception

                        # obter a informação de cor da imagem
                        imagem_info = Image.open(path + i + "/" + sequencias[j])
                        pix = imagem_info.load()
                        contador = 1
                        with open("Poses/Elements/Datasets/Surveillance/BIODI/pose_patches_constantProp/" + (((sequencias[j]).split(")")[1])).split(".")[0] + ".csv") as ficheiro:
                            reader = list(csv.reader(ficheiro,delimiter=','))
                            # obter a informação de cor
                            for k in range(0,len(reader),1):
                                # obter pontos intermédios (se forem proveitosos)
                                if(not(contador==3 or contador==6 or contador==8 or contador==9 or contador==10 or contador==13 or contador==16)):
                                    valores = (pix[int((int(float(reader[k][0])) + int(float(reader[k+1][0])))/2),int((int(float(reader[k][1])) + int(float(reader[k+1][1])))/2)])
                                    valores_aux = []
                                    valores_aux.append(valores[0])
                                    valores_aux.append(valores[1])
                                    valores_aux.append(valores[2])
                                    imagem_cor.append(valores_aux)

                                # pontos normais
                                valores = (pix[int(float(reader[k][0])),int(float(reader[k][1]))])
                                valores_aux = []
                                valores_aux.append(valores[0])
                                valores_aux.append(valores[1])
                                valores_aux.append(valores[2])
                                imagem_cor.append(valores_aux)
                                contador += 1
                        
                        # obter as distâncias
                        distancia_cor[len(distancia_cor)-1][1] += distancia(imagem1_cor,imagem_cor)
                        distancia_extras[len(distancia_extras)-1][1] += distancia_carateristicas(carateristicas,carateristicas_aux)
                        
                        contador += 1
                        imagem_cor = []
                    
                    # qualquer tipo de erro
                    except:
                        distancia_cor = distancia_cor[:-1]
                        distancia_extras = distancia_extras[:-1]
                        erro = True
                        break
            
            # guardar apenas a média das distâncias das patches de cada indivíduo
            if(not erro):
                if(contador==0):
                    distancia_cor = distancia_cor[:-1]
                    distancia_extras = distancia_extras[:-1]
                else:
                    distancia_cor[len(distancia_cor)-1][1] = ((distancia_cor[len(distancia_cor)-1][1])/contador)
                    distancia_extras[len(distancia_extras)-1][1] = ((distancia_extras[len(distancia_extras)-1][1])/contador)
            contador = 0
            erro = False

        else: break
    ##############################################################################################################################################

    if(len(distancia_cor)==0):
        return(["ERRO",0])
    if(len(distancia_extras)==0):
        return (["ERRO", 0])

    ## OBTER O COEFICIENTE DE SEMELHANÇA
    ##############################################################################################################################################
    def funcao_auxiliar(elemento): # função que simplesmente devolve o 2º elemento (critério de ordenação)
        return (elemento[1])

    # ordenar a lista das distâncias de cor
    distancia_cor.sort(key=funcao_auxiliar, reverse=True)

    # gerar uma lista de coeficientes (para a cor de roupa)
    coeficientes = []
    if(len(distancia_cor)==1): coeficientes.append(peso_cor)
    else:
        for i in range(0,len(distancia_cor),1): coeficientes.append(i*(float(peso_cor)/(len(distancia_cor)-1)))

    # atribuir os coeficientes aos indivíduos, em termos de cor de roupa
    for i in range(0,len(distancia_cor),1):
        final.append([distancia_cor[i][0],coeficientes[i]]) 

    # ordenar a lista das distâncias de extras
    distancia_extras.sort(key=funcao_auxiliar, reverse=True)

    # gerar uma lista de coeficientes (para os extras)
    coeficientes = []
    if(len(distancia_extras)==1): coeficientes.append(peso_extras)
    else:
        for i in range(0,len(distancia_extras),1): coeficientes.append(i*(float(peso_extras)/(len(distancia_extras)-1)))

    # atribuir os coeficientes aos indivíduos, em termos de extras
    for i in range(0,len(distancia_extras),1):
        for j in range(0,len(final),1):
            if(final[j][0]==distancia_extras[i][0]):
                final[j][1] += coeficientes[i]
                break

    # finalmente, ordenar os coeficientes
    final.sort(key=funcao_auxiliar, reverse=True)
    return(final[0])
    ##############################################################################################################################################

def patches(escolhidas, imagem1, individuo, individuo_original):

    vencedor = []
    pontos = []
    aux = 0.0
    imagem1_esqueleto = []

    ## OBTER AS INFORMAÇÕES DE ESQUELETO DA IMAGEM ORIGINAL
    ##############################################################################################################################################
    # obter as dimensões da imagem original
    imagem_original = cv2.imread(individuo_original + "/" + individuo_original.split("/")[-2] + "-" + individuo_original.split("/")[-1] + ")" + imagem1 + ".jpg",cv2.IMREAD_COLOR)
    height, width, _ = imagem_original.shape

    try:
        with open("Poses/Elements/Datasets/Surveillance/BIODI/pose_patches_constantProp/" + imagem1 + ".csv") as ficheiro:
            reader = csv.reader(ficheiro,delimiter=',')
            for row in reader:
                imagem1_esqueleto.append([float(row[0])/width,float(row[1])/height])
    except:
        return(["ERRO",0])
    ##############################################################################################################################################

    ## AVALIAR OS ESQUELETOS DO INDIVÍDUO COM MELHOR COEFICIENTE
    ##############################################################################################################################################
    sequencias = os.listdir(individuo)
    sequencias = natsort.natsorted(sequencias, reverse=False)

    # se nenhuma das frames do individuo tiver dados de esqueleto, retornamos uma aleatória
    _, _, files = next(os.walk(individuo))
    tamanho = len(files)

    escolhido_default = sequencias[random.randint(0,tamanho-1)]
    vencedor = [individuo + "/" + escolhido_default,100000000.0]

    for j in sequencias:
        if(j[0]=="." or j in escolhidas): continue

        # obter as dimensões da imagem
        imagem = cv2.imread(individuo + "/" + j,cv2.IMREAD_COLOR)
        height, width, _ = imagem.shape
        try:
            contador = 1
            with open("Poses/Elements/Datasets/Surveillance/BIODI/pose_patches_constantProp/" + (j.split(")")[1]).split(".")[0] + ".csv") as ficheiro:
                reader = list(csv.reader(ficheiro,delimiter=','))
                # obter a informação de esqueleto
                for i in range(0,len(reader),1):
                    if(float(reader[i][0])<0.0 or float(reader[i][1])<0.0): raise Exception
                    # obter pontos intermédios (se forem proveitosos e/ou possíveis)
                    if(not(contador==3 or contador==6 or contador==8 or contador==9 or contador==10 or contador==13 or contador==16)):
                        pontos.append([((float(reader[i][0]) + float(reader[i+1][0]))/2)/width,((float(reader[i][1]) + float(reader[i+1][1]))/2)/height])
    
                    pontos.append([float(reader[i][0])/width,float(reader[i][1])/height])
                    contador += 1
                    
            aux = esqueleto(imagem1_esqueleto,pontos)
            if(aux<vencedor[1]): vencedor = [individuo + "/" + j,aux]
            pontos = []
        
        # qualquer tipo de erro
        except:
            pontos = []
            continue
    return(vencedor)
    ##############################################################################################################################################
