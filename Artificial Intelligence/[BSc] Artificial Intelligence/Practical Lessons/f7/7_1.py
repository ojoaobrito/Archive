# coding: utf-8
from sklearn.datasets import load_iris
from sklearn import tree
import numpy as np
import graphviz 

iris = load_iris()

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 

# aux = iris.feature_names
# print aux

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  

graph = graphviz.Source(dot_data)
graph.view()
print "A resposta da árvore é %d" % clf.predict([[2.1, 2.7, 3.9, 1.2]])