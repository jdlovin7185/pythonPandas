import pandas as pd

data = pd.read_csv('dataset.csv')

genre_dancie = crosstab(data['track_genre'], data['danceability'])
print(genre_dancie)
