import pandas as pd
import numpy as np

df=pd.read_csv("weather_data.csv")
#new_df=df.replace(-9999,np.NaN)   #Replace the -9999 with NaN

#new_df=df.replace({                #By this you can replce the value acc to the specific coloumn
#    'temperature': -9999,
#  'windspeed':  -9999,
#    'event': '0'
#},np.NaN)

df2=pd.DataFrame({
    'score':['exceptional','average','good','poor','average','exceptional'],
    'student':['rob','maya','parthiv','tom','Julian','erica']
})

#new_df2=df2.replace(['poor','average','good','exceptional'],[1,2,3,4])  #For mapping the grade


