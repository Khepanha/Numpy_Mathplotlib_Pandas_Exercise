# we will reverse all the bar

from matplotlib import pyplot as plt
x = ['A','B','C','D','E']
y = [5,4,1,3,2]
plt.title("Horizontal Sorted Bar")
plt.xlabel("Math Score")
plt.ylabel("Students")
y,x = zip(*sorted(zip(y,x)))
plt.barh(x,y,color = 'red')
ax = plt.subplot()
ax.invert_yaxis()
plt.show()