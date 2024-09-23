import numpy as np


def create_list():
    return list(range(1, 11))


def numpy_array(lst):
    return np.array(lst)


if __name__ == '__main__':
    print(numpy_array(create_list()))
