def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    l = []
    for i in brackets_row:
        if i == '(':
            l.append(1)
        else:
            try:
                l.pop()
            except IndexError:
                return False
    return False if 1 in l else True
