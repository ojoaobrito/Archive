from shutil import copyfile
from shutil import rmtree
import os
import natsort 
import sys

def remover_pastas(pastas):

	for j in pastas:

		diretoria = os.listdir("grupos_interpolados/" + j + "/afasta")
		diretoria = natsort.natsorted(diretoria,reverse=False)

		for i in diretoria:
			if("X" in i and i[0]!="."):
				rmtree("grupos_interpolados/" + j + "/afasta/" + i)

		diretoria = os.listdir("grupos_interpolados/" + j + "/aproxima")
		diretoria = natsort.natsorted(diretoria,reverse=False)

		for i in diretoria:
			if("X" in i and i[0]!="."):
				rmtree("grupos_interpolados/" + j + "/aproxima/" + i)

		diretoria = os.listdir("grupos_interpolados/" + j + "/lateral")
		diretoria = natsort.natsorted(diretoria,reverse=False)

		for i in diretoria:
			if("X" in i and i[0]!="."):
				rmtree("grupos_interpolados/" + j + "/lateral/" + i)

# remover_pastas(["treino","validacao","teste"])