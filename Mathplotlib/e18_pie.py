import matplotlib.pyplot as plt
class BasicPie():
    def __init__(self, title, data):
        self.title = title
        self.data = data
    def show(self):
        pielabels = []
        popularity = []
        explodes = [0.1,0,0,0,0]
        colors = ['#24f0db','#cef024','#f09b24','#da99e8','#82315a','#e38f8f']
        circles = plt.Circle((0, 0), 0.2, fc='#ffffff')
        plt.gcf().gca().add_artist(circles)
        for key, value in self.data:
            pielabels.append(key)
            popularity.append(value)
        plt.pie(popularity,labels = pielabels,explode = explodes, autopct = '%i%%',shadow = True,colors = colors)
        plt.title(title, bbox={'facecolor': '0.8', 'pad': 5})
        return plt.show()
    def save(self, filename):
        pielabels = []
        popularity = []
        explodes = [0.1, 0, 0, 0, 0]
        colors = ['#24f0db', '#cef024', '#f09b24', '#da99e8', '#82315a', '#e38f8f']
        circles = plt.Circle((0, 0), 0.2, fc='#ffffff')
        plt.gcf().gca().add_artist(circles)
        for key, value in self.data:
            pielabels.append(key)
            popularity.append(value)
        plt.pie(popularity, labels=pielabels, explode=explodes, autopct='%i%%', shadow=True, colors=colors)
        plt.title(title, bbox={'facecolor': '0.8', 'pad': 5})
        plt.tight_layout()
        plt.savefig(filename+".png")
title = "My Day"
data = (("A", 10), ("B", 15), ("C", 20), ("D", 30), ("E", 25))
A = BasicPie(title,data)
A.show()
A.save("random")


