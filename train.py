#!/usr/local/bin/python3.6

import tensorflow as tf
from tensorflow.python import debug as tf_debug

import keras
from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, concatenate, Input, Flatten
from keras.callbacks import TensorBoard

import matplotlib.pyplot as plt

import load

def build_model(data_length, label_length):

    precipitation = Input(shape=(data_length, 1), name='precipitation')
    soilmoisture = Input(shape=(data_length, 1), name='soilmoisture')

    precipLayers = LSTM(64, return_sequences=False)(precipitation)
    soilmoLayer = LSTM(64, return_sequences=False)(soilmoisture)

    output = concatenate(
        [
            soilmoLayer,
            precipLayers,
        ]
    )

    output = Dense(label_length, activation='linear', name='weightedAverage_output')(output)

    model = Model(
        inputs=
        [
            soilmoisture,
            precipitation,
        ],
        outputs=
        [
            output
        ]
    )

    model.compile(optimizer='rmsprop', loss='mse')

    return model


if __name__ == '__main__':
    # keras.backend.set_session(tf_debug.TensorBoardDebugWrapperSession(tf.Session(), "127.0.0.1:6011"))

    # Load data
    _days = load.new()
    _data = _days.get_data(.64)

    _train = _data['train']
    _test = _data['test']


    tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=False)

    rnn = build_model( 3, 1 )
    fit = rnn.fit(
        _train['x'],
        # _train['y'],
        validation_data=(
            _test['x'],
            _test['y']
        ),
        epochs=5,
        batch_size=15,
        #        callbacks=[tensorboard]
    )

    _predicted = []
    _actual = []
    for i in range( 0, 31):
        _predict = rnn.predict([[_test['x'][0][i]], [_test['x'][1][i]]])
        _actual.append( _test['y'][0][i][0] )
        _predicted.append( _predict[0][0] )

    plt.plot(_predicted, '-y')
    plt.plot(_actual, '-r')
    plt.show()
