from keras.models import Model
from keras.models import Sequential
from keras.layers import Dense, Activation, LSTM, concatenate, Input
from keras.callbacks import TensorBoard


def build_model(data_length, label_length):

    precipitation = Input(shape=(data_length, 1), name='precipitation')
    soilmoisture = Input(shape=(data_length, 1), name='soilmoisture')

    precipLayers = LSTM(64, return_sequences=False)(precipitation)
    soilmoLayer = LSTM(64, return_sequences=False)(soilmoisture)

    output = concatenate(
        [
            precipLayers,
            soilmoLayer,
        ]
    )

    output = Dense(label_length, activation='linear', name='weighted_average_output')(output)

    model = Model(
        inputs=
        [
            precipitation,
            soilmoisture,
        ],
        outputs=
        [
            output
        ]
    )

    model.compile(optimizer='rmsprop', loss='mse')

    return model


if __name__ == '__main__':

    training_data, training_labels, testing_data, testing_labels = loader.loadObjectFromPickle(PATH)
    tbCallBack = TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)

    rnn = build_model(3650, 3)

    rnn.fit(
        [
            training_data["precipitation"],
            training_data["soilmoisture"],
        ],
        [
            training_labels["soilmoisture"]
        ],
        validation_data=(
            [
                testing_data["precipitation"],
                testing_data["soilmoisture"],
            ],
            [
                testing_labels["soilmoisture"]
            ]),
        epochs=1,
        batch_size=3000,
        callbacks=[
            tbCallBack
        ]
    )
