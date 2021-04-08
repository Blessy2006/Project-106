import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Ice = []
    Cold = []

    with open(data_path) as csvFile:
        df = csv.DictReader(csvFile)
        for row in df:
            Ice.append(float(row["Coffee in ml"]))
            Cold.append(float(row["sleep in hours"]))
    return{"x":Ice,"y":Cold}        

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print(correlation[0,1])

def main():
    data_path = "coffee.csv"
    dataSource = getDataSource(data_path)  
    findCorrelation(dataSource)  
   
main() 
