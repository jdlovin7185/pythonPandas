import pandas as pd

df1 = pd.DataFrame({
    'Employee': ['Kyle', 'Stan', 'Kenny', 'Cartman'],
    'Group': ['Accounting', 'Engineering', 'Engineering', 'HR']
                    })

df2 = pd.DataFrame({
    'Employee': ['Kyle', 'Stan', 'Kenny', 'Cartman'],
    'Hire_date': [2004, 2008, 2012, 2014]
})

dataframes_concat = pd.concat([df1, df2], sort=False)
print("Before merge\n", dataframes_concat)


# Performs an inner join where needed, almost like how you will do it in
# SQL, but pandas does it for you
# With the How parameter
df3 = pd.merge(df1, df2)
print("After merge\n", df3)
