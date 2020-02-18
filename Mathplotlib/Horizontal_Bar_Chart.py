# this show us the horizontal Bar Graph using "plt.barh(x,y)"

from matplotlib import pyplot as plt
x = ['A','B','C','D','E']
y = [5,4,1,3,2]
plt.barh(x,y,color = 'purple')
plt.title("Horizontal Bar Graph")
plt.xlabel("Math Score")
plt.ylabel("Students")
plt.show()