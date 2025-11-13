import numpy as np 

np.random.seed(42)

n = 100

x1= np.random.uniform(1,10,n)

x2= np.random.uniform(1,10,n)

noise = np.random.normal(0,1,n)

y= 5*x1 + 2*x2 + noise 

X = np.column_stack((x1,x2))
y = np.reshape(-1,1)

# Print essentials
print("X shape:", X.shape)
print("y shape:", y.shape)
print("First 5 samples:\n", X[:5], "\n", y[:5])

# Stats
print("Mean per feature:", np.mean(X, axis=0))
print("Std per feature:", np.std(X, axis=0))
print("Correlation x1-x2:", np.corrcoef(x1, x2)[0,1])
