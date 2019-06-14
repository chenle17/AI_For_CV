from cv_lesson06.model import cnn
from cv_lesson06.load_data import load_train_data, load_test_data

import keras
from keras import optimizers,metrics
from keras.callbacks import EarlyStopping,ModelCheckpoint

from keras.utils import plot_model

class LossHistory(keras.callbacks.Callback):
    def on_train_begin(self, logs={}):
        self.losses = []
        self.accuracy = []
        self.epochs = []
    def on_epoch_end(self, epoch, logs={}):
        self.losses.append(logs.get('loss'))
        self.accuracy.append(logs.get('categorical_accuracy'))
        self.epochs.append(logs.get('epochs'))

def train_cnn():
    model = cnn()

    adam = optimizers.Adam(lr=0.0001)
    history = LossHistory()
    stopping = EarlyStopping(monitor='loss', patience=3, mode='min')
    CNN_LOGS = '/home/ubuntu/Downloads/Learn_CV/cv_lesson06/logs/'
    tbCallBack_c = keras.callbacks.TensorBoard(log_dir=CNN_LOGS, write_graph=True, write_images=1)
    weights_path = '/home/ubuntu/Downloads/Learn_CV/cv_lesson06/models/'
    mc = ModelCheckpoint(weights_path + 'weight-{epoch:002d}.h5', period=3)

    model.compile(loss='categorical_crossentropy',
                  optimizer=adam,
                  metrics=[metrics.mae,metrics.categorical_accuracy])

    X, Y = load_train_data()
    try:
        model.fit(X, Y,
              batch_size=64,
              epochs=100,
              shuffle=True,
              # verbose=1,
              # validation_split=0.2,
              callbacks=[history, stopping, tbCallBack_c, mc])
    except:
        # record_loss_accuracy(history)
        model.save_weights(weights_path + 'except_weights.h5')
        plot_model(model, to_file="except_mode.png", show_shapes=True)
        return

    model.save_weights(weights_path + 'best_weights.h5')
    plot_model(model, to_file="best_mode.png", show_shapes=True)

def predict_cnn():
    model = cnn()
    model.load_weights('/home/ubuntu/Downloads/Learn_CV/cv_lesson06/models/best_weights.h5', by_name=True)

    X, Y = load_test_data()
    predicts = model.predict(X)
    print('Y:', Y)
    print('predicts', predicts)
    print('-------end!')

if __name__ == '__main__':
    print("--------start train!---------")
    train_cnn()

    print("--------start test!--------")
    predict_cnn()