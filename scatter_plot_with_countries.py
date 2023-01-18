import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# reading the first 50 rows of the dataset
from matplotlib import cm

df = pd.read_csv('2019_happy_data.csv', nrows=10)

fig = plt.figure(figsize=[12, 5])

ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('Scatter plot of social support and GDP per capita based on origin')
ax.set_ylabel('Social support')
ax.set_xlabel('GDP per capita')

country_list = df['Country or region'].unique()

colors = cm.jet(np.linspace(0, 1, len(country_list)))

for country, color in zip(country_list, colors):
    x = df[df['Country or region'] == country]['Social support']
    y = df[df['Country or region'] == country]['GDP per capita']
    plt.scatter(x, y, color=color, label=country)

plt.legend()

plt.show()
