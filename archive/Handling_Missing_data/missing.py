import pandas as pd

data = {

 "Name" : ['sumaya',None,'mahad','mousia','suma'],
 "Age":[10,None,30,40,50],
 "salary" : [50000,None,52000,68000,72000],
 "perfomance_score":[45,None,23,48,78]

}


df= pd.DataFrame(data)
print(df)


print(df.isnull())
print(df.isnull().sum())