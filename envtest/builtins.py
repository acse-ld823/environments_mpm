import numpy as np


__all__ = ['rand_array', 'my_mat_solve']


def rand_array(shape):
    return np.random.rand(*shape)


def my_mat_solve(A, b):
    return A.inv()*b