import matplotlib.pyplot as plt
import numpy as np
import sys

# ML model: linear regression
def f_wb(w, b, x):
    return w*x + b

# cost function: mean squared error / 2
def Jcost(X, Y, w, b):
    n = len(X)
    cost = 0
    for i in range(n):
        cost += (f_wb(w, b, X[i]) - Y[i])**2
    cost /= (2*n)
    return cost

def weightDerivative(X, Y, w, b):
    n = len(X)
    derivative = 0
    for i in range(n):
        derivative += (f_wb(w, b, X[i]) - Y[i])*X[i]
    derivative /= n
    return derivative

def biasDerivative(X, Y, w, b):
    n = len(X)
    derivative = 0
    for i in range(n):
        derivative += (f_wb(w, b, X[i]) - Y[i])
    derivative /= n
    return derivative

def gradientDescent(X, Y, alpha = 0.01, tolerance = 1):
    n = len(X)
    w, b = 0, 0
    cost = float("inf")
    iter = 0
    while cost > tolerance:
        iter += 1
        temp_w = w - alpha * weightDerivative(X, Y, w, b)
        temp_b = b - alpha * biasDerivative(X, Y, w, b)
        w, b = temp_w, temp_b

        # cost calculation
        cost = Jcost(X, Y, w, b)
        if iter > 10000:
            break
        
    return w, b, cost, iter

def generateDataSet(n = 50, trueCoeff = 1, noiseIntensity = 5):
    X = np.arange(n)
    Y = trueCoeff * X + noiseIntensity * np.random.randn(n)
    return X, Y

noiseIntensity = 6
n = 30
trueCoeff = 10
X, Y = generateDataSet(n, trueCoeff, noiseIntensity)

with open("testDataSet.txt", "w") as file:
    n = len(X)
    for i in range(n):
        file.write(f"{X[i]},{Y[i]}\n")

alpha = 0.005
w, b, cost, iter = gradientDescent(X, Y, alpha, n * noiseIntensity / 1000)
plt.title("linear regression")
plt.plot(X, Y, '.')
plt.plot(X, w*X + b)

plt.text(X.min(), Y.max(), f"Model: {w:.2f}x + ({b:.2f})\nMSE: {cost:.2f}\nRan for {iter} iterations.", verticalalignment='top')
plt.savefig("modelFit.jpg")