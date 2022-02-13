import sys, os
from shutil import copyfile
from shutil import rmtree
import natsort
from random import randint

from pontos_pose import melhor_individuo
from pontos_pose import patches

if(not os.path.exists("grupos")): os.makedirs("grupos")

# TREINO (APROXIMA)
diretoria = os.listdir("grupos_interpolados/treino/aproxima")
diretoria = natsort.natsorted(diretoria,reverse=False)

# avaliar quantas sequências únicas existem
diferentes = 0
for i in diretoria:
    if(("X" not in i) and (i[0]!=".") and ("_" not in i)): diferentes += 1

num_erradas = 0
num_seq = 0

for i in diretoria:
    if(("X" not in i) and (i[0]!=".")): num_seq += 1

aux = 1
if(diferentes>1):
    for i in diretoria:
        if(((i + "X") in diretoria)): continue
        if(("X" not in i) and i[0]!="."):
            print("ERRADAS - TREINO - APROXIMA (" + str(aux) + "/" + str(num_seq) + ")")
            aux += 1

            if(not os.path.exists("grupos_interpolados/treino/aproxima/" + i + "X")): os.makedirs("grupos_interpolados/treino/aproxima/" + i + "X")

            ficheiro = open("grupos_interpolados/treino/aproxima/" + i + "X/1escolha.txt","w")

            _, _, files = next(os.walk("grupos_interpolados/treino/aproxima/" + i))
            tamanho = len(files)

            # sortear o número de patches a trocar
            if(tamanho==1): continue
            elif(tamanho==2): num_erradas = 1
            else: num_erradas = randint(1,2)

            dir_original = natsort.natsorted((os.listdir("grupos_interpolados/treino/aproxima/" + i)),reverse=False)
            escolhidas = []
            
            # mover todas as outras patches da diretoria original para a pasta "X"
            for k in dir_original:
                nome_aux = k.split(")")[0]
                nome_aux2 = k.split(")")[1]
                copyfile("grupos_interpolados/treino/aproxima/" + i + "/" + k, "grupos_interpolados/treino/aproxima/" + i + "X/" + nome_aux + "X)" + nome_aux2)

            # escolher a patch a trocar
            escolha = round((randint(1,tamanho))/float(tamanho),5)
            while(escolha in escolhidas or escolha==0): 
                escolha = round((randint(1,tamanho))/float(tamanho),5)
            escolhidas.append(escolha)

            melhor = []

            # obter o melhor indivíduo para trocar patches
            if(int(escolha*tamanho)>=tamanho):
                melhor = melhor_individuo(((dir_original[tamanho-1]).split(".")[0]).split(")")[1],"grupos_interpolados/treino/aproxima/",i)
            
            else:
                melhor = melhor_individuo(((dir_original[int(escolha*tamanho)]).split(".")[0]).split(")")[1],"grupos_interpolados/treino/aproxima/",i)

            # erro ao tentar obter o melhor indivíduo para trocar patches
            if(melhor[0]=="ERRO"):
                rmtree("grupos_interpolados/treino/aproxima/" + i + "X")
                continue

            atual = []
            ficheiro.write(melhor[0] + " (" + str(melhor[1]) + ")")
            ficheiro.close()

            # trocar as "num_erradas" patches
            for count in range(0,num_erradas,1):

                if(int(escolha*tamanho)>=tamanho):
                    atual = patches(escolhidas, ((dir_original[tamanho-1]).split(".")[0]).split(")")[1], melhor[0], "grupos_interpolados/treino/aproxima/" + i)
                
                else:
                    atual = patches(escolhidas, ((dir_original[int(escolha*tamanho)]).split(".")[0]).split(")")[1], melhor[0], "grupos_interpolados/treino/aproxima/" + i)

                # erro ao tentar obter as patches
                if(atual[0]=="ERRO"):
                    rmtree("grupos_interpolados/treino/aproxima/" + i + "X")
                    break

                # patch original
                if(int(escolha*tamanho)>=tamanho): ficheiro_original = dir_original[tamanho-1]
                else: ficheiro_original = dir_original[int(escolha*tamanho)]

                nome_aux = ficheiro_original.split(")")[0]
                nome_aux2 = ficheiro_original.split(")")[1]
                ficheiro_original = nome_aux + "X)" + nome_aux2

                copyfile(atual[0], "grupos_interpolados/treino/aproxima/" + i + "X/" + ficheiro_original)

                # escolher outra patch a trocar
                escolha = round((randint(1,tamanho))/float(tamanho),5)
                while(escolha in escolhidas or escolha==0): 
                    escolha = round((randint(1,tamanho))/float(tamanho),5)
                escolhidas.append(escolha)

                atual = []

            escolhidas = []

print("ERRADAS - TREINO - APROXIMA (DONE!)")
print("ERRADAS - TREINO (DONE!)")