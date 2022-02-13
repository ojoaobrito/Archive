import sys, os
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

if(not os.path.exists("imagens")): os.makedirs("imagens")

# carregar os dados das áreas
f = open("areas_interpoladas.txt", "r")
areas = []
contador = 0
conteudo = (f.read()).split('\n')

while(True):
    # quando chegarmos ao fim do ficheiro vai ser lançada uma exceção, então aproveitamos isso para sair do ciclo
    try:
        areas.append(list(map(float,((conteudo[contador]).split(" --- ")[1]).split(', '))))
        contador+=1
    except ValueError: break
    except IndexError: break
f.close()

# preparar os dados para o C-Means
dados_aux = []

for i in range(0,len(areas),1):
    dados_aux.append([])
    for j in areas[i]:
        dados_aux[len(dados_aux)-1].append(j)

dados = np.vstack(dados_aux)

# executar o algoritmo de clustering C-Means
cntr, prototipos, _, _, _, _, _ = fuzz.cluster.cmeans(dados, 2, 2, error=0.005, maxiter=1000)

# guardar os protótipos obtidos num ficheiro
f = open('c_means_results.txt', 'w')
for i in prototipos.tolist():
    f.write(", ".join(map(str,i)))
    f.write("\n")
f.close()

# apresentar os 2 protótipos
fig2, ax = plt.subplots()
plt.plot(prototipos.tolist()[0], label="Protótipo 1")
plt.plot(prototipos.tolist()[1], label="Protótipo 2")
plt.title("C-Means")
plt.ylabel("Area (normalizada)")
plt.xlabel("Frames")
ax.legend()
plt.savefig("imagens/c-means_25.png")
# plt.show()