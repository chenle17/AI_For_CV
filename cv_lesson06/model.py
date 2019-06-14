from keras.models import Model
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout,Input
from keras.layers import BatchNormalization,PReLU

def cnn():
    inputs = Input(shape=(256, 256, 3), name='inputs')
    # conv_1 = Conv2D(16, (7, 7), padding='same', name='conv_1', activation='relu')(inputs)
    # pooling_1 = MaxPooling2D((4, 4), strides=(2, 2), name='pool_1')(conv_1)
    # # drop_1 = Dropout(0.5)(pooling_1)
    # conv_2 = Conv2D(32, (7, 7), padding='same', name='conv_2', activation='relu')(pooling_1)
    # pooling_2 = MaxPooling2D((4, 4), strides=(2, 2), name='pool_2')(conv_2)
    # # drop_2 = Dropout(0.5)(pooling_2)
    # conv_3 = Conv2D(64, (7, 7), padding='same', name='conv_3', activation='relu')(pooling_2)
    # pooling_3 = MaxPooling2D((4, 4), strides=(2, 2), name='pool_3')(conv_3)

    conv_1 = Conv2D(32, (5, 5), padding='same', name='conv_1')(inputs)
    bn_1 = BatchNormalization()(conv_1)
    pr_1 = PReLU()(bn_1)
    conv_2 = Conv2D(32, (5, 5), padding='same', name='conv_2')(pr_1)
    bn_2 = BatchNormalization()(conv_2)
    pr_2 = PReLU()(bn_2)
    pooling_2 = MaxPooling2D((2, 2), strides=(2, 2), name='pool_2')(pr_2)
    conv_3 = Conv2D(64, (5, 5), padding='same', name='conv_3')(pooling_2)
    bn_3 = BatchNormalization()(conv_3)
    pr_3 = PReLU()(bn_3)
    pooling_3 = MaxPooling2D((2, 2), strides=(2, 2), name='pool_3')(pr_3)

    conv_4 = Conv2D(128, (3, 3), padding='same', name='conv_4')(pooling_3)
    bn_4 = BatchNormalization()(conv_4)
    pr_4 = PReLU()(bn_4)
    pooling_4 = MaxPooling2D((2, 2), strides=(2, 2), name='pool_4')(pr_4)
    fl = Flatten(name='flatten')(pooling_4)
    fc_1 = Dense(256, name='fc_1')(fl)
    bn_5 = BatchNormalization()(fc_1)
    pr_5 = PReLU()(bn_5)
    # dro_1 = Dropout(0.5)(fc_1)
    fc_2 = Dense(64, name='fc_2')(pr_5)
    bn_6 = BatchNormalization()(fc_2)
    pr_6 = PReLU()(bn_6)
    # dro_2 = Dropout(0.5)(fc_2)
    out = Dense(3, activation='sigmoid', name='out')(pr_6)

    model = Model(inputs=inputs, outputs=out)
    return model
