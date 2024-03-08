#Pivot and Pivot Table
import pandas as pd
df=pd.read_csv("weather_by_cities.csv")
#df=df.pivot(index="day",columns="city")  #By this you reshape the data frame by passing value on index(set as row),columns(set as column)
#df=df.pivot(index="day",columns="city",values="temperature") #See data according to the parameter pass on the values argument
df=df.pivot_table(index="city",columns="day",aggfunc="min") #You can any function(max,min,sum,diff,etc)as parameter in the aggfunc argument
print(df)