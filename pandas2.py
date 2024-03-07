import pandas as pd

#df=pd.read_csv("pandas1.csv")-->using csv file as dataframe

#using the excel file is same as the using csv file

data = {'index': [('a', 'b'), ('a', 'c')],
        'columns': [('x', 1), ('y', 2)],
        'data': [[1, 3], [2, 4]],
        'index_names': ['n1', 'n2'],
        'column_names': ['z1', 'z2']}

#df=pd.DataFrame(data)--->using dictionary as a dataframe

#same way we are able to use tuple just we have to pass extra argument columns in which we have to write the name of column
#and list of dictionary