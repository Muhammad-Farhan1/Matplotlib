import matplotlib.pyplot as plt

provinces = ['Punjab' , 'KPK' , 'Sindh', 'Balochistan', 'Gilgit-Baltistan']
population = [5005 , 2200 , 3210 , 1101 , 3431]
punjabExplode = [.2,0,0,0,0]


plt.pie(population ,labels=provinces, autopct='%1.1f%%', colors=['lightblue' , 'grey' , 'gold' , 'brown', 'lightpink'] , explode=punjabExplode , shadow=True)

plt.title("Population in each province")
plt.legend(provinces , title="Provinces" ,loc='upper left')
plt.show()