import pandas as pd
import matplotlib.pyplot as plt
#specifiying the column names and reading the csv file
drug_frequency = ['age','alcohol-frequency','marijuana-frequency','cocaine-frequency','crack-frequency','oxycontin-frequency','tranquilizer-frequency','stimulant-frequency','meth-frequency','sedative-frequency']
drugs=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug-use-by-age.csv",usecols=drug_frequency)
#setting 'age' as the index
drugs.set_index('age',inplace=True)
print(drugs)

def PlotLineGraph(data,x_col,y_col,title,legend):
#Plotting the data
    drugs.plot()
    #labelling the x and y axis
    plt.xlabel('age')
    plt.ylabel('Frequency')
    #adding title to the graph
    plt.title('Drug use by age',size=18)
    #Displaying graph legend
    plt.legend(drugs.columns)
    plt.show()

#calling the PlotLineGraph with the data and column name
PlotLineGraph(drugs,'age','alcohol-frequency','Drug use by age','drugs.drug_frequency')

drug_use = ['age','alcohol-use','marijuana-use','cocaine-use','crack-use','oxycontin-use','tranquilizer-use','stimulant-use','meth-use','sedative-use']
drugs=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug-use-by-age.csv",usecols=drug_use)
#setting 'age' as the index
drugs.set_index('age',inplace=True)
total_usage=drugs.sum()

