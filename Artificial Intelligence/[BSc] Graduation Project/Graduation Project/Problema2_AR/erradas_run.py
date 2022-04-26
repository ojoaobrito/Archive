import sys, os
import subprocess

## FICHEIRO QUE JUNTA TODOS OS FICHEIROS DE GERAÇÃO DE INSTÂNCIAS ERRADAS
##################################################################################################################################################################
p1 = subprocess.Popen(["python3", "erradas_treino.py"])
p2 = subprocess.Popen(["python3", "erradas_validacao.py"])
p3 = subprocess.Popen(["python3", "erradas_teste.py"])

# esperar que todos os subprocessos finalizem o seu trabalho
processos = [p1,p2,p3]
exit_codes = [p.wait() for p in processos]
##################################################################################################################################################################
