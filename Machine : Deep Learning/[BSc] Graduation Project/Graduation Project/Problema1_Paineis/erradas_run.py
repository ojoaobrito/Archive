import subprocess, sys

## FICHEIRO QUE JUNTA OS SUB-FICHEIROS DE GERAÇÃO DE SEQUÊNCIAS ERRADAS (NA FORMA INFORMADA)
############################################################################################
p1 = subprocess.Popen(["python3", "erradas_treino_afasta_lateral.py"])
p2 = subprocess.Popen(["python3", "erradas_treino_aproxima.py"])
p3 = subprocess.Popen(["python3", "erradas_validacao.py"])
p4 = subprocess.Popen(["python3", "erradas_teste.py"])

# esperar que todos os subprocessos finalizem o seu trabalho
processos = [p1,p2,p3,p4]
exit_codes = [p.wait() for p in processos]
############################################################################################