import pandas as pd
#GroupBy
df=pd.read_csv("weather_by_cities.csv")
g=df.groupby('city') #Grouping of data acc to the city

for city, city_df in g:
    print(city)
    print(city_df)

#print(g.max()) #give the max in each group of cities
#print(g.describe()) #Give all the statistical result like mean.median,max.etc