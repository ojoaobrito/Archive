# coding: utf-8

def ler():
	aux=raw_input("Digite uma frase: ")	
	return aux	

def gravar(ficheiro, frase):
	abrir = open(ficheiro,"a")
	abrir.write(frase+"\n")
	abrir.close()

def contaVogais(frase):
	b=0
	
	for i in range(0,len(frase),1):
		if frase[i]=="a" or frase[i]=="e" or frase[i]=="i" or frase[i]=="o" or frase[i]=="u":
			b = b+1

	return b

ficheiro = raw_input("Que ficheiro vamos abrir?\n")
frase1 = ler()
frase2 = ler()

vogais1 = contaVogais(frase1)
vogais2 = contaVogais(frase2)

if vogais1>=vogais2:
	gravar(ficheiro,frase1)

else:
	gravar(ficheiro,frase2)

print "A primeira frase tem " +str(vogais1) +" vogais e a segunda tem " +str(vogais2) +"."

