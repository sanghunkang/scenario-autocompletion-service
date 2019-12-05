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