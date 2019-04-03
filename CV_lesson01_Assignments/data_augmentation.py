import argparse
import os
import cv2 as cv
import numpy as np
import random as rd


def img_augmentation(crop,color_shift,rotation,random_margin,aug_size):
    '''
    image augmentation combine image crop, color shift, rotation and perspective transform

    :param crop: float, [0,1)
    :param color_shift: int, [0,255]
    :param rotation: int, [-180,180]
    :param random_margin: int
    :param aug_size: int, >0
    :return:None
    '''
    img_dir = "/home/ubuntu/Downloads/Learn_CV/CV_lesson01_Assignments/img"
    img_save = "/home/ubuntu/Downloads/Learn_CV/CV_lesson01_Assignments/img_aug"
    imgs = os.listdir(img_dir)
    # imgs = [os.path.join(img_dir, img) for img in imgs]
    for img_name in imgs:
        file_name = os.path.join(img_dir, img_name)
        img_name = img_name.split('.')[0]
        img = cv.imread(file_name)
        img_shape = img.shape
        for i in range(aug_size):
            #crop
            crop_x = rd.uniform(0, crop)
            x = int(img_shape[1]*crop_x)
            crop_y = rd.uniform(0, crop)
            y = int(img_shape[0]*crop_y)
            img_crop = img[y//2:img_shape[0]-y//2, x//2:img_shape[1]-x//2]

            #color_shift
            B, G, R = cv.split(img_crop)
            b_rand = rd.randint(-color_shift, color_shift)
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

            #rotation
            ro_range = rd.randint(-rotation, rotation)
            rotation_mat = cv.getRotationMatrix2D((img_merge.shape[1] / 2, img_merge.shape[0] / 2), ro_range, 1)  # center, angle, scale
            img_rotate = cv.warpAffine(img_merge, rotation_mat, (img_merge.shape[1], img_merge.shape[0]))

            #perspective
            height, width, channels = img_rotate.shape

            x1 = rd.randint(-random_margin, random_margin)
            y1 = rd.randint(-random_margin, random_margin)
            x2 = rd.randint(width - random_margin - 1, width - 1)
            y2 = rd.randint(-random_margin, random_margin)
            x3 = rd.randint(width - random_margin - 1, width - 1)
            y3 = rd.randint(height - random_margin - 1, height - 1)
            x4 = rd.randint(-random_margin, random_margin)
            y4 = rd.randint(height - random_margin - 1, height - 1)

            dx1 = rd.randint(-random_margin, random_margin)
            dy1 = rd.randint(-random_margin, random_margin)
            dx2 = rd.randint(width - random_margin - 1, width - 1)
            dy2 = rd.randint(-random_margin, random_margin)
            dx3 = rd.randint(width - random_margin - 1, width - 1)
            dy3 = rd.randint(height - random_margin - 1, height - 1)
            dx4 = rd.randint(-random_margin, random_margin)
            dy4 = rd.randint(height - random_margin - 1, height - 1)

            pts1 = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
            pts2 = np.float32([[dx1, dy1], [dx2, dy2], [dx3, dy3], [dx4, dy4]])
            M_warp = cv.getPerspectiveTransform(pts1, pts2)
            img_warp = cv.warpPerspective(img_rotate, M_warp, (width, height))

            cv.imwrite(img_save + "/" + img_name + ("_%03d.jpg" % i), img_warp)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--crop', type=float,default=0.15, help='crop range: [0,1)')
    parser.add_argument('--color_shift', type=int,default=15, help='random light color : [0,255]')
    parser.add_argument('--rotation', type=int, default=15, help='rotation angle')
    parser.add_argument('--random_margin', type=int, default=15, help='random margin')
    parser.add_argument('--aug_size', type=int, default=3, help='number of augmentation')

    args = parser.parse_args()
    print(args)

    img_augmentation(args.crop,args.color_shift,args.rotation,args.random_margin,args.aug_size)

