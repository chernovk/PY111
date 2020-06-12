import numpy as np


def calculate_paths(shape: (int, int), point: (int, int)) -> int:
    """
    Given field with size rows*cols count available paths from (0, 0) to point

    :param shape: tuple of rows and cols (each from 1 to rows/cols)
    :param point: desired point for horse
    :return: count of paths from (1, 1) to (point[0], point[1]) (numerating from 0, so (0, 0) - left bottom tile)
    """
    ar = np.zeros(shape, dtype=np.int32)
    ar[0, 0] = 1

    for i in range(ar.shape[0]):
        for j in range(ar.shape[1]):
            if j - 1 >= 0 and i - 2 >= 0:
                ar[i, j] += 2 * ar[i - 2, j - 1]
            if j + 1 < ar.shape[1] and i - 2 >= 0:
                ar[i, j] += 2 * ar[i - 2, j + 1]
            if j - 2 >= 0 and i - 1 >= 0:
                ar[i, j] += 2 * ar[i - 1, j - 2]
            if j + 2 < ar.shape[1] and i - 1 >= 0:
                ar[i, j] += 2 * ar[i - 1, j + 2]
    return ar[point[0], point[1]]

