import subprocess, sys
import time, datetime
import shutil
import os

## FICHEIRO QUE JUNTA TODOS OS FICHEIROS DE PRÉ-PROCESSAMENTO
##################################################################################################################################################################
# criar pastas para guardar cada sequência individual, agrupadas de acordo com o tipo de movimento
print("SEPARAR")
subprocess.run(["python3", "separar.py"])

# gerar uma sequencia errada - 1 a 2 imagens trocadas/adicionadas - para todas as sequencias, obtidas através dos scripts anteriores
print("ERRADAS")
subprocess.run(["python3", "erradas_run.py"])

# gera um ficheiro .csv com o resultado de todos os scripts anteriores
print("GERAR CSV")
subprocess.run(["python3", "gerar_csv.py"])

tempo = 0
contador = 0
num_runs = 1

while(contador<num_runs):
    while(tempo<1800):
        
        # libertar a memória usada por instâncias anteriores do programa de classificação
        cmd = "ps a > limpar_memoria.txt"
        output,error = subprocess.Popen(cmd, shell=True, executable="/bin/bash", stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

        with open("limpar_memoria.txt") as ficheiro:
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
        # realizar o processo de aprendizagem
        print("APRENDER")
        subprocess.run(["python3", "scr_classification_3_allmodels.py"])
        tempo = time.time()-t0
        if(tempo>1800):
            tempo = time.time()-t0
            print("\nA execução demorou: " + str(datetime.timedelta(seconds=tempo)))
            contador += 1
            tempo = 0
            break
        contador += 1
        tempo = 1800
##################################################################################################################################################################