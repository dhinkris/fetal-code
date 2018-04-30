import tensorflow as tf

def Dice(binaryLabels, binaryOutputLayer):
    with tf.variable_scope('DiceCoefficient'):
        binaryLabelsSum = tf.reduce_sum(binaryLabels, axis=[1,2])
        binaryOutputSum = tf.reduce_sum(binaryOutputLayer, axis=[1,2])
        denom = tf.cast(binaryLabelsSum + binaryOutputSum, tf.float32)
        numer = tf.cast(2 * tf.reduce_sum(binaryOutputLayer * binaryLabels, axis=[1,2]), tf.float32)
        diceOp = tf.reduce_mean(tf.boolean_mask(numer / denom, tf.logical_not(tf.is_nan(numer / denom))))
    return diceOp