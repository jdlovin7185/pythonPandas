import pandas as pd
import matplotlib.pyplot as plt
from pandas._libs.reshape import explode

df = pd.read_csv('nobel_final.csv')

pie_df = pd.DataFrame()

pie_df['Count'] = df['category'].value_counts()

pie_df = pie_df.reset_index()

pie_df.rename(columns={'index': 'category'}, inplace=True)

print(pie_df)

fig = plt.figure(figsize=[8, 6])

ax = fig.add_axes([0, 0, 1, 1])

# setting axes
ax.set_title('Nobel Peace prizes by Category')

ax.pie(pie_df['Count'], labels=pie_df['category'])

plt.show()
