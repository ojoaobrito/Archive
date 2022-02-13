import sys
import matplotlib.pyplot as plt
import numpy as np
np.set_printoptions(threshold=sys.maxsize)

dx, dy = 0.015, 0.05
y, x = np.mgrid[slice(-50, 50 + dy, dy), 
                slice(-50, 50 + dx, dx)] 

# define the activation functions
z_linear = 1*x + 1*y + 0
z_relu = (1*x + 1*y + 0) * ((1*x + 1*y + 0) > 0)
z_mish = (1*x + 1*y + 0)*(2/(1+np.exp(-2*(np.log(1+(np.exp((1*x + 1*y + 0)))))))-1)
z_swish = 1*x + 1*y + 0

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4) 

# Linear
z_linear = z_linear[:-1, :-1] 
z_min, z_max = -np.abs(z_linear).max(), np.abs(z_linear).max() 
    
c = ax1.pcolormesh(x, y, z_linear, cmap ='Reds', vmin = z_min, 
                  vmax = z_max) 

ax1.axis("off")
ax1.invert_yaxis()
ax1.set_title("Linear") 

# ReLU
z_relu = z_relu[:-1, :-1] 
z_min, z_max = -np.abs(z_relu).max(), np.abs(z_relu).max() 
    
c = ax2.pcolormesh(x, y, z_relu, cmap ='Reds', vmin = z_min, 
                  vmax = z_max) 

ax2.axis("off")
ax2.invert_yaxis()
ax2.set_title("ReLU") 

# Mish
z_mish = z_mish[:-1, :-1] 
z_min, z_max = -np.abs(z_mish).max(), np.abs(z_mish).max() 
    
c = ax3.pcolormesh(x, y, z_mish, cmap ='Reds', vmin = z_min, 
                  vmax = z_max) 

ax3.axis("off")
ax3.invert_yaxis()
ax3.set_title("Mish") 

# Swish
z_swish = z_swish[:-1, :-1] 
z_min, z_max = -np.abs(z_swish).max(), np.abs(z_swish).max() 
    
c = ax4.pcolormesh(x, y, z_swish, cmap ='Reds', vmin = z_min, 
                  vmax = z_max) 

ax4.axis("off")
ax4.invert_yaxis()
ax4.set_title("Swish") 

plt.tight_layout()
plt.show() 