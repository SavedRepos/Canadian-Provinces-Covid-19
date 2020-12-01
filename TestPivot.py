import numpy as np
import pandas as pd

# "Date", "Region", "New_Tests", "Total_Tests", "Positivity", "Turn_Around"
url = 'http://www.bccdc.ca/Health-Info-Site/Documents/BCCDC_COVID19_Dashboard_Lab_Information.csv'

df = pd.read_csv(url)
print(df.info())
df['New_Positives'] = df['New_Tests'] * df['Positivity']
print(df.info())
print(df.tail())
