import os
import cv2
import numpy as np

from keras.utils import np_utils

def load_train_data():
    imgs_dir = r'/home/ubuntu/Downloads/CV_slides/lesson6/week6_CNN_Tiny_Project/src_data/aug_train/'
    imgs = []
    labels = []
    for i in range(3):
        sub_imgs_dir = imgs_dir + str(i) + '/'
        sub_imgs = load_imgs(sub_imgs_dir)
        imgs.extend(sub_imgs)

        sub_labels = [i for _ in sub_imgs]
        labels.extend(sub_labels)

    return data_shuffle(imgs, labels)

def load_test_data():
    imgs_dir = r'/home/ubuntu/Downloads/CV_slides/lesson6/week6_CNN_Tiny_Project/src_data/Test/'
    imgs = []
    labels = []
    with open(imgs_dir + 'Label.txt', 'r') as txt_file:
        labels_info = txt_file.readlines()
        for label_info in labels_info:
            img_name, label, label_ = label_info.split()
            img = read_gray(imgs_dir + img_name)
            imgs.append(img)
            labels.append(label)

    imgs = np.array(imgs)
    labels = np.array(labels)
    return imgs, labels


def data_shuffle(imgs, labels):
    imgs = np.array(imgs)
    labels = np.array(labels)

    shuffle_index = np.arange(imgs.shape[0])
    np.random.shuffle(shuffle_index)
    imgs = imgs[shuffle_index, ...]
    labels = labels[shuffle_index, ...]
    labels = np_utils.to_categorical(labels, 3)
    return imgs, labels

def load_imgs(imgs_dir):
    imgs_name = os.listdir(imgs_dir)
    imgs = [read_gray(imgs_dir + img_name) for img_name in imgs_name]
    return imgs


def read_gray(img_name):
    img = cv2.resize(cv2.imread(img_name, 0), (256, 256))
    img = img[..., np.newaxis]
    img = np.tile(img, (3))
    return img

