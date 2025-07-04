#Single column return series
#selecting multiple column

import pandas as pd

data = {

 "Name" : ['sumaya','rizvi','mahad','mousia','suma'],
 "Age":[10,20,30,40,50],
 "salary" : ['50000','60000','52000','68000','72000'],
 "perfomance_score":[45,67,23,48,78]

}


df= pd.DataFrame(data)

print("Sample dataframe")
print(df)
print("Names(Single column return series)")
name = df['Name']
print(name)

subset = df[["Name" , "salary"]]
print('\nSubset with Name and salary')
print(subset)
