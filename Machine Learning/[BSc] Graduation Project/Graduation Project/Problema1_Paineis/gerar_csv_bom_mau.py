import os, sys
import csv
import natsort 

lista_aux = []
tamanho_seq = 10

with open("data.csv", "w") as ficheiro:

    writer = csv.writer(ficheiro)

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
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("0")

        writer.writerow(lista_aux)
        lista_aux = []

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
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("0")

        writer.writerow(lista_aux)
        lista_aux = []
    
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
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("0")

        writer.writerow(lista_aux)
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
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("1")

        writer.writerow(lista_aux)
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
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("1")

        writer.writerow(lista_aux)
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
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("1")

        writer.writerow(lista_aux)
        lista_aux = []

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
        if("X" in i and (tamanho)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("2")

        writer.writerow(lista_aux)
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
        if("X" in i and (tamanho)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue

        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("2")

        writer.writerow(lista_aux)
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
        if("X" in i and (tamanho)<tamanho_seq): continue
        if("X" not in i and tamanho<tamanho_seq): continue

        # não existe instância negativa para esta positiva
        if("X" not in i and (i + "X") not in diretoria): continue
        # casos bons
        sequencia = os.listdir(path + "/" + i)
        sequencia = natsort.natsorted(sequencia,reverse=False)
        for j in sequencia: 
            if(j!="1escolha.txt"): lista_aux.append(path + "/" + i + "/" + j)
        
        # guardar a classe
        if("X" in i): lista_aux.append("0")
        else: lista_aux.append("1")
        
        # guardar se é de treino, validacao ou teste
        lista_aux.append("2")

        writer.writerow(lista_aux)
        lista_aux = []

print("CSV (DONE!)")