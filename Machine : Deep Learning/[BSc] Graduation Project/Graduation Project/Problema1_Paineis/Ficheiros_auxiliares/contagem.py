from shutil import copyfile
from shutil import rmtree
import os
import natsort 
import sys

total = 0
contador_erradas = 0
contador_erradas_validas = 0
contador_certas_validas = 0
tamanho_seq = 10

path = "grupos_redimensionados/treino/afasta"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/treino/aproxima"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/treino/lateral"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/teste/afasta"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue
    
    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/teste/aproxima"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") not in diretoria): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/teste/lateral"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/validacao/afasta"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue
    
    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/validacao/aproxima"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

path = "grupos_redimensionados/validacao/lateral"
diretoria = os.listdir(path)
diretoria = natsort.natsorted(diretoria,reverse=False)

for i in diretoria:
    if("X" in i and i[0]!="."): contador_erradas += 1
    total += 1

    _, _, files = next(os.walk(path + "/" + i))
    tamanho = len(files)

    # casos que não interessam
    if("X" in i and (tamanho-1)<tamanho_seq): continue
    if("X" not in i and tamanho<tamanho_seq): continue

    if("X" not in i and (i + "X") in diretoria): contador_certas_validas += 1
    if("X" in i): contador_erradas_validas += 1

with open("/home/socialab/Desktop/resultados/contagem_final.txt","w") as ficheiro:
    ficheiro.write("Total de sequências: " + str(total) + "\n")
    ficheiro.write("Total de sequências válidas (tamanho adequado e correspondente válida): " + str(contador_certas_validas+contador_erradas_validas) + "\n")
    ficheiro.write("---\n")
    ficheiro.write("Sequências certas: " + str(total-contador_erradas) + "\n")
    ficheiro.write("Sequências erradas: " + str(contador_erradas) + "\n")
    ficheiro.write("---\n")
    ficheiro.write("Sequências certas válidas (tamanho adequado e correspondente válida): " + str(contador_certas_validas) + "\n")
    ficheiro.write("Sequências erradas válidas (tamanho adequado e correspondente válida): " + str(contador_erradas_validas) + "\n")
