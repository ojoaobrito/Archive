import sys, os, csv
from shutil import copyfile
import natsort 

percentagem_treino = 0.8
percentagem_validacao = 0.1
percentagem_teste = 0.1

contador = 1
seq_atual = 1

afasta = []
aproxima = []
lateral = []

nomes = []

diretoria = os.listdir("Patches/Elements/Datasets/Surveillance/BIODI/patches_constantProp")
diretoria = natsort.natsorted(diretoria,reverse=False)

# criar, se preciso, a diretoria "validacao"
if not os.path.exists("grupos/validacao"): os.makedirs("grupos/validacao")

# obter os resultados obtidos pelo processo pai
with open("sequencias_separadas.txt","r") as ficheiro:
    conteudo = (ficheiro.read()).split("---\n")
    
    # afastamento
    afasta_ficheiro = conteudo[0].split("\n")
    for i in afasta_ficheiro: 
        if(i!=""):
            afasta.append(int(i))
    
    # aproximação
    aproxima_ficheiro = conteudo[1].split("\n")
    for i in aproxima_ficheiro:
        if(i!=""):
            aproxima.append(int(i))

    # movimento lateral
    lateral_ficheiro = conteudo[2].split("\n")
    for i in lateral_ficheiro: 
        if(i!=""):
            lateral.append(int(i))

# obter os resultados obtidos pelo processo pai
with open("nomes_sequencias.txt","r") as ficheiro:
    conteudo = (ficheiro.read()).split("\n")
    for i in conteudo:
        if(i!=""): nomes.append(i) 

# VALIDACAO (AFASTA)
if not os.path.exists("grupos/validacao/afasta"): os.makedirs("grupos/validacao/afasta")
for i in range(int(percentagem_treino*len(afasta)),int((percentagem_treino+percentagem_validacao)*len(afasta)),1):
    for j in diretoria:
        # mover apenas as patches do indivíduo atual
        if(((nomes[afasta[i]].split("_")[0] + "_" + nomes[afasta[i]].split("_")[1] + "_" + nomes[afasta[i]].split("_")[2]) in j) and ((nomes[afasta[i]].split("_")[3])==j.split("_")[4])):

            # criar a diretoria, se não existir
            if not os.path.exists("grupos/validacao/afasta/" + str(contador)): os.makedirs("grupos/validacao/afasta/" + str(contador))

            # mover as patches correspondentes a cada sequência para a pasta criada para o efeito
            copyfile("Patches/Elements/Datasets/Surveillance/BIODI/patches_constantProp/"+ j, "grupos/validacao/afasta/" + str(contador) + "/" + "afasta-" + str(contador) + ")" + j)
    contador += 1
    print("SEPARAR - VALIDACAO - AFASTA (" + str(seq_atual) + "/" + str(len(nomes)) + ")")
    seq_atual +=1

contador = 1
print("SEPARAR - VALIDACAO - AFASTA (DONE!)")

# VALIDACAO (APROXIMA)
if not os.path.exists("grupos/validacao/aproxima"): os.makedirs("grupos/validacao/aproxima")
for i in range(int(percentagem_treino*len(aproxima)),int((percentagem_treino+percentagem_validacao)*len(aproxima)),1):
    for j in diretoria:
        # mover apenas as patches do indivíduo atual
        if(((nomes[aproxima[i]].split("_")[0] + "_" + nomes[aproxima[i]].split("_")[1] + "_" + nomes[aproxima[i]].split("_")[2]) in j) and ((nomes[aproxima[i]].split("_")[3])==j.split("_")[4])):

            # criar a diretoria, se não existir
            if not os.path.exists("grupos/validacao/aproxima/" + str(contador)): os.makedirs("grupos/validacao/aproxima/" + str(contador))

            # mover as patches correspondentes a cada sequência para a pasta criada para o efeito
            copyfile("Patches/Elements/Datasets/Surveillance/BIODI/patches_constantProp/" + j, "grupos/validacao/aproxima/" + str(contador) + "/" + "aproxima-" + str(contador) + ")" + j)
    contador += 1
    print("SEPARAR - VALIDACAO - APROXIMA (" + str(seq_atual) + "/" + str(len(nomes)) + ")")
    seq_atual +=1

contador = 1
print("SEPARAR - VALIDACAO - APROXIMA (DONE!)")

# VALIDACAO (LATERAL)
if not os.path.exists("grupos/validacao/lateral"): os.makedirs("grupos/validacao/lateral")
for i in range(int(percentagem_treino*len(lateral)),int((percentagem_treino+percentagem_validacao)*len(lateral)),1):
    for j in diretoria:
        # mover apenas as patches do indivíduo atual
        if(((nomes[lateral[i]].split("_")[0] + "_" + nomes[lateral[i]].split("_")[1] + "_" + nomes[lateral[i]].split("_")[2]) in j) and ((nomes[lateral[i]].split("_")[3])==j.split("_")[4])):

            # criar a diretoria, se não existir
            if not os.path.exists("grupos/validacao/lateral/" + str(contador)): os.makedirs("grupos/validacao/lateral/" + str(contador))

            # mover as patches correspondentes a cada sequência para a pasta criada para o efeito
            copyfile("Patches/Elements/Datasets/Surveillance/BIODI/patches_constantProp/" + j, "grupos/validacao/lateral/" + str(contador) + "/" + "lateral-" + str(contador) + ")" + j)
    contador += 1
    print("SEPARAR - VALIDACAO - LATERAL (" + str(seq_atual) + "/" + str(len(nomes)) + ")")
    seq_atual +=1

contador = 1
print("SEPARAR - VALIDACAO - LATERAL (DONE!)")
print("SEPARAR - VALIDACAO (DONE!)")
