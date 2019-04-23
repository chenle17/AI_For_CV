import numpy as np

<<<<<<< HEAD
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

=======
def get_angle(v, V, S, T):
    '''

    :param v: 人的速度
    :param V: 河水速度的数组
    :param S: 河水宽的数组
    :param T: 限定时间
    :return: a，过每条河时的角度
    '''
    a = np.zeros(S.shape)

    # a[S - T * v == 0] = 0  # 0度角到对岸刚好T时间
    # 0度角也到达不了对岸时：
    a[S - T * v  > 0] = None
    # T时间到达对岸，游泳的角度：
    a[S - T * v < 0] = np.arccos(S / (T * v))
>>>>>>> bfc60d13520840a21e3fb0a79187199f91480928
    return a