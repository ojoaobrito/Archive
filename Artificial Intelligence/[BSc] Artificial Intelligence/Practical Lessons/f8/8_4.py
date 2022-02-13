# coding: utf-8
import csv
import numpy as math
# from sklearn.neighbors import KNeighborsClassifier

def nearest_neighbours(points, p, k): # função que devolve os "k" pontos mais próximos de "p"

	neighbours = []
	aux = []
	current_distance = 0
	maximum = [[],0] # guarda o vizinho com maior distância, dos que estão escolhidos num dado momento (é este que vai ser substituído)
	max_pos = 0

	for i in range(0,len(points),1):
		aux = points[i]
		current_distance = math.sqrt([((p[0]-aux[0])*(p[0]-aux[0])) + ((p[1]-aux[1])*(p[1]-aux[1]))]) 
		
		if(len(neighbours)<k): # ainda não temos a lista de vizinhos preenchida
			neighbours.append(aux)
			if(current_distance>maximum[1]):
				maximum[0] = aux
				maximum[1] = current_distance
				max_pos = (len(neighbours)-1)

		elif(current_distance<maximum[1]): # a partir daqui temos de substituir os vizinhos mais distantes por outros mais próximos
			neighbours[max_pos] = aux
			maximum = [[],0]
			max_pos = 0

			# reencontrar o vizinho provisório com a maior distância
			for i in range(0,len(neighbours),1):
				current_distance = math.sqrt([((p[0]-neighbours[i][0])*(p[0]-neighbours[i][0])) + ((p[1]-neighbours[i][1])*(p[1]-neighbours[i][1]))])
				if(current_distance>maximum[1]):
					maximum[0] = neighbours[i]
					maximum[1] = current_distance
					max_pos = i
			
	return(neighbours)

points = [] 
k = 1 # parâmetro "k"
neighbors = [] # "k" vizinhos mais próximos
classes = [0, 0] # 2 classes ("1" e "0")

# classificador = KNeighborsClassifier(n_neighbors=1)
# x = []
# y = []

# ficheiro com os dados de aprendizagem
with open("espiral_train.csv") as ficheiro:

	reader = csv.reader(ficheiro, delimiter=',')

	for i in reader:
		points.append([float(i[0]),float(i[1]),int(i[2])])
		# x.append([float(i[0]),float(i[1])])
		# y.append([int(i[2])])

num_tests = 0
correct_predictions = 0

# acertos_classificador = 0
# classificador.fit(x,y)

# ficheiro com os testes reais
with open("espiral_test.csv") as ficheiro:

	reader = csv.reader(ficheiro, delimiter=',')

	for i in reader:
		neighbors = nearest_neighbours(points,[float(i[0]),float(i[1]),int(i[2])],k)

		for j in range(0,len(neighbors),1):
			if(neighbors[j][2]==0):
				classes[0]+=1

			else:
				classes[1]+=1

		if(classes[0]>classes[1]):
			previsao = 0

		else:
			previsao = 1

		if(previsao==int(i[2])):
			correct_predictions+=1

		# if(classificador.predict([[float(i[0]),float(i[1])]])==int(i[2])):
			# acertos_classificador+=1

		num_tests+=1
		classes = [0, 0]
		points.append([float(i[0]),float(i[1]),int(i[2])])

print("\nO erro de teste é de {0}%\n".format(float((1.0-(float(correct_predictions)/num_tests))*10000)/100))

# print("\nO erro de teste do classificador é de %0.2f%%\n".format(float((1.0-(float(acertos_classificador)/num_tests))*10000)/100))
