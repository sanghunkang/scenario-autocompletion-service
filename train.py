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
embedding = tf.EmbeddingLookup(X) # Where to store embedding? Is it necessary?
layer1 = tf.LSTM(embedding) # Non linearity?
layer2 = tf.LSTM(layer1) # Non linearity?
z = tf.FullyConnected(layer2) # ...which is the weighted(weight trained during traintime) sum
pred = tf.logit(z)

# Step2-2: Calculate cost
optimizer = tf.keras.optimizers.Adam()
loss_object = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True, reduction='none')
mask = tf.math.logical_not(tf.math.equal(real, 0))
loss_ = loss_object(real, pred)

mask = tf.cast(mask, dtype=loss_.dtype)
loss_ *= mask

tf.reduce_mean(loss_)

# Step2-3: Run Traing


# Step3: Save model somewhere