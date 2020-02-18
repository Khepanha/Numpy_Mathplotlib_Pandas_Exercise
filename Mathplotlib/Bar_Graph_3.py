# Bar Graph with hide the "Y" axis
from matplotlib import pyplot as plt
x = [4,1,5,2,3]
y = [1,2,3,4,5]
plt.bar(x,y)
plt.yticks()
plt.title("Bar Graph 3")
plt.xlabel("students")
plt.ylabel("Score")
barplot = plt.bar(x,y,color='orange')
for bar in barplot:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), va='bottom')
    plt.yticks([]) #used to hide the axis "Y" in the graph
plt.show()