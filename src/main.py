import keras
from keras import layers

model = keras.Sequential([
    layers.Dense(units=1, input_shape=[3])
]);
