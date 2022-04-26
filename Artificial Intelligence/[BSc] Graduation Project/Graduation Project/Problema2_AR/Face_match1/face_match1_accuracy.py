import os, sys
import subprocess
import shutil

## FICHEIRO QUE AVALIA A EFICÁCIA DO FACE_MATCH V2
##################################################################################################################################################################################################################################################################################################################################################################################################
if(os.path.exists("face_match1_ranking.txt")): os.remove("face_match1_ranking.txt")
if(os.path.exists("face_match1_top.txt")): os.remove("face_match1_top.txt")

bd = os.listdir("input_BD")
for i in bd:
    print(i)
    shutil.rmtree("input")
    os.makedirs("input")
    shutil.copyfile("input_BD/"+i,"input/"+i)
    subprocess.run(["python3","face_match1.py",i])

posicoes = []
posicoes_contagem = []
posicoes_media = []
sem_partilha = []
with open("face_match1_ranking.txt","r") as ficheiro:
    conteudo = ficheiro.read().split("\n")
    for i in range(len(conteudo)-1):
        if(conteudo[i].split(" ")[0] not in posicoes): 
            posicoes.append(conteudo[i].split(" ")[0])
            posicoes_contagem.append(1)
            posicoes_media.append(int(conteudo[i].split(" ")[1]))
            if(int(conteudo[i].split(" ")[1])==0): sem_partilha.append(1)
            else: sem_partilha.append(0)
        else:
            posicoes_contagem[posicoes.index(conteudo[i].split(" ")[0])] += 1
            posicoes_media[posicoes.index(conteudo[i].split(" ")[0])] += int(conteudo[i].split(" ")[1])
            if(int(conteudo[i].split(" ")[1])==0): sem_partilha[posicoes.index(conteudo[i].split(" ")[0])] += 1

posicoes_final = []
for i in range(len(posicoes)):
    posicoes_final.append([posicoes[i],posicoes_contagem[i],posicoes_media[i],sem_partilha[i]])

posicoes_final.sort(key=lambda x: x[1],reverse=True)

print("TOTAL INDIVÍDUOS: " + str(sum(posicoes_contagem)))
for i in posicoes_final:
    print(i[0] + "º lugar: " + str(i[1]) + " vez(es) - %.1f%% - partilhou com %d pessoas, em média (%.1f%% das vezes em que ficou nesta posição não partilhou)" % ((float(i[1])/sum(posicoes_contagem))*100.0, int(i[2]/i[1]), (float(i[3])/i[1])*100.0))
##################################################################################################################################################################################################################################################################################################################################################################################################
