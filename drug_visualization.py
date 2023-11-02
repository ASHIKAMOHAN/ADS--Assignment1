import pandas as pd
import matplotlib.pyplot as plt
rows = ['age','alcohol-use','alcohol-frequency','marijuana-use','marijuana-frequency','cocaine-use','cocaine-frequency','crack-use','crack-frequency','oxycontin-use','oxycontin-frequency','tranquilizer-use','tranquilizer-frequency','stimulant-use','stimulant-frequency','meth-use','meth-frequency','sedative-use','sedative-frequency']
drugs=pd.read_csv("C:\\Users\\ashik\\Desktop\\ADS\\ASSIGNMENTS\\drug\\drug-use-by-age.csv",usecols=rows)
print(drugs)
drugs.plot()

plt.show()
