import pandas as pd
#Merge DataFrame
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})

#df3=pd.merge(df1,df2,on="city") #It will merge the 2 dataframes and in "on" you have to pass argument in which you want to merge the dataframe

df3=pd.merge(df1,df2,on="city", how="inner") #in how argument you to pass parameter according to your need (left,right,outer,etc)
print(df3)