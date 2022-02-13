import sys, os
from shutil import copyfile
import natsort

escolher_atual = 1.0
tamanho_minimo = 0.2
contador_sub = 1
tamanho_seq = 10
possibilidades = []

# contar o número de sequências disponíveis
f = open("numero_sequencias.txt", "r")
conteudo = (f.read()).split(" ")
numero_sub = 7

num_afasta = int(conteudo[2])
num_aproxima = int(conteudo[5])
num_lateral = int(conteudo[8])

# função que simplesmente retorna a distância entre o elemento final e o inicial
def funcao_aux(elemento):
    return(elemento[1]-elemento[0])

# TESTE (AFASTA)
diretoria = os.listdir("grupos/teste/afasta")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if(("_" not in i) and (i[0]!=".")): contador += 1

# gerar as sub-sequências, para cada sequência original
for i in diretoria:
    # já existem sub-sequências para esta sequência geradas
    if((i + "_1") in diretoria): continue
    
    # gerar as sub-sequências
    if(("_" not in i)):
        print("SUB-SEQUENCIAS - TESTE - AFASTA (" + str(i) + "/" + str(contador) + ")")

        _, _, files = next(os.walk("grupos/teste/afasta/" + i))
        tamanho = len(files)

        if(tamanho<=tamanho_seq): continue

        # todos os inícios disponíveis, para esta sequência original
        inicios_disponiveis = [i for i in range(0,tamanho-(int(round(tamanho*tamanho_minimo,0)))-1,1)]

        while(len(inicios_disponiveis)!=0):
            # inicio = random.choice(inicios_disponiveis)
            inicio = inicios_disponiveis[len(inicios_disponiveis)-1]

            # para cada inicio vamos gerar todos os finais possíveis, e consequentemente, todas as sub-sequências
            fins_disponiveis = [i for i in range(inicio+int(round(tamanho_minimo*tamanho,0)),tamanho,1)]
            
            # percorrer cada final disponível
            while(len(fins_disponiveis)!=0):
                # fim = random.choice(fins_disponiveis)
                fim = fins_disponiveis[len(fins_disponiveis)-1]
            
                # guardar esta nova sub-sequência
                possibilidades.append([inicio, fim])

                fins_disponiveis.remove(fim)
            
            inicios_disponiveis.remove(inicio)

        final = []
        # de todas as possibilidades de sub-sequências vamos escolher as que têm mais patches
        possibilidades.sort(reverse=True,key=funcao_aux)

        for k in range(0,numero_sub,1):
            if(k==len(possibilidades)):
                break
            final.append(possibilidades[k])

        for j in final:

            originais = os.listdir("grupos/teste/afasta/" + i)
            originais = natsort.natsorted(originais,reverse=False)

            if not os.path.exists("grupos/teste/afasta/" + i + "_" + str(contador_sub)): 
                os.makedirs("grupos/teste/afasta/" + i + "_" + str(contador_sub))

            # formar esta nova sub-sequência
            for k in range(j[0],j[1]+1,1):
                copyfile("grupos/teste/afasta/" + i + "/" + originais[k], "grupos/teste/afasta/" + i + "_" + str(contador_sub) + "/" + "afasta-" + i + "_" + str(contador_sub) + ")" + (originais[k].split(")")[1])) 

            contador_sub += 1
    
    contador_sub = 1
    possibilidades = []

print("SUB-SEQUENCIAS - TESTE - AFASTA (DONE!)")

# TESTE (APROXIMA)
diretoria = os.listdir("grupos/teste/aproxima")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if(("_" not in i) and (i[0]!=".")): contador += 1

# gerar as sub-sequências, para cada sequência original
for i in diretoria:
    # já existem sub-sequências para esta sequência geradas
    if((i + "_1") in diretoria): continue
    
    # gerar as sub-sequências
    if(("_" not in i)):
        print("SUB-SEQUENCIAS - TESTE - APROXIMA (" + str(i) + "/" + str(contador) + ")")

        _, _, files = next(os.walk("grupos/teste/aproxima/" + i))
        tamanho = len(files)

        if(tamanho<=tamanho_seq): continue

        # todos os inícios disponíveis, para esta sequência original
        inicios_disponiveis = [i for i in range(0,tamanho-(int(round(tamanho*tamanho_minimo,0)))-1,1)]

        while(len(inicios_disponiveis)!=0):
            # inicio = random.choice(inicios_disponiveis)
            inicio = inicios_disponiveis[len(inicios_disponiveis)-1]

            # para cada inicio vamos gerar todos os finais possíveis, e consequentemente, todas as sub-sequências
            fins_disponiveis = [i for i in range(inicio+int(round(tamanho_minimo*tamanho,0)),tamanho,1)]
            
            # percorrer cada final disponível
            while(len(fins_disponiveis)!=0):
                # fim = random.choice(fins_disponiveis)
                fim = fins_disponiveis[len(fins_disponiveis)-1]
            
                # guardar esta nova sub-sequência
                possibilidades.append([inicio, fim])

                fins_disponiveis.remove(fim)
            
            inicios_disponiveis.remove(inicio)

        final = []
        # de todas as possibilidades de sub-sequências vamos escolher as que têm mais patches
        possibilidades.sort(reverse=True, key=funcao_aux)

        for k in range(0, numero_sub, 1):
            if (k == len(possibilidades)):
                break
            final.append(possibilidades[k])

        for j in final:

            originais = os.listdir("grupos/teste/aproxima/" + i)
            originais = natsort.natsorted(originais,reverse=False)

            if not os.path.exists("grupos/teste/aproxima/" + i + "_" + str(contador_sub)): 
                os.makedirs("grupos/teste/aproxima/" + i + "_" + str(contador_sub))

            # formar esta nova sub-sequência
            for k in range(j[0],j[1]+1,1):
                copyfile("grupos/teste/aproxima/" + i + "/" + originais[k], "grupos/teste/aproxima/" + i + "_" + str(contador_sub) + "/" + "aproxima-" + i + "_" + str(contador_sub) + ")" + (originais[k].split(")")[1])) 

            contador_sub +=1
    
    contador_sub = 1
    possibilidades = []

print("SUB-SEQUENCIAS - TESTE - APROXIMA (DONE!)")

# TESTE (LATERAL)
diretoria = os.listdir("grupos/teste/lateral")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if(("_" not in i) and (i[0]!=".")): contador += 1

# gerar as sub-sequências, para cada sequência original
for i in diretoria:
    # já existem sub-sequências para esta sequência geradas
    if((i + "_1") in diretoria): continue
    
    # gerar as sub-sequências
    if(("_" not in i)):
        print("SUB-SEQUENCIAS - TESTE - LATERAL (" + str(i) + "/" + str(contador) + ")")

        _, _, files = next(os.walk("grupos/teste/lateral/" + i))
        tamanho = len(files)

        if(tamanho<=tamanho_seq): continue
            
        # todos os inícios disponíveis, para esta sequência original
        inicios_disponiveis = [i for i in range(0,tamanho-(int(round(tamanho*tamanho_minimo,0)))-1,1)]

        while(len(inicios_disponiveis)!=0):
            # inicio = random.choice(inicios_disponiveis)
            inicio = inicios_disponiveis[len(inicios_disponiveis)-1]

            # para cada inicio vamos gerar todos os finais possíveis, e consequentemente, todas as sub-sequências
            fins_disponiveis = [i for i in range(inicio+int(round(tamanho_minimo*tamanho,0)),tamanho,1)]
            
            # percorrer cada final disponível
            while(len(fins_disponiveis)!=0):
                # fim = random.choice(fins_disponiveis)
                fim = fins_disponiveis[len(fins_disponiveis)-1]
            
                # guardar esta nova sub-sequência
                possibilidades.append([inicio, fim])

                fins_disponiveis.remove(fim)
            
            inicios_disponiveis.remove(inicio)

        final = []
        # de todas as possibilidades de sub-sequências vamos escolher as que têm mais patches
        possibilidades.sort(reverse=True, key=funcao_aux)

        for k in range(0, numero_sub, 1):
            if (k == len(possibilidades)):
                break
            final.append(possibilidades[k])

        for j in final:

            originais = os.listdir("grupos/teste/lateral/" + i)
            originais = natsort.natsorted(originais,reverse=False)

            if not os.path.exists("grupos/teste/lateral/" + i + "_" + str(contador_sub)): 
                os.makedirs("grupos/teste/lateral/" + i + "_" + str(contador_sub))

            # formar esta nova sub-sequência
            for k in range(j[0],j[1]+1,1):
                copyfile("grupos/teste/lateral/" + i + "/" + originais[k], "grupos/teste/lateral/" + i + "_" + str(contador_sub) + "/" + "lateral-" + i + "_" + str(contador_sub) + ")" + (originais[k].split(")")[1])) 

            contador_sub +=1
    
    contador_sub = 1
    possibilidades = []

print("SUB-SEQUENCIAS - TESTE - LATERAL (DONE!)")
print("SUB-SEQUENCIAS - TESTE (DONE!)")