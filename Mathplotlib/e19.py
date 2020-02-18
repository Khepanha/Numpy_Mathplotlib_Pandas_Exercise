
# Get the data from csv file using pandas and print it as a piechart
#and save the piechart image in the directory.


import matplotlib.pyplot as plt
import pandas as pd
def gen_pie(title, csv_filename, out_filename, names_key, values_key):
    df = pd.read_csv(csv_filename)
    names_key = df[names_key]
    values_key = df[values_key]
    circles = plt.Circle((0,0),0.2,fc = '#ffffff')
    plt.gcf().gca().add_artist(circles)
    colors = ['#24f0db','#cef024','#f09b24','#da99e8','#82315a','#e38f8f']
    plt.pie(values_key,labels = names_key, autopct = '%1.1f%%',colors=colors, shadow = True, startangle = 0)
    plt.title(title,bbox = {'fc' : '#dce627', 'pad' : 5})
    plt.tight_layout()
    plt.savefig(out_filename)
    return ('PieChart image had saved as D1.png in your directory.')
print (gen_pie("Random", "random_data.csv", "D1.png", "names", "values"))



