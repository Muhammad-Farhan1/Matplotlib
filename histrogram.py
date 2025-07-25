import matplotlib.pyplot as plt

ages = [10 ,34, 45, 32, 54, 34, 67, 55, 43, 32, 56,59,11,23,67,45,66,60,65]

plt.hist(ages , bins=6 , color='lightpink' , edgecolor='black' , width=1.4)
plt.xlabel('Ages of peeps')
plt.ylabel('Number of peeps')
plt.title('peeps with different age')
plt.show()