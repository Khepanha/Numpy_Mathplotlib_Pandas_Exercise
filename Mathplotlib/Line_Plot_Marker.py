# Add Marker in Line plot

from matplotlib import pyplot as plt
import pandas  as pd

df = pd.DataFrame({"Year" : [2014,2015,2016,2017,2018], "Sales" : [2000, 3000, 4000, 3500, 6000]})
plt.plot(df["Year"],df["Sales"])
plt.title("Line Plot")
plt.xlabel("Year")
plt.ylabel("Sales")
ax = df.plot(x="Year", y="Sales", kind="line", title ="Simple Line Plot", legend=False, style = 'r--')
ax.set(ylabel='Sales', xlabel = 'Year', xticks =df["Year"])
plt.style.use('fivethirtyeight')

plt.show()