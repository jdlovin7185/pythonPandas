import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019_happy_data.csv', nrows=10)

# bar graph works better givin a yearly comparison
grouped_df = df.groupby(['Social support']).count()[['Country or region']]
grouped_df.reset_index(inplace=True)

fig = plt.figure(figsize=[7, 5])
# setting axis
ax = fig.add_axes([0, 0, 1, 1])
ax.set_title("Socially supportive", fontsize=15)
ax.set_ylabel('countries', fontsize=15)
ax.set_xlabel('Social support', fontsize=15)

# plotting the bar graph
ax.bar(grouped_df['Social support'], grouped_df['Country or region'])

plt.show()
