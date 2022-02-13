import os, sys
import csv
import natsort 
from random import shuffle,randint

## FICHEIRO QUE GERA O .CSV USADO NA APRENDIZAGEM E CLASSIFICAÇÃO FINAL
####################################################################################################################################################################################################################
lista_aux = []
shuffle_on = False
ordem = []

with open("base.csv", "w") as ficheiro2:
    with open("data.csv", "w") as ficheiro:

        writer = csv.writer(ficheiro)
        writer2 = csv.writer(ficheiro2)

        # TREINO
        print("CSV - TREINO")
        path = "grupos_errados/treino"
        diretoria = os.listdir(path)
        diretoria = natsort.natsorted(diretoria,reverse=False)
        for i in diretoria:

            # casos que não interessam
            if(i[0]=="."): continue
            _, _, files = next(os.walk(path + "/" + i))
            tamanho = len(files)

            # casos bons
            sequencia = os.listdir(path + "/" + i)
            sequencia = natsort.natsorted(sequencia,reverse=False)
            lista_aux.append(path + "/" + i + "/" + j)
            
            if(shuffle_on):
                if("X" not in i):
                    if(randint(0,1)==0): 
                        shuffle(lista_aux)
                    ordem = lista_aux[:]

                if("X" in i):
                    lista_aux = ordem[:]
                    for j in range(0,len(lista_aux),1):
                        lista_aux[j] = "/".join(lista_aux[j].split("/")[0:2]) + "/" + lista_aux[j].split("/")[2] + "X/" + lista_aux[j].split("/")[3].split(")")[0] + "X)" + lista_aux[j].split("/")[3].split(")")[1] 

            # guardar a classe
            if("X" in i): lista_aux.append("0")
            else: lista_aux.append("1")
            
            # guardar se é de treino, validacao ou teste
            lista_aux.append("0")

            writer.writerow(lista_aux)
            writer2.writerow(lista_aux)
            lista_aux = []
        
        # VALIDACAO
        ordem = []
        print("CSV - VALIDACAO")
        path = "grupos_errados/validacao"
        diretoria = os.listdir(path)
        diretoria = natsort.natsorted(diretoria,reverse=False)
        for i in diretoria:

            # casos que não interessam
            if(i[0]=="."): continue
            _, _, files = next(os.walk(path + "/" + i))
            tamanho = len(files)

            # casos bons
            sequencia = os.listdir(path + "/" + i)
            sequencia = natsort.natsorted(sequencia,reverse=False)
            lista_aux.append(path + "/" + i + "/" + j)
        
            if(shuffle_on):
                if("X" not in i):
                    if(randint(0,1)==0): 
                        shuffle(lista_aux)
                    ordem = lista_aux[:]

                if("X" in i):
                    lista_aux = ordem[:]
                    for j in range(0,len(lista_aux),1):
                        lista_aux[j] = "/".join(lista_aux[j].split("/")[0:2]) + "/" + lista_aux[j].split("/")[2] + "X/" + lista_aux[j].split("/")[3].split(")")[0] + "X)" + lista_aux[j].split("/")[3].split(")")[1] 

            # guardar a classe
            if("X" in i): lista_aux.append("0")
            else: lista_aux.append("1")
            
            # guardar se é de treino, validacao ou teste
            lista_aux.append("1")

            writer.writerow(lista_aux)
            writer2.writerow(lista_aux)
            lista_aux = []

        # TESTE
        ordem = []
        print("CSV - TESTE")
        path = "grupos_errados/teste"
        diretoria = os.listdir(path)
        diretoria = natsort.natsorted(diretoria,reverse=False)
        for i in diretoria:

            # casos que não interessam
            if(i[0]=="."): continue
            _, _, files = next(os.walk(path + "/" + i))
            tamanho = len(files)

            # casos bons
            sequencia = os.listdir(path + "/" + i)
            sequencia = natsort.natsorted(sequencia,reverse=False)
            lista_aux.append(path + "/" + i + "/" + j)
            
            if(shuffle_on):
                if("X" not in i):
                    if(randint(0,1)==0): 
                        shuffle(lista_aux)
                    ordem = lista_aux[:]

                if("X" in i):
                    lista_aux = ordem[:]
                    for j in range(0,len(lista_aux),1):
                        lista_aux[j] = "/".join(lista_aux[j].split("/")[0:2]) + "/" + lista_aux[j].split("/")[2] + "X/" + lista_aux[j].split("/")[3].split(")")[0] + "X)" + lista_aux[j].split("/")[3].split(")")[1] 

            # guardar a classe
            if("X" in i): lista_aux.append("0")
            else: lista_aux.append("1")
            
            # guardar se é de treino, validacao ou teste
            lista_aux.append("2")

            writer.writerow(lista_aux)
            lista_aux = []

print("CSV (DONE!)")
####################################################################################################################################################################################################################