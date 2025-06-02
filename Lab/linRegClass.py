import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# linear regression using MSE cost function and gradient descent algorithm
class LinReg:
    def __init__(self, dataX=np.array([]), dataY=np.array([])):
        self.dataX = dataX
        self.dataY = dataY
        self.w = 0
        self.b = 0
    def reset(self):
        self.w = 0
        self.b = 0
    def model(self, x):
        return self.w*x + self.b
    def cost(self):
        return 1/(2*len(self.dataX)) * sum((self.model(self.dataX)-self.dataY)**2)
    def wDeri(self):
        return 1/len(self.dataX) * sum((self.model(self.dataX)-self.dataY) * self.dataX)
    def bDeri(self):
        return 1/len(self.dataX) * sum((self.model(self.dataX)-self.dataY))
    def train(self, alpha, iterations):
        costArr = []
        for _ in range(iterations):
            self.w, self.b = self.w - alpha*self.wDeri(), self.b - alpha*self.bDeri()
            costArr.append(self.cost())
        return costArr
    def chooseLearningRate(self, start, factor):
        alphaChoices = factor**np.arange(8) * start
        X = np.arange(10)
        fig, axes = plt.subplots(2, 4, figsize=(12, 6))
        fig.suptitle("no. of iterations vs cost", fontsize=16, y=1.05)
        axes = axes.flatten()
        for i, alpha in enumerate(alphaChoices):
            self.reset()
            costArr = self.train(alpha, 10)
            axes[i].plot(X, costArr, label=f'alpha = {alpha:.4f}')
            axes[i].legend()
        plt.tight_layout()
        plt.show()

n = 35
trueW, trueB = 0.7, 3
noiseLvl = 3
X, Y = [np.arange(n)] * 2
Y = trueW*X+trueB + noiseLvl*np.random.randn(n)
linRegModel = LinReg(X, Y)

linRegModel.chooseLearningRate(5e-5, 2) # 0.002 works
alpha = float(input("Enter learning rate: "))

linRegModel.train(alpha, 10000)
plt.plot(X, Y, 'r.', label='Training set')
plt.plot(X, trueW*X+trueB, 'g', label='True function')
plt.plot(X, linRegModel.w*X+linRegModel.b, 'black', label='Model')
plt.legend()
plt.show()

print(f"w: {linRegModel.w:.3f}")
print(f"b: {linRegModel.b:.3f}")
print(f"Cost: {linRegModel.cost()}")

fig, ax = plt.subplots()
plt.ylim(-0.1,1.1)
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')

def init():
    ax.scatter(X, Y, c='r', marker='x', label='Training set')
    return ln,

def update(frame):
    ax.cla()
    plt.ylim(min(Y)-1, max(Y)+1)
    linRegModel.reset()
    linRegModel.train(frame, 1000)
    ax.scatter(X, Y, c='r', marker='x', label='Training set')
    ax.plot(X, linRegModel.model(X), label='model')
    ax.plot(X, trueW*X+trueB, label='function')
    return ln,

ani = FuncAnimation(fig, update, frames=np.arange(alpha/10, alpha, alpha/10),
                    init_func=init, blit=True)
ani.save('linReg.gif')