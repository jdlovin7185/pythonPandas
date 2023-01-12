import pandas as pd
import numpy as np

df = pd.read_json('example.json')

df_head = df.head()

df_head.set_index('Calories', inplace=True)

print(df_head)


