import random

with open("file.txt", "r") as tf:
    lines = tf.read().split(',')

def proxyRandom():
    return random.choice(lines)