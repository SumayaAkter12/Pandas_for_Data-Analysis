#condition


import pandas as pd

data = {

 "Name" : ['sumaya','rizvi','mahad','mousia','suma'],
 "Age":[10,20,30,40,50],
 "salary" : ['50000','60000','52000','68000','72000'],
 "perfomance_score":[45,67,23,48,78]

}


df= pd.DataFrame(data)

high_salary = df[df['salary'] > 50000]
print('Employess with salary')
print(high_salary)