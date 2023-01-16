import pandas as pd

df = pd.read_csv('../dataset.csv')
# this will sort descending 0 to whatever loudness goes down to
df_loudness = df.sort_values(by='loudness')

# print(df_loudness)

df_ascending_tempo = df.sort_values(['track_genre', 'tempo'], ascending=(1, 0))

print(df_ascending_tempo)
