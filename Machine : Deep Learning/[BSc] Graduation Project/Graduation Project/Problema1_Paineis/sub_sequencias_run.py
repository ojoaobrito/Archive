import subprocess, sys

## FICHEIRO QUE JUNTA OS SUB-FICHEIROS DE GERAÇÃO DE SUB-SEQUÊNCIAS
###################################################################
p1 = subprocess.Popen(["python3", "sub_sequencias_treino.py"])
p2 = subprocess.Popen(["python3", "sub_sequencias_validacao.py"])
p3 = subprocess.Popen(["python3", "sub_sequencias_teste.py"])

# esperar que todos os subprocessos finalizem o seu trabalho
processos = [p1,p2,p3]
exit_codes = [p.wait() for p in processos]
###################################################################