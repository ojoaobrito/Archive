# coding: utf-8
import random
import time

def cria_mundo():
	mundo = [['N','N','N','N'],
			 ['N','N','N','N'],
			 ['N','N','N','N'],
			 ['N','N','N','N']]

	# casa [1,3]
	aux = random.randint(1,5)
	if aux==1: # probabilidade de 0.2
		mundo[1][0] = 'P'
		mundo[0][0] = 'B'
		mundo[1][1] = 'B'
		mundo[2][0] = 'B'

	# casa [2,2]
	aux = random.randint(1,5)
	if aux==1: # probabilidade de 0.2
		mundo[1][1] = 'B'
		mundo[2][1] = 'P'
		mundo[2][0] = 'B'
		mundo[2][2] = 'B'
		mundo[3][1] = 'B'

	# casa [3,1]
	aux = random.randint(1,5)
	if aux==1: # probabilidade de 0.2
		mundo[3][2] = 'P'
		mundo[3][1] = 'B'
		mundo[1][1] = 'B'
		mundo[3][3] = 'B'

	return mundo

# casos favoráveis a cada casa
poco_1_3 = 0
poco_2_2 = 0
poco_3_1 = 0
contador = 0

T0 = time.time()

while(True):
	mundo = cria_mundo()
	if mundo[2][0]=='B' and mundo[3][1]=='B': # mundo válido
		contador += 1
		if mundo[1][0]=='P':
			poco_1_3 += 1
		
		if mundo[2][1]=='P':
			poco_2_2 += 1
		
		if mundo[3][2]=='P':
			poco_3_1 += 1

		if contador==10000:
			break

# a multiplicação por 1.0 serve de cast, neste caso para float
prob_1_3 = (poco_1_3 * 1.0)/10000
prob_2_2 = (poco_2_2 * 1.0)/10000
prob_3_1 = (poco_3_1 * 1.0)/10000

print "\nPROBABILIDADES (10000 CASOS - POÇOS 20%)\n"
print "[1,3]: %.3f\n[2,2]: %0.3f\n[3,1]: %0.3f\n\nTEMPO: %0.2fs\n" % (prob_1_3,prob_2_2,prob_3_1,time.time()-T0)