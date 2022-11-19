#needed librarys 
import pandas as pd
import csv


df = pd.read_csv(r'Path to csv') #CSV File location
df1 = df[['description', 'name','family','password','email id']] #change this based on your csv header or csv column title

header = ['data'] #give the title you want to import all columns to it
with open(r'Path to csv', 'w' , encoding='UTF8') as f:

    writer = csv.writer(f)
    # CREATING HEADER
    writer.writerow(header)
    # WRITING DATA TO 1 ROW
    writer.writerow(df1.values)
