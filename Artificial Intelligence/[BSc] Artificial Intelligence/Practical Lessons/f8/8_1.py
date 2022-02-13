#coding: utf-8
import csv # importar biblioteca de manipulação de ficheiro em formato csv

N = 0
size = [] # eixo dos áreas das casas (em m^2)
price = [] # eixo dos preços das casas (em 1000$)
tot_size = 0 # somatório dos tamanhos
tot_price = 0 # somatório dos preços
size_times_price = 0 # somatório dos preços multiplicados pelos tamanhos
tot_size_squared = 0 # somatório dos tamanhos elevados ao quadrado

with open("size_price.csv") as ficheiro:

	reader = csv.reader(ficheiro, delimiter=',')

	for i in reader:
		size.append(float(i[0]))
		tot_size = tot_size + float(i[0])
		price.append(float(i[1]))
		tot_price = tot_price + float(i[1])
		size_times_price = size_times_price + (float(i[0])*float(i[1]))
		tot_size_squared = tot_size_squared + (float(i[0])*float(i[0]))
		N+=1

# calcular os pesos
w1 = ((N*size_times_price)-(tot_size*tot_price))/((N*tot_size_squared)-(tot_size*tot_size))
w0 = ((tot_price-(w1*tot_size))/N)

print "\nQual o tamanho da casa (em m^2)?"
x = float(raw_input("> "))

print "\nO preço estimado é de %.2f€\n" % ((x*w1 + w0)*1000)