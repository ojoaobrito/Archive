# coding: utf-8
from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz 

data = np.loadtxt('CTG.csv', delimiter=',')
X = data[:,0:21] # conjunto de dados
Y = data[:,21] # classe atribuida aos dados

teste = data[0:126,:]
features = []

for i in range(0,21,1):
	features.append(str(unichr(i+48)))

clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("teste") 

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=features,  
                         class_names=Y,  
                         filled=True, rounded=True,  
                         special_characters=True)  

graph = graphviz.Source(dot_data)
graph.view()

lista_previsoes = []

for i in range(126,2127,1):
	lista_previsoes.append(clf.predict([Y]))