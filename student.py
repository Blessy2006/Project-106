import plotly.express as px
import csv

with open("Student.csv") as csvFile:
    df = csv.DictReader(csvFile)
    fig = px.scatter(df,x = "Roll No", y = "Marks In Percentage", 
    z = "Days Present")
    
fig.show()    
