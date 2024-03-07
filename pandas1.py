import pandas as pd



# Read CSV file
df = pd.read_csv('pandas1.csv')

#print(df.event) ---->to print the event
#print(type(df['event'])) ----for print the type of event
#print(df) ----->for whole table
#print(df[['day','event']])  ---->to just print the day and event
#print(df.describe( )) ----for showing all the statistical data

#print(df['temp'].max( ))-->print the max
#print(df[df.temp>=32])-->print the data on which day the temp>=32

#print(df.set_index("day"))-->set the index at day it just return
#print(df.set_index('day',inplace=True))--it actually modify the actual data
#print(df.set_index('event' ,inplace=True))
#print(df.loc['snow'])  -->After setting the index as events and modify it by using inplace we can access and localise the data using any event which is present in it



