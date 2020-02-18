import matplotlib.pyplot as plt
import pandas as pd
class PieChartContainer():
    def __init__(self, pc_data_arr):
        self.pc_data_arr = pc_data_arr
    def show(self):
        # fig = plt.figure(figsize = (4,4))
        # for i in range (1,len(self.pc_data_arr)+1):
        #     fig.add_subplot(4,4,i)
        #     plt.pie(self.value_key,self.pc_data_arr[i-1],autopct='%1.1f%%', labels = self.pc_data_arr[i-1])
        # plt.show()
        for i in range (len(self.pc_data_arr)):
            plt.pie(self.pc_data_arr[i],labels=self.pc_data_arr[i])
        plt.show()

class PieChartData():
    def __init__(self,csv_filename, name_key, value_key):
        self.csv_filename = csv_filename
        self.name_key = name_key
        self.value_key = value_key
    def get_name(self):
        r = pd.read_csv(self.csv_filename)
        name = r[self.name_key]
        values = r[self.value_key]
        print (name)
        print (values)


    # def show(self):
    #     df = plt.read_csv(self.csv_filename)
    # def save(self,filename):


CD1 = PieChartData("random_data.csv","names","values")
CD2 = PieChartData("courses_data.csv","courses","values")
CD3 = PieChartData("courses_data.csv","courses","values")
CD4 = PieChartData("random_data.csv","names","values")

pc_array = [CD1, CD2, CD3, CD4]
pc_container = PieChartContainer(pc_array)
pc_container.show()
# pc_container.save("random_courses.png")