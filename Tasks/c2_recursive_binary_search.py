from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    def bin_2(lb, rb):
        mi = (lb + rb) // 2

        if arr[mi] == elem:
            if arr[mi - 1] != elem:
                return mi
        if lb >= rb:
            return None

        if elem > arr[rb]:
            return None
        if elem < arr[lb]:
            return None

        if arr[mi] > elem:
            rb = mi - 1
        else:
            lb = mi + 1

        return bin_2(lb, rb)

    left_border = 0
    right_border = len(arr) - 1

    return bin_2(left_border, right_border)





