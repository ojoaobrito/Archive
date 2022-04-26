import sys, os, csv, subprocess
import shutil
import natsort 

## FICHEIRO QUE COMEÇA A SEPARAR AS SEQUÊNCIAS E JUNTA OS SUB-FICHEIROS DE SEPARAÇÃO
##################################################################################################################################################################
representantes = 25

if(os.path.exists("grupos")): shutil.rmtree("grupos")
os.makedirs("grupos")
 
if(os.path.exists("sequencias_separadas.txt")): os.remove("sequencias_separadas.txt")
if(os.path.exists("numero_sequencias.txt")): os.remove("numero_sequencias.txt")

# 2 protótipos de movimento obtidos pelo C-Means (podem vir trocados, pelo que é preciso fazer uma verificação)
f = open("c_means_results.txt", "r")
conteudo = (f.read()).split('\n')
aux = (list(map(float,conteudo[0].split(", "))))
aux2 = (list(map(float,conteudo[1].split(", "))))

if(aux[0]<aux2[0]): 
    aproxima_prototipo = aux
    afasta_prototipo = aux2
else: 
    afasta_prototipo = aux
    aproxima_prototipo = aux2
f.close()

# arredondar os valores
for i in range(0,len(afasta_prototipo),1): afasta_prototipo[i] = round(afasta_prototipo[i],5)
for i in range(0,len(aproxima_prototipo),1): aproxima_prototipo[i] = round(aproxima_prototipo[i],5)

# função que determina o tipo de uma dada sequência
def tipo(seq, nome):

    tipo = ""

    # primeira avaliação
    if((sum(seq)/len(seq))==seq[0]): return("lateral")

    sum_afasta = 0
    sum_aproxima = 0

    for i in range(0,len(seq),1):
        sum_afasta += abs(seq[i]-afasta_prototipo[i])
        sum_aproxima += abs(seq[i]-aproxima_prototipo[i])

    if(sum_afasta<sum_aproxima): tipo = "afasta"
    elif(sum_aproxima<sum_afasta): tipo = "aproxima"

    # segunda avaliação (13-14 -> frente (aproxima); 14-13 -> trás (afasta))
    sum_afasta = 0
    sum_aproxima = 0

    diretoria = os.listdir("Poses/Elements/Datasets/Surveillance/BIODI/pose_patches_constantProp")

    try:
        for i in diretoria:
            if(i[0]!="."):
                # já não há mais ficheiros que interessam         
                if(ord(i[0])>ord(nome[0])): 
                    if(sum_afasta==0 and sum_aproxima==0): raise Exception
                    break
                # ignorar estes ficheiros
                if(not(aux[0]==(nome.split("_"))[0] and aux[1]==(nome.split("_"))[1] and aux[2]==(nome.split("_"))[2] and aux[4]==(nome.split("_"))[3])): continue
                aux = (i.split(".")[0]).split("_")
                with open("Poses/Elements/Datasets/Surveillance/BIODI/pose_patches_constantProp/" + i) as ficheiro:
                    reader = list(csv.reader(ficheiro,delimiter=","))
                    # erro
                    if(float(reader[12][0])<0 or float(reader[13][0])<0): raise Exception
                    # valores válidos
                    if(float(reader[12][0])<float(reader[13][0])): return("aproxima")
                    else: return("afasta")
        
        # tudo correu bem
        if(sum_afasta>sum_aproxima): return("afasta")
        elif(sum_aproxima>sum_afasta): return("aproxima")
    except:
        return(tipo)

# função auxiliar que calcula o eixo dos "x" para fazer os gráficos
def eixo_x():

    xpts = []
    for j in range(1,representantes+1,1): xpts.append(round((float(j-1)/(representantes-1)),5))
    
    return(xpts)

# carregar os dados das áreas
f = open("areas_interpoladas.txt", "r")
areas = []
nomes = []
contador = 0
conteudo = (f.read()).split('\n')

while(True):
    # quando chegarmos ao fim do ficheiro vai ser lançada uma exceção, então aproveitamos isso para sair do ciclo
    try:
        nomes.append(((conteudo[contador]).split(" --- ")[0]))
        areas.append(list(map(float,((conteudo[contador]).split(" --- ")[1]).split(', '))))
        contador+=1
    except ValueError: break
    except IndexError: break
f.close()

afasta = []
aproxima = []
lateral = []

# classificar as sequências
for i in range(0,len(areas),1):

    tipo_aux = tipo(areas[i],nomes[i])
    print("SEPARAR - TIPO (" + str(i+1) + "/" + str(len(areas)) + ")")

    # sequências de afastamento
    if(tipo_aux=="afasta"): afasta.append(i)

    # sequências de aproximação
    elif(tipo_aux=="aproxima"): aproxima.append(i)
    
    # sequências laterais
    else: lateral.append(i)

# guardar os resultados num ficheiro, que será usado pelos subprocessos de separação
with open("sequencias_separadas.txt","w") as ficheiro:
    for i in afasta:        
        ficheiro.write(str(i) + "\n")
    ficheiro.write("---\n")
    for i in aproxima:        
        ficheiro.write(str(i) + "\n")
    ficheiro.write("---\n")
    for i in lateral:        
        ficheiro.write(str(i) + "\n")

# guardar os nomes num ficheiro, que serão usados pelos subprocessos de separação
with open("nomes_sequencias.txt","w") as ficheiro:
    for i in nomes: ficheiro.write(i + "\n")

# guardar estes dados num ficheiro próprio
f = open("numero_sequencias.txt", "w")
f.write("Afasta - " + str(len(afasta)) + " sequências\n")
f.write("Aproxima - " + str(len(aproxima)) + " sequências\n")
f.write("Lateral - " + str(len(lateral)) + " sequências\n")
f.close()

p1 = subprocess.Popen(["python3", "separar_treino.py"])
p2 = subprocess.Popen(["python3", "separar_validacao.py"])
p3 = subprocess.Popen(["python3", "separar_teste.py"])

# esperar que todos os subprocessos finalizem o seu trabalho
processos = [p1,p2,p3]
exit_codes = [p.wait() for p in processos]
##################################################################################################################################################################