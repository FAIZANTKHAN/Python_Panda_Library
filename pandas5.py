import pandas as pd
df=pd.read_csv("weather.csv")


#new_df=df.fillna(0)  #NaN will replace with 0
#new_df=df.fillna({                  #It will replace according to the value assign with coloumn
#  'temperature':0,
#    'windspeed':0,
#    'event':'no event'
#})


#new_df=df.fillna(method="ffill") #Fill the next NaN with the previous value default-vertical direction
#new_df=df.fillna(method="bfill")  #Fill the previous NaN with the current value default-vertical direction
#new_df=df.fillna(method="bfill" ,axis="columns")  #just like previous case but in horizantal manner
#new_df=df.fillna(method="ffill",limit=1)  # just like previous case but only copy one time

#new_df=df.interpolate() #It come with some better estimation

#new_df=df.dropna() #it will delete all the NaN value containing data
#new_df=df.dropna(how="all") #It only delete when all the data in row will contain NaN
#new_df=df.dropna(thresh="2") #If the row contain that no.of NaN which is passed in the thresh value then only it will delete the row or the data
print(new_df)