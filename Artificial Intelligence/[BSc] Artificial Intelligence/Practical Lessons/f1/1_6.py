# coding: utf-8

notas = { # no fundo é um conjunto de tuplos
	
	"Estruturas de Dados": 12, # chave: valor
	"Teoria da Computação": 14,
	"Bases de Dados": 15
}

def inserirNota(uc, nota):
	
	notas[uc] = nota

def alterarNota(uc, nota):
	
	notas[uc] = nota

def mostrarTudo():

	for i,j in notas.items(): # "items() refere-se aos itens numa linha do dicionário, sendo o "i" a UC e o "j" a nota
		print i +" - " +str(j) +" valores"

def obterMedia():

	soma = 0

	for i in notas:
		soma = soma + notas[i]

	print "\nA média é: %0.2f valores" % (float(soma)/len(notas)) # "float()" transforma a divisão inteira numa fracionária
																  # print à la C, ao invés de ser mais no estilo do Java

sair = 0

while sair==0:

	print "\n-------- MENU DE NOTAS --------\n"
	print "1: Inserir novo par \"UC - Nota\""
	print "2: Alterar a nota de uma UC"
	print "3: Mostrar tudo"
	print "4: Obter a média das notas\n"
	print "0: SAIR\n"

	escolha = raw_input("> ")

	while True:

		if escolha=="0":
			print "" # só para deixar uma linha em branco
			sair = 1
			break
		
		if escolha=="1":

			k=0

			while k==0:

				print "\nQual a cadeira que quer acrescentar?"
				uc = raw_input("> ")

				k=1 # se este valor for alterado é porque a UC introduzida já existe no dicionário

				for i,j in notas.items():

						if i==uc:
							k=0
							print "\nNOME INVÁLIDO!"
							break

			print "\nE qual foi a nota?"
			nota = int(raw_input("> "))
			inserirNota(uc,nota)
			break

		elif escolha=="2":
			
			k=0

			while k==0:

				print "\nQual a cadeira que quer alterar?"
				uc = raw_input("> ")

				for i,j in notas.items():

					if i==uc:
						k=1
						break

				print "\nNOME INVÁLIDO!"

			print "\nE qual foi a nota?"
			nota = int(raw_input("> "))
			alterarNota(uc,nota)
			break

		elif escolha=="3":

			print "" # só para deixar uma linha em branco
			mostrarTudo()
			break

		elif escolha=="4":

			obterMedia()
			break

		else:

			print "\nQUANTAS OPÇÕES VÊ?! META LÁ UM VALOR DE JEITO SFF\n"
			escolha = raw_input("> ")