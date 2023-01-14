import pandas as pd

marks_A = {'Chemistry': [67, 90, 66, 32],
           'Physics': [45, 92, 72, 40]
           }

marks_A_df = pd.DataFrame(marks_A, index=['Bob', 'Billy', 'Sarah', 'Jill'])

marks_B = {'Chemistry': [72, 45, 60, 98],
           'Physics': [78, 34, 72, 95]
           }

marks_B_df = pd.DataFrame(marks_B, index=['Natalie', 'Cole', 'Drew', 'Kate'])

# using the concat method to combine to tables together
# if the values are not there, they will show NaN

combined_tables = pd.concat([marks_A_df, marks_B_df], sort=False)
print(combined_tables)
