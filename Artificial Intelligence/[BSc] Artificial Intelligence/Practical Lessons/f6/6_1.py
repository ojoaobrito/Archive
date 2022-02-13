# encoding: utf8
# ----------------------------------
import sys
sys.path.append('bayesian')
from bayesian.bbn import build_bbn

def f_prize_door(prize_door): # porta com o prémio
	return 0.25000000

def f_guest_door(guest_door): # porta que o convidado escolheu
	return 0.25000000

def f_monty_door(prize_door, guest_door, monty_door):
	
	if prize_door==guest_door: # o convidado escolheu bem

		if prize_door==monty_door: # o Monty nunca revela o prémio
			return 0

		else: # o Monty escolhe uma das portas com cabras
			return 0.33333333

	elif prize_door==monty_door: # o Monty nunca vai escolher a porta com prémio
		return 0

	elif guest_door==monty_door: # isto nunca acontece
		return 0

	else:
		return 1

if __name__ == '__main__':
	g = build_bbn(
	f_prize_door,
	f_guest_door,
	f_monty_door,
	domains=dict(
	prize_door=['A', 'B', 'C', 'D'],
	guest_door=['A', 'B', 'C', 'D'],
	monty_door=['A', 'B', 'C', 'D']))
