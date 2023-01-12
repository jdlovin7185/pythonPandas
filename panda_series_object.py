import numpy as np
import pandas as pd

# series takes in any kind of data type, but it is a one dimensional array
# series can take in firstly the data that you want to pass, can be a list, a list of lists, or even a dictionary
# second is index, it can be defined if its explicitly required,
# third is the dtype, it represents the data type used in the series

series = pd.Series(data=[78, 92, 36, 64, 89])
# prints out the data, along with what index it is in
# print(series)

# prints jus the values
# print(series.values)

# gives you a range index, start, stop, and step
# print(series.index)

# you can access the values like a traditional array
# print(series[1])

# you can do some traditional slicing as well
print(series[1:3])


