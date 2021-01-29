from collections import OrderedDict
import matplotlib.pyplot as plt
import pandas as pd
class DataReader():
    def __init__(self) -> None:
        self.departments=dict()
        self.electives=dict()
        self.sections=dict()
        self.electiveNames=OrderedDict({'IT1654':'Data Science','IT1653':'A.I','CS1653':'Cloud Computing','CS1650':'Distributed Databases','CC1653':'Internet Of Things','CC1652':'Advanced Internet Technologies','CC1654':'Principles of Software Engineering'})

    #method which will read the excel files and construct a histogram
    def readExcelFile(self,filename):
        allSheets=pd.concat(pd.read_excel('{}.xlsx'.format(filename),sheet_name=None))
        allSheets=allSheets.dropna()
        for index,rows in allSheets.iterrows():
            self.electives[self.electiveNames[index[0]]]=[x+1 for x in self.electives.get(self.electiveNames[index[0]],[0])]
            self.departments[rows['Branch']+' '+rows['Section']]=[x+1 for x in self.departments.get(rows['Branch']+' '+rows['Section'],[0])]
        

    def plotGraphForDe(self):
        newdf=pd.DataFrame(self.electives)
        newdf.plot(kind="bar")
        plt.xticks(rotation=30,horizontalalignment='center')
        plt.show()
    
    def plotGraphForStudents(self):
        newdf=pd.DataFrame(self.departments)
        newdf.plot(kind="bar")
        plt.show()

    