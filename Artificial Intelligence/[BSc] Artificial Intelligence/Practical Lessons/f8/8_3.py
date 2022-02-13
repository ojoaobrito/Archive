# coding: utf-8
from sklearn.naive_bayes import GaussianNB
import csv

classificador = GaussianNB()
values = []
classes = [] # etiquetas das classes (bolas ou cruzes)

# ficheiro com os dados de aprendizagem
with open("espiral_train.csv") as ficheiro:

	reader = csv.reader(ficheiro, delimiter=',')

	for i in reader:
		values.append([float(i[0]),float(i[1])])
		classes.append(float(i[2]))

classificador.fit(values, classes)

num_testes = 0
acertos = 0

# ficheiro com os testes reais
with open("espiral_test.csv") as ficheiro:

	reader = csv.reader(ficheiro, delimiter=',')

	for i in reader:
		num_testes+=1
		if(int(i[2])==classificador.predict([[float(i[0]),float(i[1])]])):
			acertos+=1

print "\nO erro de teste é de %0.2f%%\n" % (float((1.0-(float(acertos)/num_testes))*10000)/100)