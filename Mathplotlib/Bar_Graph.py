# without Vertical Alingment Y positional argument
# not show values or labels on top of bar
from matplotlib import pyplot as plt
x = [1, 2, 3, 4, 5]
y = [5, 7, 3, 8, 4]
plt.bar(x,y)
plt.title("simple Bar graph")
plt.xlabel("Students")
plt.ylabel("Math Score")
plt.bar(x,y,color='yellow')
plt.show()