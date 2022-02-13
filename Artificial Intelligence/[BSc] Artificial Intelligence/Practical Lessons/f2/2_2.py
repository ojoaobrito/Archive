# coding: utf-8
import csv # importar biblioteca de manipulação de ficheiro em formato csv
import networkx as net # importar biblioteca de grafos
import matplotlib.pyplot as plt # importar biblioteca de imagens/figuras

def heuristica(grafo, cidade, chegada): # função que avalia o custo (distância) entre um nó/cidade e o ponto de chegada

    atual = [cidade] # cidades a considerar
    atual2 = []
    visitados = set() # cidades já visitadas
    distancia_temp = 20000
    escolha = cidade
    custo = 0 # número de cidades intermédias

    while True:
        for i in range(0,len(atual),1):
            for j in net.predecessor(grafo,chegada,escolha):

                if j==chegada: # fim da execução
                    return custo + grafo[escolha][chegada]["weight"]

                else: # vamos considerar este vizinho na próxima iteração (se ele nunca tiver sido visitado)
                    if grafo[escolha][j]['weight']<distancia_temp:
                        distancia_temp = grafo[escolha][j]['weight']
                        print "escolha " +j +": " +str(grafo[escolha][j]['weight'])
                        escolha = j

            visitados.add(escolha) # marcar a cidade atual como visitada


        print escolha +": " +str(distancia_temp)
        custo = custo + distancia_temp
        distancia_temp = 20000

def AEstrela(grafo, partida, chegada):

    escolha = "" # o melhor vizinho que se pode escolher, a uma dada altura
    menor = 200000
    atual = partida
    retorno = { "caminho": partida,	"total": 0 } # dicionário com toda a informação que queremos retornar

    while True:
        for i in net.predecessor(grafo,chegada,atual):

            if i==chegada: # fim da execução
                retorno["caminho"] = retorno["caminho"] +" " +chegada
                retorno["total"] = retorno["total"] + grafo[atual][i]['weight']
                return retorno

            elif atual==partida: # poupar a chamada à função heurística
                valor = grafo[partida][i]['weight'] + heuristica(grafo,i,chegada)

            elif atual!=partida:
                valor = heuristica(grafo,partida,i) + heuristica(grafo,i,chegada) # obter o melhor vizinho

            print "\n--------\n" +i +": " +str(valor) +"\n--------\n"

            if valor<menor: # atualizar com o melhor vizinho
                menor = valor
                escolha = i

        retorno["caminho"] = retorno["caminho"] +" " +escolha # colocamos o melhor vizinho no caminho final
        retorno["total"] = retorno["total"] + grafo[atual][escolha]['weight']
        atual = escolha # passamos a considerar este vizinho
        menor = 20000

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

    # print "\n Pelo A* imbutido:\n"
    # print net.astar_path(grafo,partida,chegada)
    # print ""

net.draw(grafo,with_labels=True,font_size=8)
plt.savefig("grafo.png") # save as png
plt.show() # display
