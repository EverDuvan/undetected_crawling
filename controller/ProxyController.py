import random

def get_proxy_random():
    with open("file.txt", "r") as tf:
        lines = tf.read().split(',')
        lines = random.choice(lines)
        return lines

