from typing import Union, Sequence

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    d = {1: stairway[0],
         2: stairway[1]}
    for step in range(2, len(stairway)):
        d[step + 1] = min(d[step],
                          d[step - 1]) + stairway[step]
    return d[len(stairway)]

