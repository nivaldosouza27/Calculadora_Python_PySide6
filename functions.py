import re

NUM_OR_DOR_REGEX = re.compile(r'^[0-9.]$')


def isNumOrDot(string: str):
    return bool(NUM_OR_DOR_REGEX.search(string))


def isEmpty(string: str):
    return len(string) == 0
