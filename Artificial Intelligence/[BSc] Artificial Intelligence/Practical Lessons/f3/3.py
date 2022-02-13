# coding: utf8
import copy
import random
import time

# ------------------------------------------------------------------
def mostra_tabuleiro(T):

	string = ""

	for i in range(0,9,3): # linhas

		for j in range(0,3,1): #colunas

			if T[j+i]==1:
				string = string + "X  " # MAX jogou

			elif T[j+i]==0:
				string = string + ".  " # ninguém jogou

			else:
				string = string + "O  " # MIN jogou

		print string
		string = ""

# ------------------------------------------------------------------
def mostra_tabuleiro_linha(T):

	string = ""

	for i in range(0,12,4): # linhas

		for j in range(0,4,1): #colunas

			if T[j+i]==1:
				string = string + "X  " # MAX jogou

			elif T[j+i]==0:
				string = string + ".  " # ninguém jogou

			else:
				string = string + "O  " # MIN jogou

		print string
		string = ""

# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes(T):

	a = [] # lista de ações

	for i in range(0,len(T),1):
		if T[i]==0:
			a.append(i) # ação possível

	return a

# ------------------------------------------------------------------
# devolve a lista de ações que se podem executar partido de um estado
def acoes_linha(T):

	a = [] # lista de ações

	for i in range(0,len(T),1): # percorrer as linhas restantes

		if i>=8 and i<=11: # última linha
			if T[i]==0:
				a.append(i) # ação possível

		elif T[i+4]!=0 and T[i]==0:
			a.append(i) # ação possível

	return a

# ------------------------------------------------------------------
# devolve o estado que resulta de partir de um estado e executar uma ação
def resultado(T, a, jogador):

	aux = copy.copy(T)

	if jogador=="MAX":
		aux[a] = 1

	else:
		aux[a] = -1

	return aux

# ------------------------------------------------------------------
# existem 8 possíveis alinhamentos vencedores, para cada jogador
def utilidade(T):

	# linhas
	for i in range(0,9,3):
		if (T[i]==1 and T[i+1]==1 and T[i+2]==1) or (T[i]==-1 and T[i+1]==-1 and T[i+2]==-1):
			if T[i]==1:
				return 1

			else:
				return -1

	# colunas
	for i in range(0,3,1):
		if (T[i]==1 and T[i+3]==1 and T[i+6]==1) or (T[i]==-1 and T[i+3]==-1 and T[i+6]==-1):
			if T[i]==1:
				return 1

			else:
				return -1

	# diagonais
	if (T[0]==1 and T[4]==1 and T[8]==1) or (T[0]==-1 and T[4]==-1 and T[8]==-1):
		if T[0]==1:
			return 1

		else:
			return -1

	if (T[2]==1 and T[4]==1 and T[6]==1) or (T[2]==-1 and T[4]==-1 and T[6]==-1):
		if T[2]==1:
			return 1

		else:
			return -1

	# houve empate (ou então ainda não houve, isso é avaliado na função "estado_terminal()")
	return 0

# ------------------------------------------------------------------
# existem 14 possíveis alinhamentos vencedores, para cada jogador
def utilidade_linha(T):

	# linhas
	for i in range(0,9,4):
		if (T[i]==1 and T[i+1]==1 and T[i+2]==1) or (T[i]==-1 and T[i+1]==-1 and T[i+2]==-1):
			if T[i]==1:
				return 1

			return -1

		elif (T[i+1]==1 and T[i+2]==1 and T[i+3]==1) or (T[i+1]==-1 and T[i+2]==-1 and T[i+3]==-1):
			if T[i+1]==1:
				return 1

			return -1

	# colunas
	for i in range(0,4,1):
		if (T[i]==1 and T[i+4]==1 and T[i+8]==1) or (T[i]==-1 and T[i+4]==-1 and T[i+8]==-1):
			if T[i]==1:
				return 1

			return -1

	# diagonais
	if (T[0]==1 and T[5]==1 and T[10]==1) or (T[0]==-1 and T[5]==-1 and T[10]==-1):
		if T[0]==1:
			return 1

		return -1

	elif (T[1]==1 and T[6]==1 and T[11]==1) or (T[1]==-1 and T[6]==-1 and T[11]==-1):
		if T[1]==1:
			return 1

		return -1

	elif (T[2]==1 and T[5]==1 and T[8]==1) or (T[2]==-1 and T[5]==-1 and T[8]==-1):
		if T[2]==1:
			return 1

		return -1

	elif (T[3]==1 and T[6]==1 and T[9]==1) or (T[3]==-1 and T[6]==-1 and T[9]==-1):
		if T[3]==1:
			return 1

		return -1

	# houve empate (ou então ainda não houve, isso é avaliado na função "estado_terminal()")
	return 0

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
def estado_terminal(T):

	aux = utilidade(T)

	if aux==1 or aux==-1: # de certeza que alguém ganhou
		return True

	for i in range(0,len(T),1): # a função "utilidade()" devolveu 0 (empate), mas vamos ver se foi mesmo isso que aconteceu
		if T[i]==0:
			return False

	return True # de facto é um empate

# ------------------------------------------------------------------
# devolve True se T é terminal, senão devolve False
def estado_terminal_linha(T):

	aux = utilidade_linha(T)

	if aux==1 or aux==-1: # de certeza que alguém ganhou
		return True

	for i in range(0,len(T),1): # a função "utilidade()" devolveu 0 (empate), mas vamos ver se foi mesmo isso que aconteceu
		if T[i]==0:
			return False

	return True # de facto é um empate

# ------------------------------------------------------------------
# algoritmo da wikipedia
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta(T, alfa, beta, jogador):

	if estado_terminal(T): # critério de paragem
		return utilidade(T),-1,-1

	if jogador: # joga o MAX
		v = -10
		melhor_acao = -1
		acoes_aux = acoes(T)

		for a in range(0,len(acoes_aux),1): # percorrer as ações que o MAX pode realizar

			v1,ac,es = alfabeta(resultado(T,acoes_aux[a],'MAX'),alfa,beta,False)
			if v1 > v: # guardo a ação que corresponde ao melhor
				v = v1
				melhor_acao = acoes_aux[a]

			alfa = max(alfa,v)
			if beta <= alfa: # se o MIN puder obter um melhor valor do que já tem, não vamos por esta ramificação
				break
		return v,melhor_acao,resultado(T,melhor_acao,'MAX')

	else: # joga o MIN
		v = 10
		melhor_acao = 1
		acoes_aux = acoes(T)

		for a in range(0,len(acoes_aux),1): # percorrer as ações que o MIN pode realizar

			v1,ac,es = alfabeta(resultado(T,acoes_aux[a],'MIN'),alfa,beta,True)
			if v1 < v: # guardo a ação que corresponde ao melhor
				v = v1
				melhor_acao = acoes_aux[a]

			beta = min(beta,v)
			if beta <= alfa: # se, por esta ramificação, o MAX obtiver um resultado pior, então ele já vai descartar esta ação (independentemente do que ainda não foi avalaido)
				break
		return v,melhor_acao,resultado(T,melhor_acao,'MIN')

# ------------------------------------------------------------------
# algoritmo da wikipedia
# https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
# ignoramos a profundidade e devolvemos o valor, a ação e o estado resultante
def alfabeta_linha(T, alfa, beta, jogador):

	if estado_terminal_linha(T): # critério de paragem
		return utilidade_linha(T),-1,-1

	if jogador: # joga o MAX
		v = -10
		melhor_acao = -1
		acoes_aux = acoes_linha(T)

		for a in range(0,len(acoes_aux),1): # percorrer as ações que o MAX pode realizar

			v1,ac,es = alfabeta_linha(resultado(T,acoes_aux[a],'MAX'),alfa,beta,False)
			if v1 > v: # guardo a ação que corresponde ao melhor
				v = v1
				melhor_acao = acoes_aux[a]

			alfa = max(alfa,v)
			if beta <= alfa: # se o MIN puder obter um melhor valor do que já tem, não vamos por esta ramificação
				break
		return v,melhor_acao,resultado(T,melhor_acao,'MAX')

	else: # joga o MIN
		v = 10
		melhor_acao = 1
		acoes_aux = acoes_linha(T)

		for a in range(0,len(acoes_aux),1): # percorrer as ações que o MIN pode realizar

			v1,ac,es = alfabeta_linha(resultado(T,acoes_aux[a],'MIN'),alfa,beta,True)
			if v1 < v: # guardo a ação que corresponde ao melhor
				v = v1
				melhor_acao = acoes_aux[a]

			beta = min(beta,v)
			if beta <= alfa: # se, por esta ramificação, o MAX obtiver um resultado pior, então ele já vai descartar esta ação (independentemente do que ainda não foi avaliado)
				break
		return v,melhor_acao,resultado(T,melhor_acao,'MIN')

# ------------------------------------------------------------------
def joga_max(T):
	v,a,e = alfabeta(T,-10,10,True)
	print "\nMAX joga para " +str(a)
	return e

# ------------------------------------------------------------------
def joga_max_linha(T):
	v,a,e = alfabeta_linha(T,-10,10,True)
	print "\nMAX joga para " +str(a)
	return e

# ------------------------------------------------------------------
def joga_min(T):
	v,a,e = alfabeta(T,-10,10,False)
	print "\nMIN joga para " +str(a)
	return e

# ------------------------------------------------------------------
def joga_min_linha(T):
	v,a,e = alfabeta_linha(T,-10,10,False)
	print "\nMIN joga para " +str(a)
	return e

# ------------------------------------------------------------------
def joga_min_linha2(T):
	v,a,e = alfabeta_linha(T,-10,10,False)
	return e

# ------------------------------------------------------------------
def jogo(p1,p2):

	# cria tabuleiro vazio
	T = [0,0,0,0,0,0,0,0,0]
	# podemos partir de um estado mais "avançado"
	#T = [1,-1,0,0,-1,0,1,0,0]

	print "INÍCIO"
	mostra_tabuleiro(T)
	while acoes(T) != [] and not estado_terminal(T):
		T=p1(T)
		mostra_tabuleiro(T)
		if acoes(T) != [] and not estado_terminal(T):
			T=p2(T)
			mostra_tabuleiro(T)

	# fim
	if utilidade(T) == 1:
		print "\n>>> Venceu o jogador 1 <<<"
	elif utilidade(T) == -1:
		print "\n>>> Venceu o jogador 2 <<<"
	else:
		print "\n>>> Empate <<<"

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand(T):

	x = random.randint(0,8)

	while T[x]!=0:
		x = random.randint(0,8)

	T[x] = -1

	print "\nRand joga para " +str(x)

	return T

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand_linha(T):

	x = random.randint(0,11)
	lista = []
	k = 0

	while k==0:
		lista = acoes_linha(T)
		for i in range(0,len(lista),1): # avaliar se a ação escolhida é válida
			if x==lista[i]:
				k = 1
				break

			elif i==(len(lista)-1):
				x = random.randint(0,11)

	T[x] = -1

	print "\nRand joga para " +str(x)

	return T

# ------------------------------------------------------------------
# jogador aleatório
def joga_rand_linha2(T):

	x = random.randint(0,11)
	lista = []
	k = 0

	while k==0:
		lista = acoes_linha(T)
		for i in range(0,len(lista),1): # avaliar se a ação escolhida é válida
			if x==lista[i]:
				k = 1
				break

			elif i==(len(lista)-1):
				x = random.randint(0,11)

	T[x] = 1

	return T

# ------------------------------------------------------------------
# jogador humano
def joga_humano(T):

	print ""
	jogada = int(raw_input("Você joga para "))

	while (jogada>8 or jogada<0) or T[jogada]!=0:
		print ""
		jogada = int(raw_input("Você joga para "))

	T[jogada] = -1

	return T

# ------------------------------------------------------------------
# jogador humano
def joga_humano_linha(T):

	print ""
	k = 0
	jogada = int(raw_input("Você joga para "))

	while k==0:
		lista = acoes_linha(T)
		for i in range(0,len(lista),1): # avaliar se a ação escolhida é válida
			if jogada==lista[i]:
				k = 1
				break

			elif i==(len(lista)-1):
				print ""
				jogada = int(raw_input("Você joga para "))

	T[jogada] = -1

	return T

# ------------------------------------------------------------------
def linha(p1,p2):

	# cria tabuleiro vazio
	T = [0,0,0,0,0,0,0,0,0,0,0,0]
	# podemos partir de um estado mais "avançado"
	#T = [1,-1,0,0,-1,0,1,0,0,1,1,-1]

	print "INÍCIO"
	mostra_tabuleiro_linha(T)
	while acoes_linha(T) != [] and not estado_terminal_linha(T):
		T=p1(T)
		mostra_tabuleiro_linha(T)
		if acoes_linha(T) != [] and not estado_terminal_linha(T):
			T=p2(T)
			mostra_tabuleiro_linha(T)

	# fim
	if utilidade_linha(T) == 1:
		print "\n>>> Venceu o jogador 1 (cruzes) <<<"

	elif utilidade_linha(T) == -1:
		print "\n>>> Venceu o jogador 2 (bolas) <<<"

	else:
		print "\n>>> Empate <<<"

# ------------------------------------------------------------------
def linha2(p1,p2): # serve para o Random vs MIN

	# cria tabuleiro vazio
	T = [0,0,0,0,0,0,0,0,0,0,0,0]
	# podemos partir de um estado mais "avançado"
	#T = [1,-1,0,0,-1,0,1,0,0,1,1,-1]

	while acoes_linha(T) != [] and not estado_terminal_linha(T):
		T=p1(T)
		if acoes_linha(T) != [] and not estado_terminal_linha(T):
			T=p2(T)

	# fim
	if utilidade_linha(T) == 1:
		return 1

	elif utilidade_linha(T) == -1:
		return -1

	else:
		return 0

# ------------------------------------------------------------------
# main

while True:

	print "\n----- JOGOS DIVERTIDOS -----\n"
	print "1: 3 em linha"
	print "2: Jogo do galo"
	print "\n0: EXIT\n"
	escolha = int(raw_input("> "))

	if escolha==0:
		print ""
		break

	elif escolha==1:

		print "\n-------- 3 EM LINHA ULTIMATE --------\n"
		print "1: MAX vs MIN (jogadores alfabeta)"
		print "2: MAX vs Random"
		print "3: Random vs MIN (1000 vezes c/tempo)"
		print "4: Você contra o MAX (nível hard)"
		print "\n0: VOLTAR\n"
		escolha = int(raw_input("> "))

		if escolha==0:
			print ""

		elif escolha==1:
			print "\n--- MAX vs MIN (jogadores alfabeta) ---\n"
			linha(joga_max_linha,joga_min_linha) # deve ganhar sempre o MAX

		elif escolha==2:
			print "\n--- MAX vs Random ---\n"
			linha(joga_max_linha,joga_rand_linha) # deve ganhar quase sempre o MAX, mas o Random pode surpreender

		elif escolha==3:
			print "\n--- Random vs MIN (1000 vezes c/tempo) ---\n"
			conta_min = 0
			empate = 0
			conta_random = 0
			T0 = time.time()
			for i in range(0,1000,1):
				guarda = linha2(joga_rand_linha2,joga_min_linha2) # o MIN vai ganhar mais vezes que o Random

				if guarda==1:
					conta_random+=1

				elif guarda==-1:
					conta_min+=1

				else:
					empate+=1

			print "O MIN ganhou {0} vezes, o Random ganhou {1} vezes e houveram {2} empates." .format(conta_min,conta_random,empate)
			print "(TEMPO: {:0.2f}s)" .format(time.time()-T0)

		elif escolha==4:
			print "\n--- Você contra o MAX (nível hard) ---\n"
			linha(joga_max_linha,joga_humano_linha) # deve ganhar sempre o MAX

		else:
			print "\nOPÇÃO INVÁLIDA!\n"

	elif escolha==2:

		print "\n-------- JOGO DO GALO 2000 --------\n"
		print "1: MAX vs MIN (jogadores alfabeta)"
		print "2: MAX vs Random"
		print "3: Você contra o MAX (nível hard)"
		print "\n0: VOLTAR\n"
		escolha = int(raw_input("> "))

		if escolha==0:
			print ""

		elif escolha==1:
			print "\n--- MAX vs MIN (jogadores alfabeta) ---\n"
			jogo(joga_max,joga_min) # devem empatar sempre

		elif escolha==2:
			print "\n--- MAX vs Random ---\n"
			jogo(joga_max,joga_rand) # deve ganhar sempre o MAX

		elif escolha==3:
			print "\n--- Você contra o MAX (nível hard) ---\n"
			jogo(joga_max,joga_humano) # deve ganhar sempre o MAX

		else:
			print "\nOPÇÃO INVÁLIDA!\n"

	else:
		print "\nOPÇÃO INVÁLIDA!\n"
