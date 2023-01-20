import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019_happy_data.csv', nrows=10)

line_df = df.groupby(by=['Score'])

line_df = line_df.mean()

fig = plt.figure(figsize=[8, 4])

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(line_df['GDP per capita'], label='GDP per capita')
ax.plot(line_df['Social support'], label='Social support')
ax.plot(line_df['Healthy life expectancy'], label='Health')

# little extra style on the line chart
# plt.text(75.5, 1.14, 'GDP per capita',
#          va='center',  # va = vertical alignment
#          rotation=4,  # rotation
#          bbox=dict(
#              boxstyle='round',
#              facecolor='wheat',
#              alpha=0.3
#          )
#          )


ax.set_title('Line chart')
ax.set_ylabel('Values', fontsize=15)
ax.set_xlabel('Rank', fontsize=15)

ax.legend()

plt.show()
