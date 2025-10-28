import numpy as np
import pandas as pd 

np.random.seed(42)

#Create synthetic data
n = 100
age = np.random.randint(18,60,n)
income = age*1200 + np.random.randint(10000, 20000, n)
spending_score = np.random.randint(1,1000,n)
gender = np.random.choice([0,1],n)
purchased = (income> 40000).astype(int)

df = pd.DataFrame({
    'Age': age,
    'Income': income,
    'Spending_Score': spending_score,
    'Gender': gender, 
    'Purchased': purchased
    })


print(df.describe())
print(df.head())
print(df.groupby('Gender')['Income'].mean())