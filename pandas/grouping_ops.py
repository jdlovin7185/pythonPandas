import pandas as pd

df = pd.read_csv('../dataset.csv')

group_by_track_genre = df.groupby(['track_genre']).count()[['artists']]

# print(group_by_track_genre)

grouped_multiple = df.groupby(['artists', 'track_genre']).agg({'popularity': ['mean', 'min', 'max']})

grouped_multiple.columns = ['popular_mean', 'popular_min', 'popular_max']

grouped_multiple = grouped_multiple.reset_index()

print(grouped_multiple.head())
