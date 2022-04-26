import os, sys
import natsort
import random
from shutil import copyfile, copytree, rmtree
import itertools

## CONFIGURAÇÕES INICIAIS
#####################################################################################################################################################################################################################################################################################
if(os.path.exists("grupos_errados/teste")): rmtree("grupos_errados/teste")
os.makedirs("grupos_errados/teste")
diretoria = os.listdir("grupos/teste")

def get_candidates(gender,atual): # obter os indivíduos candidatos para trocar imagens

    final = []
    global diretoria

    for i in diretoria:
        if(i[0]!="."):
            _,_,files = next(os.walk("grupos/teste/" + i))
            if(gender==files[0][0] and i!=atual): final.append(i)
    return(final)

diretoria = natsort.natsorted(diretoria,reverse=False)

path = "grupos_errados/teste/"
num_individuos = len(diretoria)-1
contador = 1
limite_26 = 300
#####################################################################################################################################################################################################################################################################################

## GERAR AS INSTÂNCIAS ERRADAS
#####################################################################################################################################################################################################################################################################################
for i in diretoria:
    if(i[0]=="."): continue
    print("ERRADAS - TESTE (" + str(contador) + "/" + str(num_individuos) + ")")
    contador += 1
    _,_,files = next(os.walk("grupos/teste/" + i))

    if(len(files)==12):
        # sequências certas
        combinations = list(itertools.permutations(files, 2))
        for j in range(0,len(combinations),1):
            if(not os.path.exists("grupos_errados/teste/" + i + "_" + str(j+1))): os.makedirs("grupos_errados/teste/" + i + "_" + str(j+1))
            copyfile("grupos/teste/" + i + "/" + combinations[j][0],"grupos_errados/teste/" + i + "_" + str(j+1) + "/" + i + "_" + str(j+1) + ")"  + combinations[j][0])
            copyfile("grupos/teste/" + i + "/" + combinations[j][1],"grupos_errados/teste/" + i + "_" + str(j+1) + "/" + i + "_" + str(j+1) + ")" + combinations[j][1])
        
        # sequências erradas
        if("m"==files[0][0]): candidatos = get_candidates("m",i)
        else: candidatos = get_candidates("w",i)
        for j in range(0,len(combinations),1):
            copytree("grupos_errados/teste/" + i + "_" + str(j+1),"grupos_errados/teste/" + i + "_" + str(j+1) + "X")
            _,_,sequencia = next(os.walk("grupos_errados/teste/" + i + "_" + str(j+1)))
            trocar = sequencia[random.randint(0,1)]
            os.rename("grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + sequencia[len(sequencia)-1-sequencia.index(trocar)], "grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + i + "_" + str(j+1) + "X)" + sequencia[len(sequencia)-1-sequencia.index(trocar)].split(")")[1])
            individuo = 0

            # trocar a imagem escolhida pela equivalente de outro indivíduo
            if("m" in trocar): # homem
                individuo = random.randint(0,len(candidatos)-1)
                _,_,fotos_individuo = next(os.walk("grupos/teste/" + str(candidatos[individuo])))
                for k in fotos_individuo:
                    if(k[0]!="."):
                        if(((k.split(".")[0]).split("-")[2])==((trocar.split(".")[0]).split("-")[2])):
                            os.remove("grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + trocar)
                            copyfile("grupos/teste/" + str(candidatos[individuo]) + "/" + k,"grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + i + "_" + str(j+1) + "X)" + k)
                            break
            else: # mulher
                individuo = random.randint(0,len(candidatos)-1)
                _,_,fotos_individuo = next(os.walk("grupos/teste/" + str(candidatos[individuo])))
                for k in fotos_individuo:
                    if(k[0]!="."):
                        if(((k.split(".")[0]).split("-")[2])==((trocar.split(".")[0]).split("-")[2])):
                            os.remove("grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + trocar)
                            copyfile("grupos/teste/" + str(candidatos[individuo]) + "/" + k,"grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + i + "_" + str(j+1) + "X)" + k)
                            break
    
    else:
        # sequências certas
        combinations = list(itertools.permutations(files, 2))
        for j in range(0,limite_26,1):
            if(not os.path.exists("grupos_errados/teste/" + i + "_" + str(j+1))): os.makedirs("grupos_errados/teste/" + i + "_" + str(j+1))
            copyfile("grupos/teste/" + i + "/" + combinations[j][0],"grupos_errados/teste/" + i + "_" + str(j+1) + "/" + i + "_" + str(j+1) + ")" + combinations[j][0])
            copyfile("grupos/teste/" + i + "/" + combinations[j][1],"grupos_errados/teste/" + i + "_" + str(j+1) + "/" + i + "_" + str(j+1) + ")" + combinations[j][1])
        
        # sequências erradas
        if("m"==files[0][0]): candidatos = get_candidates("m",i)
        else: candidatos = get_candidates("w",i)
        for j in range(0,limite_26,1):
            copytree("grupos_errados/teste/" + i + "_" + str(j+1),"grupos_errados/teste/" + i + "_" + str(j+1) + "X")
            _,_,sequencia = next(os.walk("grupos_errados/teste/" + i + "_" + str(j+1) + "X"))
            trocar = sequencia[random.randint(0,1)]
            os.rename("grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + sequencia[len(sequencia)-1-sequencia.index(trocar)], "grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + i + "_" + str(j+1) + "X)" + sequencia[len(sequencia)-1-sequencia.index(trocar)].split(")")[1])
            individuo = 0

            # trocar a imagem escolhida pela equivalente de outro indivíduo
            if("m" in trocar): # homem
                individuo = random.randint(0,len(candidatos)-1)
                _,_,fotos_individuo = next(os.walk("grupos/teste/" + str(candidatos[individuo])))
                for k in fotos_individuo:
                    if(k[0]!="."):
                        if(((k.split(".")[0]).split("-")[2])==((trocar.split(".")[0]).split("-")[2])):
                            os.remove("grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + trocar)
                            copyfile("grupos/teste/" + str(candidatos[individuo]) + "/" + k,"grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + i + "_" + str(j+1) + "X)" + k)
                            break
            else: # mulher
                individuo = random.randint(0,len(candidatos)-1)
                _,_,fotos_individuo = next(os.walk("grupos/teste/" + str(candidatos[individuo])))
                for k in fotos_individuo:
                    if(k[0]!="."):
                        if(((k.split(".")[0]).split("-")[2])==((trocar.split(".")[0]).split("-")[2])):
                            os.remove("grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + trocar)
                            copyfile("grupos/teste/" + str(candidatos[individuo]) + "/" + k,"grupos_errados/teste/" + i + "_" + str(j+1) + "X/" + i + "_" + str(j+1) + "X)" + k)
                            break

print("ERRADAS - TESTE (DONE!)")
##################################################################################################################################################################