import matplotlib.pyplot as plt
#----Marker----
x = [1,2,3,4]
y = [15,10,25,30]

#plt.plot(x , y , marker ='o')

#'o' ->	Circle  ,
# '*' ->	Star  ,
#'.' ->	Point etc



#----Format Strings (fmt)----
x = [2,4,6,8]
y = [10,40,30,20]

#plt.plot(x,y , 'o-.')

# '-' -> Solid line, 
# ':' -> Dotted line,
#  '--' -> Dashed line,
#  '-.'	Dashed/dotted line


#----Marker Size(ms)----
#plt.plot(x,y, marker='o' , color='b' , ms=15)

#--- markeredgecolor(mec)---
#plt.plot(x,y, marker = 'D' , color = 'w' , ms = 10 , mec = 'b')

#---markerfacecolor(mfc)---
plt.plot(x,y, marker ='o' , color = 'g', ms = 10 , mec = 'b' , mfc = 'w')
plt.show()
