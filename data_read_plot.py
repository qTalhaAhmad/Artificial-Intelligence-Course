import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("dataset.csv")
print(df)

x = np.array(df['Annual_Income_(k$)'])
y = np.array(df['Spending_Score'])

plt.scatter(x, y)
plt.show()
