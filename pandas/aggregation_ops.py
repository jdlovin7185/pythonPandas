import pandas as pd

df = pd.read_csv('../dataset.csv')


# aggregate function is used to to find the minimum and maximum values of the numerical values
list1 = [col for col in df.columns if df[col].dtype in ['float', 'int64']]
aggregate = df[list1].agg(['min', 'max'])
print(aggregate)
