import sys
import matplotlib.pyplot as plt
import numpy as np
import math

# definição das funções
x = np.linspace(-5,5,10000)
tanh = 2/(1+np.exp(-2*x))-1
softplus = np.log(1+(np.exp(x)))
mish = x*(2/(1+np.exp(-2*(np.log(1+(np.exp(x))))))-1)
relu = x * (x > 0)
swish = x*(1/(1+np.exp(-x)))

# definição das derivadas
tanh_d = 1-(tanh**2)
softplus_d = 1/(1+np.exp(-x))
mish_d = (np.exp(x)*(4*(x+1)+4*np.exp(2*x)+np.exp(3*x)+np.exp(x)*((4*x)+6)))/((2*np.exp(x)+np.exp(2*x)+2)**2)
relu_d = 1.*(x > 0)
swish_d = swish + (1/(1+np.exp(-x)))*(1-swish)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x,mish_d, 'r', label="Mish'")
plt.plot(x,swish_d, 'b', label="Swish'", alpha=0.5)
plt.plot(x,relu_d, 'g', label="ReLU'", alpha=1.0)

plt.grid()
plt.legend(loc="best")
plt.show()