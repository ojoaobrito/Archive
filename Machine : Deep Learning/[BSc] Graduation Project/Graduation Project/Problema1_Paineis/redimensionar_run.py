import subprocess, sys, os
import shutil
import natsort

## FICHEIRO QUE JUNTA OS SUB-FICHEIROS DE REDIMENSIONAMENTO DAS PATCHES
#####################################################################################
# duplicar a diretoria dos grupos, para poupar trabalho
print("REDIMENSIONAR - DUPLICAR")
if(os.path.exists("grupos_redimensionados")): shutil.rmtree("grupos_redimensionados")
shutil.copytree("grupos_interpolados","grupos_redimensionados")
print("REDIMENSIONAR - DUPLICAR (DONE!)")

p1 = subprocess.Popen(["python3", "redimensionar_treino.py"])
p2 = subprocess.Popen(["python3", "redimensionar_validacao.py"])
p3 = subprocess.Popen(["python3", "redimensionar_teste.py"])

# esperar que todos os subprocessos finalizem o seu trabalho
processos = [p1,p2,p3]
exit_codes = [p.wait() for p in processos]
#####################################################################################