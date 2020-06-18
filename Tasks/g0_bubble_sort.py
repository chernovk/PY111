from typing import List
import operator


def sort(container: List[int], reverse=False) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    dc = {True: operator.lt,
          False: operator.gt}
    compare = dc[reverse]
    while True:
        sorting = False
        for i in range(len(container) - 1):
            if compare(container[i], container[i + 1]):
                sorting = True
                container[i], container[i + 1] = container[i + 1], container[i]
        if not sorting:
            break
    return container
