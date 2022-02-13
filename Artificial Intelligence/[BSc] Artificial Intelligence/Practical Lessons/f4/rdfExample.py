# coding: utf8
# UBI, Inteligência Artificial, 2017-18
# if you are using the folders supplied with this example and did not install the rdflib package in your system because of lack of root access, uncomment the next 4 lines
import sys
sys.path.append('isodate')
import isodate
sys.path.append('rdflib')
import rdflib

print "\nCriar os grafos"
g = rdflib.Graph()
g2 = rdflib.Graph() # segundo grafo, exercício 2

print "\nDefinir os predicados"
knows = rdflib.URIRef('http://www.example.fake/relations#knows')
has_class = rdflib.URIRef('http://www.example.fake/relations#has_class')

print "\nDefinir os sujeitos e objetos"
proenca = rdflib.URIRef('https://www.di.ubi.pt/~hugomcp')
alexandre = rdflib.URIRef('http://www.di.ubi.pt/~lfbaa')
silva = rdflib.URIRef('http://www.di.ubi.pt/~agomes')
sousa = rdflib.URIRef('http://www.di.ubi.pt/~desousa')
inacio = rdflib.URIRef('https://www.di.ubi.pt/~inacio')
cordeiro = rdflib.URIRef('http://www.di.ubi.pt/~jpaulo')
muranho = rdflib.URIRef('https://www.di.ubi.pt/~muranho')
student_brito = rdflib.URIRef('http://www.di.ubi.pt/~a37880')
student_pereira = rdflib.URIRef('http://www.di.ubi.pt/~a37689')
student_salvado = rdflib.URIRef('http://www.di.ubi.pt/~a37575')

sexta_fase = rdflib.URIRef('http://www.example.org/sexta_fase')

print "\nAdicionar os triplos"
g.add((student_brito,knows,alexandre))
g.add((student_brito,knows,proenca))
g.add((student_brito,knows,silva))
g.add((student_brito,knows,student_pereira))
g.add((student_brito,knows,student_salvado))
g.add((student_brito,has_class,sexta_fase))
g.add((student_brito,knows,sousa))
g.add((student_brito,knows,inacio))
g.add((student_brito,knows,muranho))
g.add((student_brito,knows,cordeiro))

g2.add((student_pereira,knows,student_brito))
g2.add((student_pereira,knows,student_salvado))
g2.add((student_pereira,knows,silva))
g2.add((student_pereira,has_class,sexta_fase))

# in the following generic SPARQL example, ? refers to a variable
# and the where clause displays the pattern that the triples should match
# you can get more specific patterns by substituting the variables in the where clause by particular values

q = "select * where {  ?p ?o }" # query, tipo SQL

x = g.query(q)

print "\nMostrar a informação toda"
print list(x)

print "\n================================================\n"
# example of serialization and file manipulation
# write graph to file, re-read it and repeat the query on the newly created graph
g.serialize("academic.rdf")
g1 = rdflib.Graph()
g1.parse("academic.rdf", format="xml")
x1 = g1.query(q)
print list(x1)
