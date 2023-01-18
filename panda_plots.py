import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('dataset.csv')

df.plot(x='track_genre', y='popularity', marker='o', kind='scatter')

plt.show()
