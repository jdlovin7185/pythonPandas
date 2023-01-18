import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('2019_happy_data.csv')

# giving the info for the dataframe
df.info()

# replacing null values in 'popularity' with its mean value
# df['popularity'].fillna(df['popularity'].mean(), inplace=True)

# making a boxplot
fig = plt.figure(figsize=[6, 6])

# setting the axis
ax = fig.add_axes([0, 0, 1, 1])
ax.set_title('Distribution of Social Support vs Generosity')

# plotting the boxplot
ax.boxplot(df['Social support'])

# fig.show()
#
plt.show()
