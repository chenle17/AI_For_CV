import random
import numpy as np

def inference(w, b , x):
    pred_y = w * x + b
    return pred_y

def eval_loss(w, b, X, Y):
    batch_size = len(X)
    avg_loss = 0.5 / batch_size * (inference(w, b , X) - Y) ** 2
    avg_loss = avg_loss.sum()
    return avg_loss

def gredient(pred_y, gy_y, x):
    diff = pred_y - gy_y
    dw = diff * x
    db = diff
    return dw, db

def cal_step_gradient(batch_x, batch_gt_y, w, b ,lr):
    batch_size = len(batch_x)

    batch_pred_y = inference(w, b, batch_x)
    batch_dw, batch_db = gredient(batch_pred_y, batch_gt_y, batch_x)
    avg_dw = batch_dw.sum() / batch_size
    avg_db = batch_db.sum() / batch_size
    w -= lr * avg_dw
    b -= lr * avg_db

    return w, b

def train(X, Y, batch_size, lr, max_iter):

    w = 0
    b = 0
    for i in range(max_iter):
        batch_idxs = np.random.choice(len(X), batch_size)
        batch_x = np.array([X[j] for j in batch_idxs])
        batch_y = np.array([Y[j] for j in batch_idxs])
        w, b = cal_step_gradient(batch_x, batch_y, w, b, lr)
        print('w:{0}, b:{1}'.format(w, b))
        print('loss is {}'.format(eval_loss(w, b, X, Y)))

def gen_sample_data():
    w = random.randint(0, 10) + random.random()
    b = random.randint(0, 5) + random.random()
    num_samples = 200
    X = np.random.rand(num_samples) * 100
    Y = w * X + b + np.random.randint(-1, 1, X.shape)

    return X, Y, w, b

def run():
    X, Y, w, b = gen_sample_data()
    lr = 0.0001
    max_iter = 1000
    batch_size = 50
    train(X, Y, batch_size, lr, max_iter)

if __name__ == '__main__':
    run()