import numpy as np
import pandas as pd

# first way of creating a DataFrame

car_price_dict = {
    'Swift': 70000,
    'Civic': 160000,
    'Jazz': 80000,
    'Altis': 180000,
    'Gallardo': 300000
}

car_price = pd.Series(car_price_dict)
# print("Before creating a DataFrame\n", car_price)

# created the DataFrame and named a column
car_data = pd.DataFrame(car_price, columns=['Car Price'])
# print("After creating a DataFrame\n", car_data)

# Second way to create a DataFrame

data = [
    {'Name': 'Phil', 'Marks': 28},
    {'Name': 'Billy', 'Marks': 27},
    {'Name': 'Jill', 'Marks': 26},
    {'Name': 'Sarah', 'Marks': 28}
]

data_data_frame = pd.DataFrame(data)
# print(data_data_frame)


# Third way of creating a DataFrame

class_data = pd.DataFrame([
    {'Subodh': 20, 'Ram': 25},
    {'Abdoul': 29, 'John': 24}],
    index=['Mathematics', 'Physics']
)

# print(class_data)

# 4th way of creating a DataFrame

data_json = pd.read_json('example.json')
print(data_json)

