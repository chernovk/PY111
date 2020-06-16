from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    while True:
        sorting = False
        for i in range(len(container) - 1):
            if container[i] > container[i + 1]:
                sorting = True
                container[i], container[i + 1] = container[i + 1], container[i]
        if not sorting:
            break
    return container
