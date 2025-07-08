
# Add a new column to the exiting table & then increasing the salary percentage
#using insert
#updating
import pandas as pd

data = {

 "Name" : ['sumaya','rizvi','mahad','mousia','suma'],
 "Age":[10,20,30,40,50],
 "salary" : [50000,60000,52000,68000,72000],
 "perfomance_score":[45,67,23,48,78]

}


df= pd.DataFrame(data)
print(df)

df["Bonus"] = df['salary'] * 0.1
print(df)


#using insert
#df.insert(loc,"column_Name",some_data)

df.insert(2,"ID",[10,20,30,40,50])
print(df)

#updating
df.loc[0, 'salary'] = 55000
print(df)

#increasing salary by 5%

df['salary'] = df['salary']*1.05
print(df)
