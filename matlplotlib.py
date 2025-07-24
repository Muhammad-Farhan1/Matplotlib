#Matplotlib is a low level graph plotting library in python that serves as a visualization utility.

#Most of the Matplotlib utilities lies under the pyplot submodule, and are usually imported under the plt alias:
import matplotlib.pyplot as plt
import numpy as np 

x = [1,2,3,4,5,6]
y = [110,50,150,250,100,210]

#The plot() function is used to draw points (markers) in a diagram.
plt.plot(x,y , label="Sales data")
plt.title("Sales Data Visualize")
plt.xlabel("Month")
plt.ylabel("Units Sold")

plt.legend(loc='upper left')
plt.grid(ls=':')
plt.xlim(1,6)
plt.ylim(50,270)
plt.show()