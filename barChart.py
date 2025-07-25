import matplotlib.pyplot as plt

years = [2001 , 2002 , 2003 , 2004]
sales = [500 , 340 , 450 , 200]
'''
plt.bar(years , sales , color = 'orange', label = 'Sale Of Years' , edgecolor = 'blue')
plt.title("Last Four year sales")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend()
plt.show()
'''
#If you want the bars to be displayed horizontally instead of vertically, use the barh() function:

year = [2 , 4 , 6 , 8]
population = [90 , 85 , 79 , 99]

plt.barh(year, population, color='blue', label='population inspection', edgecolor='white')
plt.title("Population in Different years")
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend(loc='lower right')
plt.show()