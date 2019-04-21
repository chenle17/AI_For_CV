import math
import random
import numpy as np

def sigmoid_func(x, w, b):
    z = w * x + b
    sigm = 1 / (1 + math.e ** -z)
    return sigm

def cost_func(w, b, batch_x, batch_y):
    batch_size = len(batch_x)
    J1 = -1 / batch_size * (batch_y * np.log2(sigmoid_func(batch_x, w, b)))
    J2 = -1 / batch_size * (1- batch_y) * np.log2(1 - sigmoid_func(batch_x, w, b))
    J = (J1 + J2).sum()
    return J

def gradient(pred_y, batch_y, batch_x):
    batch_size = len(batch_x)
    diff = pred_y - batch_y
    dw = (diff * batch_x).sum() / batch_size
    db = diff.sum() / batch_size
    return dw, db

def cal_step_grediant(w, b, lr, batch_x, batch_y):
    pred_y = cost_func(w, b, batch_x, batch_y)
    dw, db = gradient(pred_y, batch_y, batch_x)
    w -= lr * dw
    b -= lr * db
    return w, b

def train(X, Y, batch_size, lr, max_iter):
    w, b = 0.001, 0.001
    for i in range(max_iter):
        batch_indx = np.random.choice(len(X), batch_size)
        batch_x = np.array([X[j] for j in batch_indx])
        batch_y = np.array([Y[j] for j in batch_indx])
        w, b = cal_step_grediant(w, b, lr, batch_x, batch_y)
        print('w:{0}, b:{1}'.format(w, b ))
        loss = cost_func(w, b, X, Y)
        print('loss is {0}'.format(loss))

        if loss < 0.1:
            print("第{0}次迭代，训练结束！".format(i))
            return

def gen_data():
    w = random.random() * 5
    b = random.random() * 2
    num_samples = 1000
    X = (np.random.rand(num_samples) - 0.5) * 100
    Y = sigmoid_func(X, w , b) + np.random.rand(num_samples) * 0.5 -0.25
    return X, Y

def run():
    lr = 0.0001
    max_iter = 10000
    batch_size = 100
    X, Y = gen_data()
    train(X, Y, batch_size, lr, max_iter)

if __name__ == '__main__':
    run()
