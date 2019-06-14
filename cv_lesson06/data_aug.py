import cv2
import os
import csv
import numpy as np

from keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img

def image_augmentation(imgs,save_dir):
    Datagen = ImageDataGenerator(rotation_range=30,  # 随机转动的角度
                                 shear_range=0.05,  # 剪切强度（逆时针方向的剪切变换角度）
                                 zoom_range=0.1,  # 随机缩放的幅度
                                 horizontal_flip=True,  # 进行随机水平翻转
                                 # vertical_flip=True,#进行随机竖直翻转
                                 width_shift_range=0.05,
                                 height_shift_range=0.05,
                                 fill_mode='nearest',
                                 )
                                 # 还有其他一些参数，具体请看：https://keras.io/preprocessing/image/ ，如去均值，标准化，ZCA白化，旋转，
                                 # 偏移，翻转，缩放等

    print(imgs.shape)
    length = len(imgs)
    print("length: ",length)
    print(type(imgs[0]))
    print(imgs[0].shape)

    i = 1
    for img_batch in Datagen.flow(imgs,
                                  batch_size=5,
                                  save_to_dir=save_dir,
                                  save_prefix='aug',
                                  save_format='jpg',
                                  # target_size=(256,256)
                                  ):
        i += 1
        if i > length:
            break

def get_imgs(flag):
    labels_filename = '/home/ubuntu/Downloads/CV_slides/lesson6/week6_CNN_Tiny_Project/src_data/Train/Label.TXT'
    img_dir = '/home/ubuntu/Downloads/CV_slides/lesson6/week6_CNN_Tiny_Project/src_data/Train/'
    with open(labels_filename, 'r') as labels:
        label = labels.readlines()
        imgs_path = [os.path.join(img_dir, i.split()[0]) for i in label if i.split()[1] == flag]
        imgs = np.array([img_to_array(load_img(img_path, target_size=(256, 256))) for img_path in imgs_path])
        # imgs = np.array([cv2.resize(cv2.imread(img_path), (256, 256)) for img_path in imgs_path]) # 有色差
        return imgs

# def save_labels():
#     save_dir = '/home/ubuntu/Downloads/CV_slides/lesson6/week6_CNN_Tiny_Project/src_data/aug_train/'
#     with open(save_dir + 'labels.csv', 'w') as csv_file:
#         csv_w = csv.writer(csv_file)
#         for i in range(3):
#             imgs_dir = save_dir + str(i)
#             imgs_i = os.listdir(imgs_dir)
#
#             for img_i in imgs_i:
#                 csv_w.writerows([img_i, i, imgs_dir + '/' + img_i])


if __name__ == "__main__":
    for i in range(3):
        imgs = get_imgs(str(i))
        save_dir = '/home/ubuntu/Downloads/CV_slides/lesson6/week6_CNN_Tiny_Project/src_data/aug_train/' + str(i)
        image_augmentation(imgs, save_dir)

    # save_labels()
