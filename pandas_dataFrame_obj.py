import numpy as np
import pandas as pd

car_price_dict = {
    'Swift': 70000,
    'Civic': 160000,
    'Jazz': 80000,
    'Altis': 180000,
    'Gallardo': 300000
}

car_man_dict = {
    'Swift': 'Maruti',
    'Jazz': 'Honda',
    'Civic': 'Honda',
    'Altis': 'Toyota',
    'Gallardo': 'Lamborghini'
}

car_price = pd.Series(car_price_dict)
car_man = pd.Series(car_man_dict)

# print(car_price)
# print(car_man)

cars = pd.DataFrame({'Price': car_price, 'Manufacturer': car_man})
# print(cars)

# price is the key in the DataFrame
# print(cars['Price'])

# jus like price, manufacturer is the same way
print(cars['Manufacturer'])



