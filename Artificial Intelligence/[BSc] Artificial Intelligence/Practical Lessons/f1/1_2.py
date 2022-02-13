# coding: utf-8

ler = int(raw_input('Digite um número menor que 100: ')) # ler do teclado

while ler>=100: # enquanto o utilizador não acertar no número...
	print "Erro!"
	ler = int(input('Digite um número menor que 100: '))

print "O número escolhido tem " +str(ler/10) +" dezenas e " +str(ler%10) +" unidades."
