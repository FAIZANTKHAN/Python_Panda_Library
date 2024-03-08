import pandas as pd
#Concat DataFrame
india_weather = pd.DataFrame({
    "city": ["mumbai","delhi","banglore"],
    "temperature": [32,45,30],
    "humidity": [80, 60, 78]
})

us_weather = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
    "humidity": [68, 65, 75]
})

#df=pd.concat([india_weather,us_weather])  #Concat the both the dataframe in one single data frame
df=pd.concat([india_weather,us_weather], keys=["india","us"]) #Concating the data on the basis of key us and india
print((df.loc["us"])) #for printing only the US data from the concated data
print((df.loc["india"]))#for printing only the INDIA data from the concated data