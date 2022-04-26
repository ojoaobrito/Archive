import sys

## FICHEIRO QUE DEVOLVE AS CARATE´RISTICA DE UMA IMAGEM (SOFT-BIOMETRICS)
###############################################################################################################################################################
etiquetas = [

    ["gender", ["male","female","unknown"]],
    ["age", ["0-11","12-19","18-24","25-34","35-44","45-54","55-64",">65","unknown"]],
    ["height", ["child","short","medium","tall","unknown"]],
    ["body volume", ["thin","medium","fat","unknown"]],
    ["ethnicity", ["white","black","asian","indian","unknown"]],
    ["hair color", ["black","brown","blonde","red","gray","can't see","unknown"]],
    ["hairstyle", ["bald","short","medium","long","unknown","horse tail"]],
    ["beard", ["yes","no","unknown"]],
    ["moustache", ["yes","no","unknown"]],
    ["glasses", ["glasses","sunglasses","no","unknown"]],
    ["head clothing", ["hat","scarf","necklace","nothing","unknown"]],
    ["upper body clothing", ["shirt","blouse","sweater","coat","bikini","naked","dress","uniform","shirt","suit","hoodie","unknown","cardigan"]],
    ["lower body clothing", ["jeans","leggins","pants","shorts","skirt","bikini","dress","uniform","suit","unknown"]],
    ["feet clothing", ["sport","classic","high heels","boots","sandals","nothing","unknown"]],
    ["accessories", ["bag","backpack","rolling bag","umbrella","sports bag","market bag","nothing","unknown"]],
    ["action", ["walking","running","standing","seated","biking","exercising","petting","phone","leave bag","fall","agression","dating","offending","trading"]]
]

def distancia_carateristicas(imagem1, imagem2): # função que calcula a distância entre as 2 imagens, em termos de extras/caraterísticas

    distancia = 0.0
    aux = set()
    aux2 = set()

    for i in range(1,len(etiquetas),1):
        for j in imagem1[i]: aux.add(j)
        for j in imagem2[i]: aux2.add(j)
        if(etiquetas[i][0]=="head clothing" or etiquetas[i][0]=="upper body clothing" or etiquetas[i][0]=="lower body clothing" 
            or etiquetas[i][0]=="feet clothing"):
            distancia += float((len(aux.difference(aux2)) + len(aux2.difference(aux)))*4.5)

        elif(etiquetas[i][0]=="ethnicity" or etiquetas[i][0]=="accessories" or etiquetas[i][0]=="hairstyle" or etiquetas[i][0]=="hair color"):
            distancia += float((len(aux.difference(aux2)) + len(aux2.difference(aux)))*3)

        else:
            distancia += float(len(aux.difference(aux2)) + len(aux2.difference(aux)))
            
        aux = set()
        aux2 = set()

    return(distancia)

def get_carateristicas(imagem): # função que devolve os extras/caraterísticas da imagem passada por parâmetro

    global etiquetas
    carateristicas_imagem = []
    aux = ""
    nome = imagem.split("_") 

    # gender
    carateristicas_imagem.append([])
    aux = (bin(int(nome[5])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[0][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[0][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[0][1][i])

    # age
    carateristicas_imagem.append([])
    aux = (bin(int(nome[6])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[1][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[1][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[1][1][i])

    # height
    carateristicas_imagem.append([])
    aux = (bin(int(nome[7])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[2][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[2][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[2][1][i])

    # body volume
    carateristicas_imagem.append([])
    aux = (bin(int(nome[8])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[3][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[3][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[3][1][i])

    # ethnicity
    carateristicas_imagem.append([])
    aux = (bin(int(nome[9])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[4][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[4][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[4][1][i])
    
    # hair color
    carateristicas_imagem.append([])
    aux = (bin(int(nome[10])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[5][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[5][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[5][1][i])

    # hairstyle
    carateristicas_imagem.append([])
    aux = (bin(int(nome[11])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[6][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[6][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[6][1][i])

    # beard
    carateristicas_imagem.append([])
    aux = (bin(int(nome[12])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[7][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[7][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[7][1][i])

    # moustache
    carateristicas_imagem.append([])
    aux = (bin(int(nome[13])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[8][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[8][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[8][1][i])

    # glasses
    carateristicas_imagem.append([])
    aux = (bin(int(nome[14])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[9][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[9][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[9][1][i])

    # head clothing
    carateristicas_imagem.append([])
    aux = (bin(int(nome[15])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[10][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[10][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[10][1][i])

    # upper body clothing
    carateristicas_imagem.append([])
    aux = (bin(int(nome[16])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[11][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[11][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[11][1][i])

    # lower body cloting
    carateristicas_imagem.append([])
    aux = (bin(int(nome[17])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[12][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[12][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[12][1][i])

    # feet clothing
    carateristicas_imagem.append([])
    aux = (bin(int(nome[18])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[13][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[13][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[13][1][i])

    # accessories
    carateristicas_imagem.append([])
    aux = (bin(int(nome[19])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[14][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[14][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[14][1][i])

    # action
    carateristicas_imagem.append([])
    aux = (bin(int(nome[20])).split('b')[1])[::-1]
    while(len(aux)<len(etiquetas[15][1])): aux = aux + "0"

    for i in range(0,len(etiquetas[15][1]),1):
        if(aux[i]=="1"): carateristicas_imagem[len(carateristicas_imagem)-1].append(etiquetas[15][1][i])

    return(carateristicas_imagem)
###############################################################################################################################################################