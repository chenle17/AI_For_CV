import numpy as np

def get_angle(v, S, T):
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

    return a