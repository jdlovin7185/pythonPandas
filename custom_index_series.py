import pandas as pd
import numpy as np

# custom stuff
data = pd.Series(data=[70000, 80000, 160000, 1800000, 300000], index=['Swift', 'Jazz', 'Civic', 'Altis', 'Gallardo'])
# print(data)

# then like a traditional array, you can access it by index but with the name of the index that you customized
# print('Swift')

# then some custom slicing and dicing, jus no dicing
print(data['Jazz': 'Gallardo'])

