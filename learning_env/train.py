from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import numpy as np
import matplotlib.pyplot as plt

import neural_structured_learning as nsl

import tensorflow as tf
tf.compat.v1.enable_v2_behavior()

import tensorflow_hub as hub

# Resets notebook state
tf.keras.backend.clear_session()

print("Version: ", tf.__version__)
print("Eager mode: ", tf.executing_eagerly())
print("Hub version: ", hub.__version__)
print("GPU is", "available" if tf.test.is_gpu_available() else "NOT AVAILABLE")

# Step1: Load data
# connect to database or whatever storage


# preprocess into datatype to feed into tensorflow
    # 

# Step2: Build Computation model
# Step2-0: Prepare data
X, y # sampled, sliced(?) set of records, last token(?) being y

# Step2-1: Model Architecture a seq2seq model
 # Where to store embedding? Is it necessary?
def lookup(X):
    X = tf.EmbeddingLookup(X)
    return X

def stacked_encoder(X, w0, b0, w1, b1, w2, b2):
    X = tf.LSTM(X)      # encoder layer 1
    X = tf.LSTM(X)      # encoder layer 2
    return X

z = tf.FullyConnected(layer2) # ...which is the weighted(weight trained during traintime) sum
pred = tf.logit(z)

@tf.function
def forward_path(X):
    X = lookup(X)
    X = stacked_encoder(X)


# Step2-2: Calculate cost
optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction='none')
mask = tf.math.logical_not(tf.math.equal(real, 0))
loss_ = loss_object(real, pred)

mask = tf.cast(mask, dtype=loss_.dtype)
loss_ *= mask

tf.reduce_mean(loss_)

# Step2-3: Run Traing
c = lambda i: tf.less(i, 10)
b = lambda i: tf.add(i, 1)
r = tf.while_loop(c, b, [i])

# Step3: Save model somewhere