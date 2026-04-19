import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from lr import myLR

df = pd.read_excel("placement.xlsx")
print("printing few rows of excel which we imported in variable df", df.head())

#x = df.iloc[:, 0].tolist() -> to python list
#y = df.iloc[:, 1].tolist()

x = df.iloc[:, 0].values #-> to pandas array
y = df.iloc[:, 1].values

print("variable type of x after being converted to np array: ", type(x))
print("Lets also print value of column cgpa, which we imported from excel and converted to np array", x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2) #-> also this function takes numpy array. splits your data for testing and training purpose. 80%

#calling class function now

lr = myLR()
print("class function is being called next")
lr.fit(x_train, y_train)

print("test samples below of x, predict y")
lr.predict(x_test)

print("till here we can say values are being passed in properly in fit and predict functions.")
# next caluculate mean of x, y - which is used in caluclating m and b (slope and intercept of best fit line)
