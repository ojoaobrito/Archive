# coding: utf-8

def apresenta(c3): # simplesmente para apresentar os elementos do conjunto de uma forma mais elegante

	string = ""

	if comp==1:
		return ("\"" +c3.pop() +"\"")

	elif comp==2:
		return ("\"" +c3.pop() +"\"" +" e \"" +c3.pop() +"\"")

	for i in range(0,len(c3)-2,1):
		string = string +"\"" +c3.pop() +"\", "

	string = string +"\"" +c3.pop() +"\" " +"e " +"\"" +c3.pop() +"\""

	return string

c1 = set() # conjunto 1 criado com o construtor set()
c2 = set() # conjunto 2 criado com o construtor set()

print "" # só para deixar uma linha em branco
frase1 = raw_input("Introduza a 1ª frase: ")

for i in range(0,len(frase1),1):
	if frase1[i]!=" ": # ignorar os espaços
		c1.add(frase1[i])

frase2 = raw_input("Introduza a 2ª frase: ")

for i in range(0,len(frase2),1):
	if frase2[i]!=" ": # ignorar os espaços
		c2.add(frase2[i])

c3 = c1.intersection(c2)
comp = len(c3)

if comp==0:
	print "\nNão existem letras comuns às 2 frases."

else:
	print "\nAs letras comuns a ambas as palavras são: " +apresenta(c3) +"."

c3.clear() # limpar o conjunto
c3 = c1.difference(c2)
comp = len(c3)

if comp==0:
	print "Todas as letras da 1ª frase estão na 2ª."

else:
	print "As letras que só aparecem na 1ª frase são: " +apresenta(c3) +"."

c3.clear() # limpar o conjunto
c3 = c2.difference(c1)
comp = len(c3)

if comp==0:
	print "Todas as letras da 2ª frase estão na 1ª.\n"

else:
	print "As letras que só aparecem na 2ª frase são: " +apresenta(c3) +".\n"

c3.clear() # limpar o conjunto