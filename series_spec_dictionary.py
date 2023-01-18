import numpy as np
import pandas as pd

car_price_dict = {
    'Swift': 70000,
    'Civic': 160000,
    'Jazz': 80000,
    'Altis': 180000,
    'Gallardo': 300000
}

# comes out like a normal table but its a dictionary
car_price = pd.Series(car_price_dict)
print(car_price)
