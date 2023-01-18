import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019_happy_data.csv', nrows=50)

fig = plt.figure(figsize=[8, 6])

# setting axis
ax = fig.add_axes([0, 0, 1, 1])

ax.hist(df['Perceptions of corruption'], bins=50)
ax.set_title('Corruption assumption', fontsize=15)
ax.set_ylabel('Frequency', fontsize=15)
ax.set_xlabel('Corruption assumption', fontsize=15)

plt.show()
