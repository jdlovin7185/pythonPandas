import pandas as pd
import numpy as np

marks = {'Chemistry': [67, 90, 66, 32],
         'Physics': [45, 92, 72, 40],
         'Math': [50, 87, 81, 12],
         'English': [19, 90, 72, 68],
         'Rhythm': [20, 77, 50, 95]
         }

marks_df = pd.DataFrame(marks, index=['Billy Bob', 'Tom Cruise', 'Rick Flair', 'Snoop Dogg'])

# we are going to add 5 points to all the marks above
# new_marks = marks_df + 5


# we can be more specific with where we apply the extra points
# you'll get an error with you do not have the perfect amount of values for the given DataFrame
new_marks = marks_df + [5, 10, 10, 2, 0]
# print(new_marks)

# this is to get the columns summary using axis = 0
marks_column_summary = marks_df.apply(np.sum, axis=0)

# print(marks_column_summary)

marks_row_summary = marks_df.apply(np.sum, axis=1)
# print(marks_row_summary)

average_of_scores = marks_df.apply(func=np.mean, axis=0, result_type='broadcast')
print(average_of_scores)
