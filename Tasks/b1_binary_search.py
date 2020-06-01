from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    if elem < arr[0]:
        return None
    if elem > arr[-1]:
        return None

    left_border = 0
    right_border = len(arr) - 1
    while True:
        middle = (right_border + left_border) // 2

        if arr[middle] == elem:
            return middle

        if left_border == right_border:
            return None

        if arr[middle] < elem:
            left_border = middle + 1
        elif arr[middle] > elem:
            right_border = middle - 1







