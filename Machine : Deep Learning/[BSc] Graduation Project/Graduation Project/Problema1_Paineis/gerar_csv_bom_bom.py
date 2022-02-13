import os, sys
import csv
import natsort 
from shutil import copytree, rmtree
from random import shuffle, randint

lista_aux = []
lista_final = []
tamanho_seq = 10
sequencias_separadas = 50 # 50 sequências certas e 50 sequências erradas
contador = 0
aux = 10
nome_sequencia = 1
shuffle_on = False

if(os.path.exists("sequencias")): 
    rmtree("sequencias")
    os.makedirs("sequencias")

with open("data.csv", "w") as ficheiro:

    writer = csv.writer(ficheiro)
    ordem = []
    
    # TREINO (AFASTA)
    print("CSV - TREINO - AFASTA")
    path = "grupos_redimensionados/treino/afasta"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("0")

        lista_final.append(lista_aux)
        lista_aux = []
    
    contador = 0
    # TREINO (APROXIMA)
    print("CSV - TREINO - APROXIMA")
    path = "grupos_redimensionados/treino/aproxima"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("0")

        lista_final.append(lista_aux)
        lista_aux = []
    
    contador = 0
    # TREINO (LATERAL)
    print("CSV - TREINO - LATERAL")
    path = "grupos_redimensionados/treino/lateral"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("0")

        lista_final.append(lista_aux)
        lista_aux = []

    # VALIDACAO (AFASTA)
    print("CSV - VALIDACAO - AFASTA")
    path = "grupos_redimensionados/validacao/afasta"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("1")

        lista_final.append(lista_aux)
        lista_aux = []
    
    # VALIDACAO (APROXIMA)
    print("CSV - VALIDACAO - APROXIMA")
    path = "grupos_redimensionados/validacao/aproxima"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("1")

        lista_final.append(lista_aux)
        lista_aux = []
    
    # VALIDACAO (LATERAL)
    print("CSV - VALIDACAO - LATERAL")
    path = "grupos_redimensionados/validacao/lateral"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("1")

        lista_final.append(lista_aux)
        lista_aux = []
    '''
    # TESTE (AFASTA)
    print("CSV - TESTE - AFASTA")
    path = "grupos_redimensionados/teste/afasta"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("2")

        lista_final.append(lista_aux)
        lista_aux = []
    
    # TESTE (APROXIMA)
    print("CSV - TESTE - APROXIMA")
    path = "grupos_redimensionados/teste/aproxima"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("2")

        lista_final.append(lista_aux)
        lista_aux = []
    
    # TESTE (LATERAL)
    print("CSV - TESTE - LATERAL")
    path = "grupos_redimensionados/teste/lateral"
    diretoria = os.listdir(path)
    diretoria = natsort.natsorted(diretoria,reverse=False)
    for i in diretoria:

        # casos que não interessam
        if(i[0]=="."): continue
        _, _, files = next(os.walk(path + "/" + i))
        tamanho = len(files)
        if("X" in i and (tamanho-1)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue
        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        if(shuffle_on):
            if("X" not in i):
                if(randint(0,1)==0): 
                    shuffle(lista_aux)
                ordem = lista_aux[:]

            if("X" in i):
                lista_aux = ordem[:]
                for j in range(0,len(lista_aux),1):
                    lista_aux[j] = "/".join(lista_aux[j].split("/")[0:3]) + "/" + lista_aux[j].split("/")[3] + "X/" + lista_aux[j].split("/")[4].split(")")[0] + "X)" + lista_aux[j].split("/")[4].split(")")[1] 

        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("2")

        lista_final.append(lista_aux)
        lista_aux = []

    # SEPARAR ALGUMAS SEQUÊNCIAS PARA UM CONJUNTO DE TESTE FUTURO
    escolhidas = []

    # separar sequências certas
    for i in range(sequencias_separadas):
        escolha = randint(0,len(lista_final)-1)
        while(escolha in escolhidas or "X" in lista_final[escolha][0]): escolha = randint(0,len(lista_final)-1)
        escolhidas.append(escolha)
        copytree("/".join((lista_final[escolha][0]).split("/")[0:4]),"sequencias/" + str(nome_sequencia))
        lista_final.pop(escolha)
        nome_sequencia += 1
    nome_sequencia = 1
    escolhidas = []    
    # separar sequências erradas
    for i in range(sequencias_separadas):
        escolha = randint(0,len(lista_final)-1)
        while(escolha in escolhidas or "X" not in lista_final[escolha][0]): escolha = randint(0,len(lista_final)-1)
        escolhidas.append(escolha)
        copytree("/".join((lista_final[escolha][0]).split("/")[0:4]),"sequencias/" + str(nome_sequencia) + "X")
        lista_final.pop(escolha)
        os.remove("sequencias/" + str(nome_sequencia) + "X/1escolha.txt")
        nome_sequencia += 1
    '''
    for i in lista_final:
        writer.writerow(i)

print("CSV (DONE!)")