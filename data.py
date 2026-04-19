import numpy as np
import pandas as pd

df = pd.read_excel("placement.xlsx")
print(df.head())

x_train = df.iloc[:, 0].tolist()
y_train = df.iloc[:, 1].tolist()

print(x_train)
print(y_train)
