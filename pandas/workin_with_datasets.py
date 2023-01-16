import pandas as pd
import numpy as np

df = pd.read_csv('../dataset.csv')

# shows the whole file
# print(df)

# shows the first 5 rows
# print(df.head())

# shows the last 5 rows
# print(df.tail())

# gives you the quick summary of the data it is reading
# print(df.describe())

# will show you the null values
# print(df.info())

# drops missing values
# df.dropna(inplace=True)
# print(df.info())

# like accessing an index but in this case it is a whole column
# print(df['track_id'])

# print(df[['track_id']])

# pick which columns you want to be displayed
print(df[['track_id', 'time_signature', 'track_genre']])

