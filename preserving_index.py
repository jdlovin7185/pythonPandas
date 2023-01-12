import pandas as pd
import numpy as np

# marks = [
#     {'Chemistry': 67, 'Physics': 45, 'Math': 50, 'British': 19, 'Rhythm': 20},
#     {'Chemistry': 90, 'Physics': 92, 'Math': 87, 'British': 90, 'Rhythm': 77},
#     {'Chemistry': 66, 'Physics': 72, 'Math': 81, 'British': 72, 'Rhythm': 50},
#     {'Chemistry': 32, 'Physics': 40, 'Math': 12, 'British': 68, 'Rhythm': 95}
# ]

marks = {'Chemistry': [67, 90, 66, 32],
         'Physics': [45, 92, 72, 40],
         'Math': [50, 87, 81, 12],
         'English': [19, 90, 72, 68],
         'Rhythm': [20, 77, 50, 95]
         }

marks_df = pd.DataFrame(marks, index=['Billy Bob', 'Tom Cruise', 'Rick Flair', 'Snoop Dogg'])

# print(marks_df)

# encrypting the marks as sine of marks

# np.sin function
encrypted_marks = np.sin(marks_df)
# print(encrypted_marks)

# we can reset the index using the reset_index(), it adds another index column 0, 1, 2...etc.
encrypted_marks.reset_index(inplace=True)
print(encrypted_marks)
