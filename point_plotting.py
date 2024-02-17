# Code for simple point plots 

import numpy as np
import matplotlib.pyplot as plt 

#x-axis data
x = [200 , 225, 250, 275, 300, 325, 350, 375, 400, 425]
             
#y-axis data
y = [0.130, 0.175, 0.223, 0.272, 0.317, 0.369, 0.415, 0.462, 0.508, 0.549]

#Note: len(x) = len(y)

# plotting the points 
plt.plot(x, y, color='black', linestyle='None', linewidth = 2,
         marker='o', markerfacecolor='black', markersize=5)             

# setting x and y axis range
plt.yticks(np.arange(0, 0.7, step=0.05))
plt.xticks(np.arange(200, 450, step=25))


# naming the x axis
plt.xlabel('Distance Between Optical Fiber Faces (µm)')
# naming the y axis
plt.ylabel('Trap Depth (eV)')
 
#Adding gridlines 
plt.grid()
# function to show the plot
plt.show()
