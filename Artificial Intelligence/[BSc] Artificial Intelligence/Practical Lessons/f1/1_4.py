# coding: utf-8

def lerLista():
	
	a=0
	lista=[]

	while True:
		a=int(raw_input())
		if a<0: break
		lista.append(a)

	return lista

def repetidos(lista,numero):

	for i in range(0,len(lista),1):
		if numero==lista[i]:
			return(True)

	return(False)
	
def numerosComuns(lista1, lista2):

	string=""
	escolhidos = []

	for i in range(0,len(lista1),1):
		for j in range(0,len(lista2),1):
			if lista1[i]==lista2[j] and repetidos(escolhidos,lista1[i])==False:
				string = string + str(lista1[i]) + " "
				escolhidos.append(lista1[i])	

	return string		

print "Escreva números à sua escolha para a 1ª lista (número negativo para terminar):"
lista1=lerLista()

print "\nEscreva números à sua escolha para a 2ª lista (número negativo para terminar):"
lista2=lerLista()

print "\nAbaixo seguem os elementos comuns:"
print numerosComuns(lista1,lista2) + "\n"
