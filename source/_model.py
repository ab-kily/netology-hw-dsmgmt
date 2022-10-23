import keras

def make_model(TRAIN_X):
    hid_size = 256
    model = keras.Sequential(
        [
            keras.layers.InputLayer(input_shape=TRAIN_X.shape[-1]),
            keras.layers.Dense(hid_size, activation="relu"),
            keras.layers.Dropout(0.2),
            keras.layers.BatchNormalization(),
            keras.layers.Dense(hid_size, activation="relu"),
            keras.layers.Dropout(0.2),
            keras.layers.BatchNormalization(),
            keras.layers.Dense(hid_size, activation="relu"),
            keras.layers.Dropout(0.2),
            keras.layers.BatchNormalization(),
            keras.layers.Dense(1),
        ]
    )
    return model
