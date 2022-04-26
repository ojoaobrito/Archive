import sys, os
from shutil import copyfile, rmtree
import natsort

## FICHEIRO QUE SEPARA OS INDIVÍDUOS POR PASTAS E GRUPOS (TREINO, VALIDAÇÃO E TESTE)
################################################################################################################################
percentagem_treino = 0.8
percentagem_validacao = 0.1
percentagem_teste = 0.1

if(os.path.exists("grupos")): rmtree("grupos")
os.makedirs("grupos")

if(os.path.exists("grupos_BD")): rmtree("grupos_BD")
os.makedirs("grupos_BD")

if(os.path.exists("input_BD")): rmtree("input_BD")
os.makedirs("input_BD")

# criar, se preciso, as diretorias "treino", "validacao" e "teste"
if not os.path.exists("grupos/treino"): os.makedirs("grupos/treino")
if not os.path.exists("grupos/validacao"): os.makedirs("grupos/validacao")
if not os.path.exists("grupos/teste"): os.makedirs("grupos/teste")

dataset = os.listdir("AR_DATASET")
dataset = natsort.natsorted(dataset,reverse=False)

name = ""
men = []
women = []
for i in dataset:
    if(i[0]!="."):
        name = i.split("-")[0] + i.split("-")[1]
        if("m" in name):
            if(name not in men): men.append(name)
        else:
            if(name not in women): women.append(name)

# separar os indivíduos
contador = 1
for i in range(0,int(percentagem_treino*len(men)),1):
    print("SEPARAR - TREINO (" + str(contador+1) + "/" + str(len(men)) + ")")
    if(not os.path.exists("grupos/treino/" + str(contador))): os.makedirs("grupos/treino/" + str(contador))
    contador += 1
    for j in dataset:
        if(j[0]!="."):
            if(int(j.split("-")[1])>int(men[i].split("m")[1])): break
            aux = j.split("-")[0] + j.split("-")[1]
            if(men[i]==aux):
                copyfile("AR_DATASET/" + j,"grupos/treino/" + str(contador-1) + "/" + j)
    # verificar se temos imagens que chegue
    _,_,files = next(os.walk("grupos/treino/" + str(contador-1)))
    if(len(files)!=13 and len(files)!=26): # indivíduo inválido
        rmtree("grupos/treino/" + str(contador-1))
        contador -= 1
    # guardar a foto 3 para o sistema de identificação de indivíduos
    diretoria = os.listdir("grupos/treino/" + str(contador-1))
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:
        if(i[0]!="."):
            if(((i.split(".")[0]).split("-")[2])=="1"):
                copyfile("grupos/treino/" + str(contador-1) + "/" + i,"grupos_BD/" + i.split(".")[0] + ".jpg")
            if(((i.split(".")[0]).split("-")[2])=="3"):
                copyfile("grupos/treino/" + str(contador-1) + "/" + i,"input_BD/" + i.split(".")[0] + ".jpg")
                os.remove("grupos/treino/" + str(contador-1) + "/" + i)

# dividir os indivíduos
for i in range(0,int(percentagem_treino*len(women)),1):
    print("SEPARAR - TREINO (" + str(contador+1) + "/" + str(len(women)) + ")")
    if(not os.path.exists("grupos/treino/" + str(contador))): os.makedirs("grupos/treino/" + str(contador))
    contador += 1
    for j in dataset:
        if(j[0]!="."):
            if("m" in j): continue
            if(int(j.split("-")[1])>int(women[i].split("w")[1])): break
            aux = j.split("-")[0] + j.split("-")[1]
            if(women[i]==aux):
                copyfile("AR_DATASET/" + j,"grupos/treino/" + str(contador-1) + "/" + j)
    # verificar se temos imagens que chegue
    _,_,files = next(os.walk("grupos/treino/" + str(contador-1)))
    if(len(files)!=13 and len(files)!=26): # indivíduo inválido
        rmtree("grupos/treino/" + str(contador-1))
        contador -= 1
    # guardar a foto 3 para o sistema de identificação de indivíduos
    diretoria = os.listdir("grupos/treino/" + str(contador-1))
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:
        if(i[0]!="."):
            if(((i.split(".")[0]).split("-")[2])=="1"):
                copyfile("grupos/treino/" + str(contador-1) + "/" + i,"grupos_BD/" + i.split(".")[0] + ".jpg")
            if(((i.split(".")[0]).split("-")[2])=="3"):
                copyfile("grupos/treino/" + str(contador-1) + "/" + i,"input_BD/" + i.split(".")[0] + ".jpg")
                os.remove("grupos/treino/" + str(contador-1) + "/" + i)

contador = 1
for i in range(int(percentagem_treino*len(men)),int(percentagem_treino*len(men)) + int(percentagem_validacao*len(men)),1):
    print("SEPARAR - VALIDACAO (" + str(contador+1) + "/" + str(len(men)) + ")")
    if(not os.path.exists("grupos/validacao/" + str(contador))): os.makedirs("grupos/validacao/" + str(contador))
    contador += 1
    for j in dataset:
        if(j[0]!="."):
            if(int(j.split("-")[1])>int(men[i].split("m")[1])): break
            aux = j.split("-")[0] + j.split("-")[1]
            if(men[i]==aux):
                copyfile("AR_DATASET/" + j,"grupos/validacao/" + str(contador-1) + "/" + j)
    # verificar se temos imagens que chegue
    _,_,files = next(os.walk("grupos/validacao/" + str(contador-1)))
    if(len(files)!=13 and len(files)!=26): # indivíduo inválido
        rmtree("grupos/validacao/" + str(contador-1))
        contador -= 1
    # guardar a foto 3 para o sistema de identificação de indivíduos
    diretoria = os.listdir("grupos/validacao/" + str(contador-1))
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:
        if(i[0]!="."):
            if(((i.split(".")[0]).split("-")[2])=="1"):
                copyfile("grupos/validacao/" + str(contador-1) + "/" + i,"grupos_BD/" + i.split(".")[0] + ".jpg")
            if(((i.split(".")[0]).split("-")[2])=="3"):
                copyfile("grupos/validacao/" + str(contador-1) + "/" + i,"input_BD/" + i.split(".")[0] + ".jpg")
                os.remove("grupos/validacao/" + str(contador-1) + "/" + i)

for i in range(int(percentagem_treino*len(women)),int(percentagem_treino*len(women)) + int(percentagem_validacao*len(women)),1):
    print("SEPARAR - VALIDACAO (" + str(contador+1) + "/" + str(len(women)) + ")")
    if(not os.path.exists("grupos/validacao/" + str(contador))): os.makedirs("grupos/validacao/" + str(contador))
    contador += 1
    for j in dataset:
        if(j[0]!="."):
            if("m" in j): continue
            if(int(j.split("-")[1])>int(women[i].split("w")[1])): break
            aux = j.split("-")[0] + j.split("-")[1]
            if(women[i]==aux):
                copyfile("AR_DATASET/" + j,"grupos/validacao/" + str(contador-1) + "/" + j)
    # verificar se temos imagens que chegue
    _,_,files = next(os.walk("grupos/validacao/" + str(contador-1)))
    if(len(files)!=13 and len(files)!=26): # indivíduo inválido
        rmtree("grupos/validacao/" + str(contador-1))
        contador -= 1
    # guardar a foto 3 para o sistema de identificação de indivíduos
    diretoria = os.listdir("grupos/validacao/" + str(contador-1))
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:
        if(i[0]!="."):
            if(((i.split(".")[0]).split("-")[2])=="1"):
                copyfile("grupos/validacao/" + str(contador-1) + "/" + i,"grupos_BD/" + i.split(".")[0] + ".jpg")
            if(((i.split(".")[0]).split("-")[2])=="3"):
                copyfile("grupos/validacao/" + str(contador-1) + "/" + i,"input_BD/" + i.split(".")[0] + ".jpg")
                os.remove("grupos/validacao/" + str(contador-1) + "/" + i)

contador = 1
for i in range(int(percentagem_treino*len(men)) + int(percentagem_validacao*len(men)),len(men),1):
    print("SEPARAR - TESTE (" + str(contador+1) + "/" + str(len(men)) + ")")
    if(not os.path.exists("grupos/teste/" + str(contador))): os.makedirs("grupos/teste/" + str(contador))
    contador += 1
    for j in dataset:
        if(j[0]!="."):
            if(int(j.split("-")[1])>int(men[i].split("m")[1])): break
            aux = j.split("-")[0] + j.split("-")[1]
            if(men[i]==aux):
                copyfile("AR_DATASET/" + j,"grupos/teste/" + str(contador-1) + "/" + j)
    # verificar se temos imagens que chegue
    _,_,files = next(os.walk("grupos/teste/" + str(contador-1)))
    if(len(files)!=13 and len(files)!=26): # indivíduo inválido
        rmtree("grupos/teste/" + str(contador-1))
        contador -= 1
    # guardar a foto 3 para o sistema de identificação de indivíduos
    diretoria = os.listdir("grupos/teste/" + str(contador-1))
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:
        if(i[0]!="."):
            if(((i.split(".")[0]).split("-")[2])=="1"):
                copyfile("grupos/teste/" + str(contador-1) + "/" + i,"grupos_BD/" + i.split(".")[0] + ".jpg")
            if(((i.split(".")[0]).split("-")[2])=="3"):
                copyfile("grupos/teste/" + str(contador-1) + "/" + i,"input_BD/" + i.split(".")[0] + ".jpg")
                os.remove("grupos/teste/" + str(contador-1) + "/" + i)

for i in range(int(percentagem_treino*len(women)) + int(percentagem_validacao*len(women)),len(women),1):
    print("SEPARAR - TESTE (" + str(contador+1) + "/" + str(len(men)) + ")")
    if(not os.path.exists("grupos/teste/" + str(contador))): os.makedirs("grupos/teste/" + str(contador))
    contador += 1
    for j in dataset:
        if(j[0]!="."):
            if("m" in j): continue
            if(int(j.split("-")[1])>int(women[i].split("w")[1])): break
            aux = j.split("-")[0] + j.split("-")[1]
            if(women[i]==aux):
                copyfile("AR_DATASET/" + j,"grupos/teste/" + str(contador-1) + "/" + j)
    # verificar se temos imagens que chegue
    _,_,files = next(os.walk("grupos/teste/" + str(contador-1)))
    if(len(files)!=13 and len(files)!=26): # indivíduo inválido
        rmtree("grupos/teste/" + str(contador-1))
        contador -= 1
    # guardar a foto 3 para o sistema de identificação de indivíduos
    diretoria = os.listdir("grupos/teste/" + str(contador-1))
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:
        if(i[0]!="."):
            if(((i.split(".")[0]).split("-")[2])=="1"):
                copyfile("grupos/teste/" + str(contador-1) + "/" + i,"grupos_BD/" + i.split(".")[0] + ".jpg")
            if(((i.split(".")[0]).split("-")[2])=="3"):
                copyfile("grupos/teste/" + str(contador-1) + "/" + i,"input_BD/" + i.split(".")[0] + ".jpg")
                os.remove("grupos/teste/" + str(contador-1) + "/" + i)

print("SEPARAR (DONE!)")
################################################################################################################################