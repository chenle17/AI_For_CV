import numpy as np

def get_max_angle(v, V, S, T):
    '''

    :param v: 人的速度
    :param V: 河的速度的数组 ndarray
    :param S: 河宽距离的数组 ndarray
    :param T: 限定过河时间
    :return: a, ndarray, 过河的角度
    '''
    a = np.zeros(S.shape)
    # 水平过河刚好到岸边，角度a为0
    a[S - T * v == 0] = 0
    # 水平过河距离超过河宽S
    a[S - T * v < 0] = np.arccos(S[S - T * v > 0] / (T * V[S - T * v > 0]))
    # 水平过河游不到河对岸
    a[S - T * v > 0] = None

    return a