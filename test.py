import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import FuncAnimation

class LinearRegression:
    def __init__(self, dataX, dataY):
        self.dataX = dataX
        self.dataY = dataY
        self.w, self.b = 0, 0
    
    def reset(self):
        self.w, self.b = 0, 0

    def model(self, x):
        return self.w*x + self.b
    
    def cost(self):
        return 1/(2*len(self.dataX)) * sum((self.model(self.dataX)-self.dataY)**2)

    def train(self, alpha, iterations):
        costArr = []
        for _ in range(iterations):
            wDer = 1/len(self.dataX) * sum((self.model(self.dataX)-self.dataY)*self.dataX)
            bDer = 1/len(self.dataX) * sum(self.model(self.dataX)-self.dataY)
            self.w, self.b = self.w-alpha*wDer, self.b-alpha*bDer
            costArr.append(self.cost())
        return costArr
    
    def chooseAlpha(self, start, factor):
        alphaChoices = start * np.arange(1,9) * factor
        fig, axes = plt.subplots(2, 4, figsize=(3*4, 3*2)) # size * no.
        x = np.arange(1,11)
        axes = axes.flatten()
        for i in range(len(alphaChoices)):
            self.reset()
            axes[i].plot(x, self.train(alphaChoices[i], 10), label=f'{alphaChoices[i]}')
            axes[i].legend()
        self.reset()
        plt.tight_layout()
        plt.show()

n = 35
trueW, trueB = 1.2, 3
noiseLvl = 5
dataX = np.arange(n)
dataY = trueW*np.arange(n)+trueB + noiseLvl*np.random.randn(n)
a = LinearRegression(dataX, dataY)
a.chooseAlpha(3e-4,3)
    
alpha = float(input("Alpha: "))
a.train(alpha, 10000)
plt.scatter(dataX, dataY, c='r', label='training set')
plt.plot(dataX, trueW*dataX+trueB, label='inspiration')
plt.plot(dataX, a.model(dataX), label='model')
plt.legend()
plt.show()