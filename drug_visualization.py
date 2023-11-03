import pandas as pd
import matplotlib.pyplot as plt
#specifiying the column names and reading the csv file
columns = ['age','alcohol-frequency','marijuana-frequency','cocaine-frequency','crack-frequency','oxycontin-frequency','tranquilizer-frequency','stimulant-frequency','meth-frequency','sedative-frequency']
drugs=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug-use-by-age.csv",usecols=columns)
#setting 'age' as the index
drugs.set_index('age',inplace=True)
print(drugs)
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
