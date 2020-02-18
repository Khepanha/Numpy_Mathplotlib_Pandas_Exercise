# show values or labels on top of bar
from matplotlib import pyplot as plt
x = [1,2,3,4,5]
y = [1,2,3,4,5]
plt.bar(x,y)
plt.title("Bar Graph")
plt.xlabel("students")
plt.ylabel("Score")
barplot = plt.bar(x,y,color='green')
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
plt.show()