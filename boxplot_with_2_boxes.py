import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019_happy_data.csv')

# getting to columns from the csv file
nice_list = [df['Social support'], df['Generosity']]

fig = plt.figure(figsize=[6, 5])

ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('Distribution of Social support vs Generosity')
ax.set_ylabel('Y Label')

ax.boxplot(nice_list, widths=0.5)

plt.show()
