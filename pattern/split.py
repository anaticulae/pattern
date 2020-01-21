# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import enum

import pattern.checker


class Token(enum.Enum):
    Abbreviation = enum.auto()
    Comma = enum.auto()
    Date = enum.auto()
    Person = enum.auto()
    URL = enum.auto()


STRATEGY = [
    (Token.Abbreviation, pattern.checker.is_abbreviation),
    (Token.Date, pattern.checker.is_date),
    (Token.Person, pattern.checker.is_person),
    (Token.URL, pattern.checker.is_url),
]


def split(line: str):
    splitted = line.split(',')
    result = []

    for token in splitted:
        token = token.strip()
        result.append(analyze(token))
        result.append(Token.Comma)
    result = result[:-1]  # remove last comma token
    return result


def analyze(token: str) -> Token:
    result = [strategy(token) for _, strategy in STRATEGY]
    index = max_index(result)
    return STRATEGY[index][0]


def max_index(items) -> int:
    result, value = 0, items[0]
    for index, item in enumerate(items[1:], start=1):
        if item <= value:
            continue
        value = item
        result = index
    return result
