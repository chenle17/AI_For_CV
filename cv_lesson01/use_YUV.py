import cv2 as cv
import numpy as np
import math
import random

def random_change_color(img):
    #random changing angle of the image hue
    sita = random.randint(-180,180)
    img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    shape = img_yuv.shape
    #####change image hue
    #1----U
    img_yuv[:,:int(shape[1]/2),1] = \
        math.cos(math.radians(sita)) * img_yuv[:,:int(shape[1]/2),1] + \
        math.sin(math.radians(sita)) * img_yuv[:,:int(shape[1]/2),1]
    #2----V
    img_yuv[:,:int(shape[1]/2),2] = \
        math.cos(math.radians(sita)) * img_yuv[:,:int(shape[1]/2),2] - \
        math.sin(math.radians(sita)) * img_yuv[:,:int(shape[1]/2),2]
    img_yuv = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)

    cv.imshow('img_yuv', img_yuv)
    esc()

def esc():
    key = cv.waitKey()
    if key == 27:
        cv.destroyAllWindows()


filename = '/home/ubuntu/Downloads/Learn_CV/cv_lesson01/img/ThereIsSomethingAboutMary_013959520_00000036.png'
img = cv.imread(filename)
random_change_color(img)

