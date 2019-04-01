import cv2 as cv
import numpy as np
import random as rd
from matplotlib import pyplot as plt

def esc():
    key = cv.waitKey()
    if key == 27:
        cv.destroyAllWindows()

'''
show gray image/image.dtype/image.shape
'''
def showImgInfo(filename,flags=1):
    # 0:gray img, 1: BGR img,
    img = cv.imread(filename,flags)
    print('img_matrix: ', img)
    print('img_shape: ', img.shape)
    print('imgt_dtype: ', img.dtype)
    return img

filename = "/home/ubuntu/Downloads/Learn_CV/CV_lesson01_Assignments/img/0_0.jpg"
img_gray = showImgInfo(filename,0)
cv.imshow('HarryPoter_gray',img_gray)
img = showImgInfo(filename)
cv.imshow('HarryPoter',img)
esc()


# img crop
img_crop = img[:100,:100]
cv.imshow('img_crop',img_crop)
esc()

# img split
B, G, R = cv.split(img)
cv.imshow('B', B)
cv.imshow('G', G)
cv.imshow('R', R)
esc()

'''change color'''
def random_light_color(img):
    B, G, R = cv.split(img)

    b_rand = rd.randint(-50, 50)
    if b_rand == 0:
        pass
    elif b_rand > 0:
        lim = 255 - b_rand
        B[B <= lim] = (B[B <= lim] + b_rand).astype(img.dtype)
        B[B > lim] = 255
    else:
        lim = 0 - b_rand
        B[B >= lim] = (B[B >= lim] + b_rand).astype(img.dtype)
        B[B < lim] = 0
    
    g_rand = rd.randint(-50, -50)
    if g_rand == 0:
        pass
    elif g_rand > 0:
        lim = 255 - g_rand
        G[G <= lim] = (G[G <= lim] + g_rand).astype(img.dtype)
        G[G > lim] = 255
    else:
        lim = 0 - g_rand
        G[G >= lim] = (G[G >= lim] + g_rand).astype(img.dtype)
        G[G < lim] = 0

    r_rand = rd.randint(-50, -50)
    if r_rand == 0:
        pass
    elif r_rand > 0:
        lim = 255 - r_rand
        R[R <= lim] = (R[R <= lim] + r_rand).astype(img.dtype)
        R[R > lim] = 255
    else:
        lim = 0 - r_rand
        R[R >= lim] = (R[R >= lim] + r_rand).astype(img.dtype)
        R[R < lim] = 0

    img_merge = cv.merge((B, G, R))
    return img_merge

img_random_color = random_light_color(img)
cv.imshow('img_random_color', img_random_color)
esc()

'''gamma correction'''
cv.imshow("ori_img", img)
def adjust_gamma(img,gamma=1.0):
    invGamma = 1.0/gamma
    table = []# 映射
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype('uint8')
    return cv.LUT(img,table)
img_brighter = adjust_gamma(img, 2)
cv.imshow("adjust_gamma_img", img_brighter)
esc()

'''histogram'''
def histogram_equalized(img):
    print("img.shape: ",img.shape)
    # Plot a histogram
    # plt.hist(img.flatten(), 256, [0,256], color='r')
    # y: luminance(明亮度), u&v: 色度饱和度
    img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    print("img_yuv.shape: ", img_yuv.shape)
    # 直方图均衡化
    img_yuv[:,:,0] = cv.equalizeHist(img_yuv[:,:,0])
    return cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
cv.imshow("img",img_brighter)
cv.imshow("Histogram equalized", histogram_equalized(img_brighter))
esc()

'''Rotation旋转'''
rotation_mat = cv.getRotationMatrix2D((img.shape[1]/2, img.shape[0]/2), 30, 1)# center, angle, scale
img_rotate = cv.warpAffine(img, rotation_mat, (img.shape[1], img.shape[0]))
cv.imshow('rotaed Harry', img_rotate)
# esc()
print("rotation_mat: ", rotation_mat)
##旋转，平移
# rotation_mat:  [[  0.8660254    0.5        -40.99484522]
#  [ -0.5          0.8660254   71.00515478]]
rotation_mat[0][2] = rotation_mat[1][2] = 0

img_rotate2 = cv.warpAffine(img, rotation_mat, (img.shape[1],img.shape[0]))
cv.imshow('rotaed Harry2', img_rotate2)
esc()

'''scale + rolation + translation = similarity transform相似变换'''
cv.getRotaitonMatrix2D((img.shape[1]/2, img.shape[0]/2), 30, 0.5)
img_rotate = cv.warpAffine(img, rotation_mat, (img.shape[1], img.shape[0]))
cv.imshow('rotaed Harry', img_rotate)
esc()

'''Affine Transform仿射变换'''
rows, cols, ch = img.shape
pts1 = np.float32([[0, 0], [cols-1, 0], [0, rows-1]])#3 Src Point
pts2 = np.float32([[cols*0.2, rows*0.1], [cols*0.9, rows*0.2], [cols*0.1, rows*0.9]])#3 Dst Points
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img, M, (cols, rows))

cv.imshow('Affine Harry', dst)
esc()

'''perspective transform 投影（透视）变换'''
def random_warp(img, row, col):
    height, width, channels = img.shape

    #warp:
    random_margin = 60
    x1 = rd.randint(-random_margin, random_margin)
    y1 = rd.randint(-random_margin, random_margin)

    x2 = rd.randint(width-random_margin-1, width-1)
    y2 = rd.randint(-random_margin, random_margin)

    x3 = rd.randint(width-random_margin-1, width-1)
    y3 = rd.randint(height-random_margin-1, height-1)

    x4 = rd.randint(-random_margin, random_margin)
    y4 = rd.randint(height-random_margin-1, height-1)




