import random

with open("file.txt", "r") as tf:
    lines = tf.read().split(',')

def get_proxy_random():
    return random.choice(lines)