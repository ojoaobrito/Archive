# coding: utf-8
import csv # importar biblioteca de manipulação de ficheiro em formato csv
import networkx as net # importar biblioteca de grafos
import matplotlib.pyplot as plt # importar biblioteca de imagens/figuras

def heuristica(grafo, cidade, chegada): # função que avalia o custo (distância) entre um nó/cidade e o ponto de chegada

    atual = [cidade] # cidades a considerar
    atual2 = []
    visitados = set() # cidades já visitadas
    distancia_temp = 20000
    custo = 0 # número de cidades intermédias

    while True:
        for i in range(0,len(atual),1):
            for j in net.all_neighbors(grafo,atual[i]):

                if j==chegada: # fim da execução
                    return custo + grafo[atual[i]][chegada]['weight']

                else: # vamos considerar este vizinho na próxima iteração (se ele nunca tiver sido visitado)
                    if grafo[atual[i]][j]['weight']<distancia_temp:
                        distancia_temp = grafo[atual[i]][j]['weight']

                    conj = set()
                    conj.add(j)
                    resultado = visitados.intersection(conj)

                    if len(resultado)==0: # se a cidade nunca tiver sido visitada, acrescentamos às cidades a considerar
                        atual2.append(j)

                    conj.clear()

            visitados.add(atual[i]) # marcar a cidade atual como visitada

        atual = atual2[:]
        print atual
        del atual2[:]
        custo = custo + distancia_temp
        print custo
        distancia_temp = 20000

def AEstrela(grafo, partida, chegada):

    escolha = "" # o melhor vizinho que se pode escolher, a uma dada altura
    menor = 200000
    atual = partida
    retorno = { "caminho": partida,	"total": 0 } # dicionário com toda a informação que queremos retornar

    while True:
        for i in net.all_neighbors(grafo,atual):

            if i==chegada: # fim da execução
                retorno["caminho"] = retorno["caminho"] +" " +chegada
                retorno["total"] = retorno["total"] + grafo[atual][i]['weight']
                return retorno

            elif atual==partida: # poupar a chamada à função heurística
                valor = grafo[partida][i]['weight'] + heuristica(grafo,i,chegada)

            elif atual!=partida: # obter o melhor vizinho
                valor = heuristica(grafo,partida,i) + heuristica(grafo,i,chegada)

            print i +"(" +str(valor) +") desde o início: " +str(heuristica(grafo,partida,i)) +" km" +" até ao fim: " +str(heuristica(grafo,i,chegada)) +" km\n"

            if valor<menor: # atualizar com o melhor vizinho
                menor = valor
                escolha = i

        retorno["caminho"] = retorno["caminho"] +" " +escolha # colocamos o melhor vizinho no caminho final
        retorno["total"] = retorno["total"] + grafo[atual][escolha]['weight']
        atual = escolha # passamos a considerar este vizinho
        print escolha
        print "------------------"
        menor = 200000

grafo = net.Graph() # criar o grafo

with open('cidades.txt') as ficheiro: # a sintaxe "with" garante que o ficheiro é sempre fechado no fim do bloco de código, mesmo que ocorra uma exceção

    reader = csv.reader(ficheiro, delimiter=',') # "reader" é o objeto que se encarrega da leitura do ficheiro .csv

    for i in reader:
        grafo.add_edge(i[0],i[1],weight=int(i[2]))

partida = raw_input("\nIntroduza uma cidade de partida: ")
chegada = raw_input("E uma cidade de chegada: ")

if partida==chegada:
    print "\nNão me tente enganar, as cidades são iguais!\n"

else:
    print "\nO melhor caminho seria:\n"

    retorno = AEstrela(grafo,partida,chegada)
    print retorno["caminho"] +"\n(com um custo aproximado de " +str(retorno["total"]) +"km)\n"

# net.draw(grafo,with_labels=True,font_size=8)
# plt.savefig("grafo.png") # save as png
# plt.show() # display
