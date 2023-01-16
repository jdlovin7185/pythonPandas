import pandas as pd
import numpy as np


df = pd.read_csv('../dataset.csv')

# you can create a table using the pivot table func along with numpy to get a bunch
# of data that you want 'math-ed over'
pivot1 = pd.pivot_table(df, index='artists', aggfunc=np.mean)
print(pivot1)
