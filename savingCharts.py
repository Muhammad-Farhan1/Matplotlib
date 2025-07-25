import matplotlib.pyplot as plt

x = [2,4,6,8]
y=[20,60,33,90]

plt.bar(x,y, color='blue',edgecolor='white'  ,width=1.5)
plt.title('Practice of Bar Chart Saving')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig('saving_Chart.png', dpi=300 , bbox_inches='tight')
plt.show()