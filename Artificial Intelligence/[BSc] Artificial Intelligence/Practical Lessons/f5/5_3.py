# coding: utf-8
import random
import time
import matplotlib.pyplot as plt

def cria_mundo(prob):
	mundo = [['N','N','N','N'],
			 ['N','N','N','N'],
			 ['N','N','N','N'],
			 ['N','N','N','N']]

	# casa [1,3]
	aux = random.randint(1,100)
	if aux<=prob:
		mundo[1][0] = 'P'
		mundo[0][0] = 'B'
		mundo[1][1] = 'B'
		mundo[2][0] = 'B'

	# casa [2,2]
	aux = random.randint(1,100)
	if aux<=prob:
		mundo[1][1] = 'B'
		mundo[2][1] = 'P'
		mundo[2][0] = 'B'
		mundo[2][2] = 'B'
		mundo[3][1] = 'B'

	# casa [3,1]
	aux = random.randint(1,100)
	if aux<=prob:
		mundo[3][2] = 'P'
		mundo[3][1] = 'B'
		mundo[1][1] = 'B'
		mundo[3][3] = 'B'

	return mundo

# casos favoráveis a cada casa
poco_1_3 = 0
poco_2_2 = 0
contador = 0
prob = 1
probabilidades = []
tempo = []

while(True):
	T0 = time.time()
	while(True):
		mundo = cria_mundo(prob+1)
		if mundo[2][0]=='B' and mundo[3][1]=='B': # mundo válido
			contador += 1
			if mundo[1][0]=='P':
				poco_1_3 += 1
			
			if mundo[2][1]=='P':
				poco_2_2 += 1

			if contador==10000:
				prob += 1
				probabilidades.append((prob*1.0)/100)
				contador = 0
				tempo.append(time.time()-T0)
				break

	if prob==101:
		break

plt.plot(probabilidades,tempo)
plt.title("Tempo em funcao das probabilidades")
plt.ylabel("Tempo que demorou a correr a experiencia (s)")
plt.xlabel("Probabilidades")
plt.xlim(0,1.0)
plt.show()
