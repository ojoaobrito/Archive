import subprocess, sys
import time, datetime
import psutil, shutil
import os
from remover import remover_pastas

## FICHEIRO QUE JUNTA TODOS OS FICHEIROS DE PRÉ-PROCESSAMENTO
############################################################################################################################################################################################################
# ["erradas_run_mau_bom.py","erradas_r_run.py","erradas_run_bom_mau.py","erradas_run.py"]
# ["gerar_csv_mau_bom.py", "gerar_csv_mau_mau.py", "gerar_csv_bom_mau.py", "gerar_csv_bom_bom.py"]
erradas = ["erradas_run.py"]
csv = ["gerar_csv_bom_bom.py"]

if(len(csv)==4 and os.path.exists("run_atual.txt")): 
    os.remove("run_atual.txt")
    ficheiro = open("run_atual.txt","w")
    ficheiro.close()

while(len(csv)!=0):
    
    # guardar num .txt as áreas normalizadas ocupadas por cada indivíduo
    print("INTERPOLAR ÁREAS")
    subprocess.run(["python3", "interpolar_areas.py"])

    # usar o algoritmo C-Means para gerar 2 protótipos de movimento - afastamento e aproximação
    print("C-MEANS")
    subprocess.run(["python3", "c_means.py"])
    
    # criar pastas para guardar cada sequência individual, agrupadas de acordo com o tipo de movimento
    print("SEPARAR")
    subprocess.run(["python3", "separar_run.py"])
    
    # gerar sub_sequencias para cada sequencia
    print("SUB-SEQUENCIAS")
    subprocess.run(["python3", "sub_sequencias_run.py"])
    
    # interpolar o resultado dos scripts anteriores para sequencias com somente N patches
    print("INTERPOLAR SEQUÊNCIAS")
    subprocess.run(["python3", "interpolar_sequencias.py"])
    
    # gerar uma sequencia errada - 1 a 2 patches trocadas - para todas as sequencias, obtidas através dos scripts anteriores
    print("ERRADAS")
    if(erradas[len(erradas)-1]=="erradas_run.py" or erradas[len(erradas)-1]=="erradas_r_run.py"):
        print("REMOVER")
        remover_pastas(["treino","validacao","teste"])
        subprocess.run(["python3", erradas[len(erradas)-1]])

    elif(erradas[len(erradas)-1]=="erradas_run_bom_mau.py"):
        print("REMOVER")
        remover_pastas(["teste"])
        subprocess.run(["python3", "erradas_r_teste.py"])

    elif(erradas[len(erradas)-1]=="erradas_run_mau_bom.py"):
        print("REMOVER")
        remover_pastas(["teste"])
        subprocess.run(["python3", "erradas_teste.py"])
    
    # redimensionar todas as patches, garantido que têm um tamanho fixo que a CNN aceita
    print("REDIMENSIONAR")
    subprocess.run(["python3", "redimensionar_run.py"])
    
    # gera um ficheiro .csv com o resultado de todos os scripts anteriores
    print("GERAR CSV")
    subprocess.run(["python3", csv[len(csv)-1]])
    
    tempo = 0
    contador = 0
    num_runs = 1
    
    while(contador<num_runs):
        while(tempo<1800):
            
            # libertar a memória usada por instâncias anteriores do programa de classificação
            cmd = "ps a > output.txt"
            output,error = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

            with open("output.txt") as ficheiro:
                conteudo = (ficheiro.read()).split("\n")
                for i in conteudo:
                    if("python3 scr_classification_3_allmodels.py" in i):
                        lista = i.split(" ")
                        for j in lista:
                            if(j!=""):
                                cmd = "kill -9 " + str(int(j))
                                output,error = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
                                break

            t0 = time.time()
            print("APRENDER")
            subprocess.run(["python3", "scr_classification_3_allmodels.py"])
            tempo = time.time()-t0
            if(tempo>1800):
                # guardar informação sobre a run atual
                '''
                ficheiro = open("run_atual.txt", "a")
                tempo = time.time()-t0
                print("\nA execução demorou: " + str(datetime.timedelta(seconds=tempo)))
                ficheiro.write((erradas[len(erradas)-1].split(".py"))[0] + " e " + (csv[len(csv)-1].split(".py"))[0] + " (" + str(contador+1) + "ª vez - " + str(datetime.timedelta(seconds=tempo)) + ")\n")
                ficheiro.close()
                '''
                contador += 1
                tempo = 0
                break

    erradas = erradas[:-1]
    csv = csv[:-1]
############################################################################################################################################################################################################