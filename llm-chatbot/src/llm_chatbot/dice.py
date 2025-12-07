import numpy as np


def roll_die():
    msg = "Roll a die"
    print(msg)
    print("Result:", np.random.randint(1, 6))
