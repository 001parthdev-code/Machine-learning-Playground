import numpy as np
import pandas as pd

np.random.seed(42)
n = 1500 #number of patients 

customer_id = np.arange(1,n+1)
age = np.random.randint(19,60,n)
gender = np.random.choice([0,1],n) #0: Male , 1: female 
income = np.random.randint(30000, 250000, n)
car_type = np.random.choice(['Sedan', 'SUV', 'Hatchback', 'Sports'], n, p=[0.3,0.35,0.25,0.1] )
fuel_type = np.random.choice(['Petrol', 'Diesel', 'Electric'],n, p = [0.45,0.45,0.1])
brand = np.random.choice(['Mercedes', 'BMW', 'Pagani', 'Lexus'], n, p=[0.15, 0.25, 0.35, 0.25])
base_price = {
    'Mercedes': 100000,
    'BMW' : 150000,
    'Pagani': 130000,
    'Lexus': 90000
}

car_modifier = {
    'Sedan': 1.0, 'SUV': 1.3, 'Hatchback': 0.8, 'Sports': 1.8
}

#price for every customer 
purchase_price = np.array([base_price[b]*car_modifier[c]+ np.random.randint(-5000, 5000)
    for b, c in zip(brand, car_type)]
    )

satisfaction_prob = (
    (income / 250000) * 0.5 +
    np.array([1 if b in ['Mercedes', 'BMW'] else 0.7 for b in brand]) * 0.3 +
    np.random.rand(n) * 0.2
)

satisfied = (satisfaction_prob > 0.5).astype(int)

df_cars = pd.DataFrame({
    "CustomerID": customer_id,
    "Age": age,
    "Gender": gender,
    "Income": income,
    "Car_Type": car_type,
    "Fuel_Type": fuel_type,
    "Brand_Preference": brand,
    "Purchase_Price": purchase_price,
    "Satisfied": satisfied
})

print(df_cars.head())
print(df_cars.info())
print(df_cars.describe(include='all'))
print(df_cars.columns)
print(df_cars['Car_Type'].value_counts())
print(df_cars['Fuel_Type'].value_counts())

print(pd.crosstab(df_cars['Gender'], df_cars['Car_Type']))

print(df_cars[(df_cars['Car_Type'] == 'SUV') & (df_cars['Satisfied'] == 1)])
print(df_cars[df_cars['Income'] > 200000])




