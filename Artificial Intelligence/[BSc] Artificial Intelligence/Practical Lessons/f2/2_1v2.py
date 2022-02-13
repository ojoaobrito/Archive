# coding: utf-8
import csv # importar biblioteca de manipulação de ficheiro em formato csv
import networkx as net # importar biblioteca de grafos
import matplotlib.pyplot as plt # importar biblioteca de imagens/figuras

def inverteString(string): # apenas inverte de forma inteligente uma string com espaços

	final = ""
	temp = ""

	for i in range(len(string)-1,-1,-1): # andar do final da string para o início
		temp = temp + string[i]

		if string[i]==" ":
			if final=="":
				final = final +temp[2] +temp[1] +temp[0]
				temp = ""

			else:
				final = final + temp[::-1]
				temp = ""

	final = final +" " +temp[::-1]

	return final

def larguraNaoInformada(grafo, partida, chegada):

	escolhido = ""
	distancia = 20000
	retorno = { "caminho": chegada,	"total": 0 } # dicionário com toda a informação que queremos retornar

	while True:
		for i in net.predecessor(grafo,partida,chegada): # a função "predecessor()" devolve os vizinhos de "chegada" que estão mais perto de "partida"
			temp = grafo[i][chegada]['weight'] # distância entre o vizinho e "chegada"

			if i==partida: # fim da execução
				retorno["caminho"] = retorno["caminho"] +" " +partida
				retorno["total"] = retorno["total"] + temp
				return retorno

			if temp<distancia: # se a distância for melhor que a atual melhor
				distancia = temp
				escolhido = i

		retorno["caminho"] = retorno["caminho"] +" " +escolhido # adicionamos o vizinho que escolhemos ao caminho
		retorno["total"] = retorno["total"] + distancia # aumentamos a distância total do percurso
		chegada = escolhido
		distancia = 20000

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

	retorno = larguraNaoInformada(grafo,partida,chegada)
	retorno["caminho"] = inverteString(retorno["caminho"])

	print retorno["caminho"] +"\n(com um custo aproximado de " +str(retorno["total"]) +"km)\n"

# net.draw(grafo,with_labels=True,font_size=8)
# plt.savefig("grafo.png") # save as png
# plt.show() # display
