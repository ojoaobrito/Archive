# coding: utf-8
import csv # importar biblioteca de manipulação de ficheiro em formato csv
import networkx as net # importar biblioteca de grafos
import matplotlib.pyplot as plt

def imprime(node): # devolve os vizinhos de cada nó

	string = ""

	for i in net.all_neighbors(grafo,node): # "all_neighbors()" devolve todos os vizinhos de um dado nó, o "i" vai iterar sobre eles
		string = string +i +" "

	return string

grafo = net.Graph() # criar o grafo

with open('cidades.txt') as ficheiro: # a sintaxe "with" garante que o ficheiro é sempre fechado no fim do bloco de código, mesmo que ocorra uma exceção

    reader = csv.reader(ficheiro, delimiter=',') # "reader" é o objeto que se encarrega da leitura do ficheiro .csv

    for i in reader:
    	grafo.add_edge(i[0],i[1])

print "\nOs vizinhos de cada cidade são os seguintes:\n"

for i in grafo.nodes(): # "nodes()" devolve todos os nós do grafo, o "i" vai iterar sobre eles
	print i +": " +imprime(i)

print ""

net.draw(grafo,with_labels=True,font_size=8)
plt.savefig("grafo.png") # save as png
plt.show() # display
