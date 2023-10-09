import numpy as np
import random

__all__ = ['rand_array', 'my_mat_solve', 'generate_random']


def rand_array(shape):
    return np.random.rand(*shape)


def my_mat_solve(A, b):
    return A.inv()*b

def generate_random():
    return random.random()