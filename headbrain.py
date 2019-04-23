%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0,10.0)

#Reading Data
data = pd.read_csv('headbrain.csv')
print(data.shape)
data.head()

#collecting X & Y
X = data['Head Size(cm^3)'].values
Y = data['Brain Weight(grams)'].values

#calculating mean of X & Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

#calculating total number of values
n = len(X)

#finding the values of slope(m) & constant(c)
numerator = 0;
denominator = 0;

for i in range (n):
    numerator += (X[i] - mean_x) * (Y[i] - mean_y)
    denominator += (X[i] - mean_x) ** 2
    
m = numerator / denominator
print(m)

c = mean_y - (m * mean_x)
print(c)

#plotting values & regression line

max_x = np.max(X) + 100
min_x = np.min(X) - 100

#claculating the line value x & y
x = np.linspace(min_x, max_x, 1000)
y = (m * x) + c

#Ploting Line
plt.plot(x, y, color='#58b970', label='Regression Line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='Scatter Plot')

plt.xlabel('Head Size in cm3')
plt.ylabel('Brain Weight in grams')
plt.legend()
plt.show()

#for calculating Root Mean Square error
ss_t = 0
ss_r = 0;
for i in range(n):
    yp = (m * X[i]) + c
    ss_t += (yp - mean_y) ** 2
    ss_r += (Y[i] - mean_y) ** 2
r2 = ss_t/ss_r
print(r2)

