import numpy as np
import matplotlib.pyplot as plt

N = 8
men_means = (9.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, men_means, width, color='b')

women_means = (77.3, 81.8, 63.6, 40.0, 71.4, 0.0, 0.0, 0.0)
rects2 = ax.bar(ind + width, women_means, width, color='r')

# add some text for labels, title and axes ticks
ax.set_ylabel('Percentagem')
ax.set_xlabel('Posição')
ax.set_title('Não partilha de posição')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('1º', '2º', '3º', '4º', '5º', '7º', '10º', '11º'))

ax.legend((rects1[0], rects2[0]), ('Face_match1', 'Face_match2'))

def autolabel(rects,num):
    contador = 0
    for rect in rects:
        height = rect.get_height()
        if(contador==1 and num==1 or contador==2 and num==1 or contador==3 and num==1 or contador==5 and num==1 or contador==6 and num==1 or contador==7 and num==1):
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                'ND',
                ha='center', va='bottom')
        elif(contador==1 and num==2):
            ax.text(rect.get_x() + rect.get_width()/2., 1.005*height,
                '%.1f%%' % height,
                ha='center', va='bottom')
        else:
            ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                    '%.1f%%' % height,
                    ha='center', va='bottom')
        contador+=1

autolabel(rects1,1)
autolabel(rects2,2)
plt.savefig("face_match_rankings2.png")
plt.show()