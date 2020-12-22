import tensorflow as tf
import numpy as np
from tensorflow import keras

# simplest possible neural network
# one layer
# that layer has one neuron
# the input shape to it is only one value
model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# loss function measures the distance of the guess from the real answer
# optimizer gives a function to optimize the guess for the next run
# sgd = stochastic gradient descent
model.compile(optimizer='sgd', loss='mean_squared_error')

# feed in the data based on our rule function Y=3X+1
# use numpy for easier declaration
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# train the model for a selected number of epochs
# to rund through loss and optimkizer
model.fit(xs, ys, epochs=500)
