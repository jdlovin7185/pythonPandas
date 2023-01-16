import pandas as pd

marks = [
    {'Chemistry': 67, 'Physics': 45, 'Math': 50, 'British': 19, 'Rhythm': 20},
    {'Chemistry': 90, 'Physics': 92, 'Math': 87, 'British': 90, 'Rhythm': 77},
    {'Chemistry': 66, 'Physics': 72, 'Math': 81, 'British': 72, 'Rhythm': 50},
    {'Chemistry': 32, 'Physics': 40, 'Math': 12, 'British': 68, 'Rhythm': 95}
]

# when ran, it makes sense
# index can be defined as the rows go down
# I used random names so don't hate me
marks_df = pd.DataFrame(marks, index=['Billy Bob', 'Tom Cruise', 'Rick Flair', 'Snoop Dogg'])

print(marks_df)

# seeing if someone failed a class
# grade > 33

f = marks_df < 33

print(marks_df.mask(f, 'Fail'))

# mask function takes in
# condition, other = nan (optional), inplace = False, (optional), axis = None (optional
