# encoding: utf8
# ----------------------------------
import sys
sys.path.append('bayesian')
from bayesian.bbn import build_bbn

def f_chuva(chuva):
	return 0.20

def f_aspersor(aspersor, chuva):
	
	if chuva==True:
		return 0.01
	
	return 0.40

def f_relva_molhada(relva_molhada, aspersor, chuva):
	
	if chuva==True and aspersor==True:
		return 0.99

	elif chuva==True and aspersor==False:
		return 0.80

	elif chuva==False and aspersor==True:
		return 0.90

	elif chuva==False and aspersor==False:
		return 0

	elif chuva==True:
		return

	elif chuva==False:
		return

if __name__ == '__main__':
	g = build_bbn(
	f_chuva,
	f_aspersor,
	f_relva_molhada,
	domains=dict(
	chuva=[True, False],
	aspersor=[True, False],
	relva_molhada=[True, False]))
