import pandas as pd

df = pd.read_csv('../dataset.csv')

df_rock_genres = df.loc[df['track_genre'] == 'rock'].head()

# sorting through csv file to get specific values
# print(df_rock_genres)

# using the spotify dataset to get the rock songs with a tempo greater than 105 BPM
df_headbangers_rock = df.loc[(df['track_genre'] == 'rock') & (df['tempo'] > 105)]

# print(df_headbangers_rock)

# get the dance floor ready for this playlist
# popularity is greater than 90
# dance-ability is greater than 0.750, not sure what the rating is tho
df_dance_floor_bruiser = df.loc[(df['popularity'] > 90) & (df['danceability'] > 0.750)]

print(df_dance_floor_bruiser)
