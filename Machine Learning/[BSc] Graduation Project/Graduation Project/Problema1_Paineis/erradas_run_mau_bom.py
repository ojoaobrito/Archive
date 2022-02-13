import subprocess, sys

p1 = subprocess.Popen(["python3", "erradas_r_treino.py"])
p2 = subprocess.Popen(["python3", "erradas_r_validacao.py"])
p3 = subprocess.Popen(["python3", "erradas_teste.py"])

# esperar que todos os subprocessos finalizem o seu trabalho
processos = [p1,p2,p3]
exit_codes = [p.wait() for p in processos]