import matplotlib.pyplot as plt

#plot 1
no_of_stds = [1,2,3,4]
marks = [10,6,4,8]
plt.subplot(1,2,1) #the figure has 1 row, 2 columns, and this plot is the first plot.
plt.title('Line Chart')
plt.plot(no_of_stds  , marks , color='brown')


#plot 2
plt.subplot(1,2,2) #the figure has 1 row, 2 columns, and this plot is the second plot.
plt.bar(no_of_stds,marks , color='blue')
plt.title('Bar Chart')

plt.suptitle("Two Charts")
plt.tight_layout()
plt.show()