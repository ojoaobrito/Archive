# coding: utf-8
import numpy as math # importar a biblioteca de matemática, sendo que passa a ter o nome "math"

def maiorAmenorB(a,b):

	if a[1][0]>=a[1][1]: # se o primeiro elemento da 2ª linha de A for maior
		if b[0][0]<=b[1][0]: # se o primeiro elemento da 1ª coluna de A for menor
			return a[1][0]*b[0][0]

		else:
			return a[1][0]*b[1][0]

	else: # se o segundo elemento da 2ª linha de A for maior
		if b[0][0]<=b[1][0]: # se o primeiro elemento da 1ª coluna de A for menor
			return a[1][1]*b[0][0]

		else:
			return a[1][1]*b[1][0]

def logaritmos(a):
	
	for i in range(0,len(a),1):
		for j in range(0, len(a[0]),1):
			if a[i][j]<0:
				print str(a[i][j]) +" -> " +str(math.log((a[i][j])/(-1)))

			elif a[i][j]==0:
				print str(a[i][j]) +" -> " +"ERRO, LOGARITMO DE 0 NÃO EXISTE!"

			else:
				print str(a[i][j]) +" -> " +str(math.log(a[i][j]))

def diferenca(a,b):
	c = math.zeros((2,2))

	c[0][0] = a[0][0]-b[0][0]
	c[0][1] = a[0][1]-b[0][1]
	c[1][0] = a[1][0]-b[1][0]
	c[1][1] = a[1][1]-b[1][1]

	return c

def produtoMatricial(a,b):
	c = math.zeros((2,2))

	c[0][0] = (a[0][0]*b[0][0])+(a[0][1]*b[1][0])
	c[0][1] = (a[0][0]*b[0][1])+(a[0][1]*b[1][1])
	c[1][0] = (a[1][0]*b[0][0])+(a[1][1]*b[1][0])
	c[1][1] = (a[1][0]*b[0][1])+(a[1][1]*b[1][1])

	return c

def produtoElementoAElemento(a,b):
	c = math.zeros((2,2))

	c[0][0] = a[0][0]*b[0][0]
	c[0][1] = a[0][1]*b[0][1]
	c[1][0] = a[1][0]*b[1][0]
	c[1][1] = a[1][1]*b[1][1]

	return c

a = math.zeros((2,2)) # criar uma matriz 2x2 toda inicializada a 0 (se fosse array seria "math.zeros(x)", sendo x um inteiro)
b = math.zeros((2,2))

print "Escreva a primeira matriz quadrada 2x2: " # ler a primeira matriz

a[0][0] = int(raw_input("Linha 1 - Coluna 1: "))
a[0][1] = int(raw_input("Linha 1 - Coluna 2: "))
a[1][0] = int(raw_input("Linha 2 - Coluna 1: "))
a[1][1] = int(raw_input("Linha 2 - Coluna 2: "))

print "\nEscreva a segunda matriz quadrada 2x2: " # ler a segunda matriz

b[0][0] = int(raw_input("Linha 1 - Coluna 1: "))
b[0][1] = int(raw_input("Linha 1 - Coluna 2: "))
b[1][0] = int(raw_input("Linha 2 - Coluna 1: "))
b[1][1] = int(raw_input("Linha 2 - Coluna 2: "))

print "\nA matriz que resulta da multiplicação elemento a elemento é: "
print produtoElementoAElemento(a,b)

print "\nO produto matricial é: "
print produtoMatricial(a,b)

print "\nA diferença entre as 2 matrizes é: "
print diferenca(a,b)

print "\nOs logaritmos dos elementos da matriz A são: "
logaritmos(a)

print "O produto do maior valor da 2ª linha de A pelo menor valor da 1ª coluna de B é: "
print maiorAmenorB(a,b)