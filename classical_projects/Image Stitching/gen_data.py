from cv_lesson01 import data_augmentation

def img_similarity_tansform():
    data_augmentation.img_augmentation(crop=0.,
                                       color_shift=0,
                                       rotation=10,
                                       random_margin=0,
                                       aug_size=5)

if __name__ == '__main__':
    img_similarity_tansform()