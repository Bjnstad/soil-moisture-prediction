#!/usr/local/bin/python3.6

from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, concatenate, Input, Flatten
from keras.callbacks import TensorBoard

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

    _days = load.new()

    tensorboard = TensorBoard(log_dir='./logs', histogram_freq=0, write_graph=True, write_images=False)

    rnn = build_model( len(_days.get_date()), 1 )

    rnn.fit(
        [
            _days.get_moist_2(),
            _days.get_precip()
        ],
        [
            _days.get_moist_2_labels()
        ],
        validation_data=(
            [
                _days.get_moist_2(),
                _days.get_precip()
            ],
            [
                _days.get_moist_2_labels() 
            ]
        ),
        epochs=20,
        batch_size=32,
        callbacks=[tensorboard]
    )
