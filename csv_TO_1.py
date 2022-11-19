import pandas as pd
import csv


df = pd.read_csv(r'C:\Users\APA\Desktop\Email_1401.csv')
df1 = df[['description', 'name','family','password','email id']]

header = ['data']
with open(r'C:\Users\APA\Desktop\export_csv.csv', 'w' , encoding='UTF8') as f:

    writer = csv.writer(f)

    writer.writerow(header)
    
    writer.writerow(df1.values)
