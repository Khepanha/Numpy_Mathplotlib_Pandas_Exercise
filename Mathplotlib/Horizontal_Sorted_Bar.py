# we will sort all the bar from small to big

from matplotlib import pyplot as plt
x = ['A','B','C','D','E']
y = [5,4,1,3,2]
plt.title("Horizontal Sorted Bar")
plt.xlabel("Math Score")
plt.ylabel("Students")
y,x = zip(*sorted(zip(y,x)))
plt.barh(x,y,color = 'red')
plt.show()