import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019_happy_data.csv')

fig = plt.figure(figsize=[10, 5])

ax = fig.add_axes([0, 0, 1, 1])

ax.scatter(df['Social support'], df['GDP per capita'])
ax.set_title('Scatter plot of Social support and GDP per capita', fontsize=15)
ax.set_ylabel('Social Support', fontsize=15)
ax.set_xlabel('GDP per capita', fontsize=15)

plt.show()
