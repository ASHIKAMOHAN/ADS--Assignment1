import pandas as pd
import matplotlib.pyplot as plt

#specifiying the column names and reading the csv file
drug_frequency = ['age','alcohol-frequency','marijuana-frequency','cocaine-frequency',
                    'crack-frequency','oxycontin-frequency','tranquilizer-frequency','stimulant-frequency',
                    'meth-frequency','sedative-frequency']
drugs=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug-use-by-age.csv",usecols=drug_frequency)
#setting 'age' as the index
drugs.set_index('age',inplace=True)
print(drugs)

def PlotLineGraph(data,x_col,y_col,title,legend):
    """
    Plotting a line graph using the given data.
    Arguments:
    data:pandas DataFrame-contains data to be plotted
    x_col:str-column name for the x axis
    y_col:str-column name for the y axis
    title:str-title for the line plot
    legend:str-legend for the line plot

    Returns:
    None
    """
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

#specifiying the column names and reading the csv file
drug_use = ['age','alcohol-use','marijuana-use','cocaine-use','crack-use',
            'oxycontin-use','tranquilizer-use','stimulant-use','meth-use','sedative-use']
drugs=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug-use-by-age.csv",usecols=drug_use)
#setting 'age' as the index
drugs.set_index('age',inplace=True)
#computing sum of values of each column
total_usage=drugs.sum()
#Extracting the top five values
top_five=total_usage.nlargest(5)
#calculating the cumulative total of drug usage taht falls outside the top five values
top_five['others']=total_usage.sum()-top_five.sum()
def plotpie(drug_use):
    """Plotting a piechart showing usage of drugs by age using specified columns
    Arguments:
    drug_use:list-list of column names indicating the drug usage
    
    Returns:
    None
    """
    #Plotting the graph
    plt.figure()
    plt.pie(top_five,labels=top_five.index,autopct='%1.1f%%')
    plt.title('Drug use by age')
    plt.show()
plotpie(drug_use)   

drug_deaths=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug_deaths.csv")
def PlotBarGraph(data):
    """plotting bar graph using the given data and column names.
    Arguments:
    data:pandas DataFrame-contains the data to be plotted

    Returns:
    None
    """
    #Plotting bar graph for the 'Age' column
    plt.figure(figsize=(10,6))
    age_counts=drug_deaths['Age'].value_counts().sort_index()
    age_counts.plot(kind='bar')

    #plotting the bar graph
    plt.xlabel('Age')
    plt.ylabel('Death count')
    plt.title('Drug Deaths')
    plt.xticks(range(0,len(age_counts),5),labels=age_counts.index[::5],rotation=0)
    plt.tight_layout()
    plt.show()
PlotBarGraph(drug_deaths)