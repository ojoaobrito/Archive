import os, sys
import natsort 
import shutil

## FICHEIRO QUE INTERPOLA CADA SEQUÊNCIA PARA QUE TENHA UM TAMANHO FIXO
#######################################################################################################

tamanho_seq = 10
aux = 1.0
finais = [1]

# duplicar a diretoria dos grupos, para poupar trabalho
print("INTERPOLAR - DUPLICAR")
if(os.path.exists("grupos_interpolados")): shutil.rmtree("grupos_interpolados")
shutil.copytree("grupos","grupos_interpolados")
print("INTERPOLAR - DUPLICAR (DONE!)")

# TREINO (AFASTA)
diretoria = os.listdir("grupos_interpolados/treino/afasta")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("TREINO - AFASTA")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - AFASTA (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/treino/afasta/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/treino/afasta/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/treino/afasta/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("AFASTA - DONE!")

# TREINO (APROXIMA)
diretoria = os.listdir("grupos_interpolados/treino/aproxima")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("TREINO - APROXIMA")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - APROXIMA (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/treino/aproxima/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/treino/aproxima/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/treino/aproxima/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("APROXIMA - DONE!")

# TREINO (LATERAL)
diretoria = os.listdir("grupos_interpolados/treino/lateral")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("TREINO - LATERAL")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - LATERAL (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/treino/lateral/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/treino/lateral/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/treino/lateral/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("LATERAL - DONE!")

# VALIDACAO (AFASTA)
diretoria = os.listdir("grupos_interpolados/validacao/afasta")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("VALIDACAO - AFASTA")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - AFASTA (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/validacao/afasta/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/validacao/afasta/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/validacao/afasta/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("AFASTA - DONE!")

# VALIDACAO (APROXIMA)
diretoria = os.listdir("grupos_interpolados/validacao/aproxima")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("VALIDACAO - APROXIMA")
aux2 =1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - APROXIMA (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/validacao/aproxima/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/validacao/aproxima/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/validacao/aproxima/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("APROXIMA - DONE!")

# VALIDACAO (LATERAL)
diretoria = os.listdir("grupos_interpolados/validacao/lateral")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("VALIDACAO - LATERAL")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - LATERAL (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/validacao/lateral/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/validacao/lateral/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/validacao/lateral/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("LATERAL - DONE!")

# TESTE (AFASTA)
diretoria = os.listdir("grupos_interpolados/teste/afasta")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("TESTE - AFASTA")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - AFASTA (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/teste/afasta/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/teste/afasta/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/teste/afasta/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("AFASTA - DONE!")

# TESTE (APROXIMA)
diretoria = os.listdir("grupos_interpolados/teste/aproxima")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("TESTE - APROXIMA")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - APROXIMA (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/teste/aproxima/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/teste/aproxima/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/teste/aproxima/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("APROXIMA - DONE!")

# TESTE (LATERAL)
diretoria = os.listdir("grupos_interpolados/teste/lateral")
diretoria = natsort.natsorted(diretoria,reverse=False)

contador = 0
for i in diretoria:
    if((i[0]!=".")): contador += 1

print("TESTE - LATERAL")
aux2 = 1
for i in diretoria:
    if(i[0]!="."):
        print("INTERPOLAR - LATERAL (" + str(aux2) + "/" + str(contador) + ")")
        aux2 += 1
        _, _, files = next(os.walk("grupos_interpolados/teste/lateral/" + i))
        tamanho = len(files)

        if(tamanho<tamanho_seq): 
            continue

        elif(tamanho==tamanho_seq): 
            continue

        else:
            for j in range(0,tamanho_seq-1,1):
                finais.append(int(round(aux+((tamanho-1)/float(tamanho_seq-1)),5)))
                aux = round(aux+((tamanho-1)/float(tamanho_seq-1)),5)
            
            diretoria_aux = os.listdir("grupos_interpolados/teste/lateral/" + i)
            diretoria_aux = natsort.natsorted(diretoria_aux,reverse=False)

            for j in range(0,len(diretoria_aux),1):
                if((j+1) in finais): continue
                else: os.remove("grupos_interpolados/teste/lateral/" + i + "/" + diretoria_aux[j])
        
            finais = [1]
            aux = 1.0

print("LATERAL - DONE!")
print("INTERPOLAR - DONE!")
#######################################################################################################