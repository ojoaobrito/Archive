import sys, os
from shutil import copyfile
import natsort 
from random import randint

if(not os.path.exists("grupos")): os.makedirs("grupos")

# VALIDACAO (AFASTA)
diretoria = os.listdir("grupos_interpolados/validacao/afasta")
diretoria = natsort.natsorted(diretoria,reverse=False)

num_erradas = 0
escolhidas = []
num_seq = 0
diferentes = 0

# avaliar quantas sequências únicas existem
for i in diretoria:
    if(("X" not in i) and (i[0]!=".") and ("_" not in i)): diferentes += 1

for i in diretoria:
    if(("X" not in i) and (i[0]!=".")): num_seq += 1

print("AFASTA")
aux = 1
if(diferentes>1):
    for i in diretoria:
        if((i + "X") in diretoria): continue
        if(("X" not in i) and i[0]!="."):
            print("ERRADAS - AFASTA (" + str(aux) + "/" + str(num_seq) + ")")
            aux += 1
            if(not os.path.exists("grupos_interpolados/validacao/afasta/" + i + "X")): os.makedirs("grupos_interpolados/validacao/afasta/" + i + "X")

            # escolher a patch a trocar
            _, _, files = next(os.walk("grupos_interpolados/validacao/afasta/" + i))
            tamanho = len(files)

            # sortear o número de patches a trocar
            if(tamanho==1): continue
            elif(tamanho==2): num_erradas = 1
            else: num_erradas = randint(1,2)

            dir_original = natsort.natsorted((os.listdir("grupos_interpolados/validacao/afasta/" + i)),reverse=False)
            escolhidas = []
            # mover todas as outras patches da diretoria original para a pasta "X"
            for k in dir_original:
                nome_aux = k.split(")")[0]
                nome_aux2 = k.split(")")[1]
                copyfile("grupos_interpolados/validacao/afasta/" + i + "/" + k, "grupos_interpolados/validacao/afasta/" + i + "X/" + nome_aux + "X)" + nome_aux2)

            for count in range(0,num_erradas,1):

                # escolher a patch a trocar
                escolha = round((randint(1,tamanho))/float(tamanho),5)
                while(escolha in escolhidas): 
                    escolha = round((randint(1,tamanho))/float(tamanho),5)
                escolhidas.append(escolha)

                # sortear uma das sequências candidatas
                if(count==0):
                    indice_escolhido = randint(0,num_seq-1)
                    atual = diretoria.index(i)
                    while(indice_escolhido==atual or ("_" in diretoria[indice_escolhido])): indice_escolhido = randint(0,num_seq-1)
                    dir_escolhida_aux = diretoria[indice_escolhido]

                # patch originais
                if(int(escolha*tamanho)>=tamanho): ficheiro_original = dir_original[tamanho-1]
                else: ficheiro_original = dir_original[int(escolha*tamanho)]

                nome_aux = ficheiro_original.split(")")[0]
                nome_aux2 = ficheiro_original.split(")")[1]
                ficheiro_original = nome_aux + "X)" + nome_aux2

                # mover a patch escolhida para a diretoria "X" com o nome do ficheiro original
                dir_escolhida = os.listdir("grupos_interpolados/validacao/afasta/" + dir_escolhida_aux)
                if(int(escolha*len(dir_escolhida))>=len(dir_escolhida)):
                    copyfile("grupos_interpolados/validacao/afasta/" + dir_escolhida_aux + "/" + dir_escolhida[len(dir_escolhida)-1], "grupos_interpolados/validacao/afasta/" + i + "X/" + ficheiro_original)        

                else:
                    copyfile("grupos_interpolados/validacao/afasta/" + dir_escolhida_aux + "/" + dir_escolhida[int(escolha*len(dir_escolhida))], "grupos_interpolados/validacao/afasta/" + i + "X/" + ficheiro_original)          

print("AFASTA - DONE!")

# VALIDACAO (APROXIMA)
diretoria = os.listdir("grupos_interpolados/validacao/aproxima")
diretoria = natsort.natsorted(diretoria,reverse=False)

# avaliar quantas sequências únicas existem
diferentes = 0
for i in diretoria:
    if(("X" not in i) and (i[0]!=".") and ("_" not in i)): diferentes += 1

num_erradas = 0
num_seq = 0

for i in diretoria:
    if(("X" not in i) and (i[0]!=".")): num_seq += 1

print("APROXIMA")
aux = 1
if(diferentes>1):
    for i in diretoria:
        if((i + "X") in diretoria): continue
        if(("X" not in i) and i[0]!="."):
            print("ERRADAS - APROXIMA (" + str(aux) + "/" + str(num_seq) + ")")
            aux += 1
            if(not os.path.exists("grupos_interpolados/validacao/aproxima/" + i + "X")): os.makedirs("grupos_interpolados/validacao/aproxima/" + i + "X")

            # escolher a patch a trocar
            _, _, files = next(os.walk("grupos_interpolados/validacao/aproxima/" + i))
            tamanho = len(files)

            # sortear o número de patches a trocar
            if(tamanho==1): continue
            elif(tamanho==2): num_erradas = 1
            else: num_erradas = randint(1,2)

            dir_original = natsort.natsorted((os.listdir("grupos_interpolados/validacao/aproxima/" + i)),reverse=False)
            escolhidas = []
            # mover todas as outras patches da diretoria original para a pasta "X"
            for k in dir_original:
                nome_aux = k.split(")")[0]
                nome_aux2 = k.split(")")[1]
                copyfile("grupos_interpolados/validacao/aproxima/" + i + "/" + k, "grupos_interpolados/validacao/aproxima/" + i + "X/" + nome_aux + "X)" + nome_aux2)

            for count in range(0,num_erradas,1):

                # escolher a patch a trocar
                escolha = round((randint(1,tamanho))/float(tamanho),5)
                while(escolha in escolhidas): 
                    escolha = round((randint(1,tamanho))/float(tamanho),5)
                escolhidas.append(escolha)

                # sortear uma das sequências candidatas
                if(count==0):
                    indice_escolhido = randint(0,num_seq-1)
                    atual = diretoria.index(i)
                    while(indice_escolhido==atual or ("_" in diretoria[indice_escolhido])): indice_escolhido = randint(0,num_seq-1)
                    dir_escolhida_aux = diretoria[indice_escolhido]

                # patch originais
                if(int(escolha*tamanho)>=tamanho): ficheiro_original = dir_original[tamanho-1]
                else: ficheiro_original = dir_original[int(escolha*tamanho)]

                nome_aux = ficheiro_original.split(")")[0]
                nome_aux2 = ficheiro_original.split(")")[1]
                ficheiro_original = nome_aux + "X)" + nome_aux2

                # mover a patch escolhida para a diretoria "X" com o nome do ficheiro original
                dir_escolhida = os.listdir("grupos_interpolados/validacao/aproxima/" + dir_escolhida_aux)
                if(int(escolha*len(dir_escolhida))>=len(dir_escolhida)):
                    copyfile("grupos_interpolados/validacao/aproxima/" + dir_escolhida_aux + "/" + dir_escolhida[len(dir_escolhida)-1], "grupos_interpolados/validacao/aproxima/" + i + "X/" + ficheiro_original)        

                else:
                    copyfile("grupos_interpolados/validacao/aproxima/" + dir_escolhida_aux + "/" + dir_escolhida[int(escolha*len(dir_escolhida))], "grupos_interpolados/validacao/aproxima/" + i + "X/" + ficheiro_original)           

print("APROXIMA - DONE!")

# VALIDACAO (LATERAL)
diretoria = os.listdir("grupos_interpolados/validacao/lateral")
diretoria = natsort.natsorted(diretoria,reverse=False)

# avaliar quantas sequências únicas existem
diferentes = 0
for i in diretoria:
    if(("X" not in i) and (i[0]!=".") and ("_" not in i)): diferentes += 1

num_erradas = 0
num_seq = 0

for i in diretoria:
    if(("X" not in i) and (i[0]!=".")): num_seq += 1

print("LATERAL")
aux = 1
if(diferentes>1):
    for i in diretoria:
        if((i + "X") in diretoria): continue
        if(("X" not in i) and i[0]!="."):
            print("ERRADAS - LATERAL (" + str(aux) + "/" + str(num_seq) + ")")
            aux += 1
            if(not os.path.exists("grupos_interpolados/validacao/lateral/" + i + "X")): os.makedirs("grupos_interpolados/validacao/lateral/" + i + "X")

            # escolher a patch a trocar
            _, _, files = next(os.walk("grupos_interpolados/validacao/lateral/" + i))
            tamanho = len(files)

            # sortear o número de patches a trocar
            if(tamanho==1): continue
            elif(tamanho==2): num_erradas = 1
            else: num_erradas = randint(1,2)

            dir_original = natsort.natsorted((os.listdir("grupos_interpolados/validacao/lateral/" + i)),reverse=False)
            escolhidas = []
            # mover todas as outras patches da diretoria original para a pasta "X"
            for k in dir_original:
                nome_aux = k.split(")")[0]
                nome_aux2 = k.split(")")[1]
                copyfile("grupos_interpolados/validacao/lateral/" + i + "/" + k, "grupos_interpolados/validacao/lateral/" + i + "X/" + nome_aux + "X)" + nome_aux2)

            for count in range(0,num_erradas,1):

                # escolher a patch a trocar
                escolha = round((randint(1,tamanho))/float(tamanho),5)
                while(escolha in escolhidas): 
                    escolha = round((randint(1,tamanho))/float(tamanho),5)
                escolhidas.append(escolha)

                # sortear uma das sequências candidatas
                if(count==0):
                    indice_escolhido = randint(0,num_seq-1)
                    atual = diretoria.index(i)
                    while(indice_escolhido==atual or ("_" in diretoria[indice_escolhido])): indice_escolhido = randint(0,num_seq-1)
                    dir_escolhida_aux = diretoria[indice_escolhido]

                # patch originais
                if(int(escolha*tamanho)>=tamanho): ficheiro_original = dir_original[tamanho-1]
                else: ficheiro_original = dir_original[int(escolha*tamanho)]

                nome_aux = ficheiro_original.split(")")[0]
                nome_aux2 = ficheiro_original.split(")")[1]
                ficheiro_original = nome_aux + "X)" + nome_aux2
                
                # mover a patch escolhida para a diretoria "X" com o nome do ficheiro original
                dir_escolhida = os.listdir("grupos_interpolados/validacao/lateral/" + dir_escolhida_aux)
                if(int(escolha*len(dir_escolhida))>=len(dir_escolhida)):
                    copyfile("grupos_interpolados/validacao/lateral/" + dir_escolhida_aux + "/" + dir_escolhida[len(dir_escolhida)-1], "grupos_interpolados/validacao/lateral/" + i + "X/" + ficheiro_original)        

                else:
                    copyfile("grupos_interpolados/validacao/lateral/" + dir_escolhida_aux + "/" + dir_escolhida[int(escolha*len(dir_escolhida))], "grupos_interpolados/validacao/lateral/" + i + "X/" + ficheiro_original)         
  
print("LATERAL - DONE!")
print("ERRADAS - DONE!")
