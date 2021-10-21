# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pattern.checker
import pattern.tok

STRATEGY = [
    (pattern.tok.Token.ABBREVIATION, pattern.checker.is_abbreviation),
    (pattern.tok.Token.DATE, pattern.checker.is_date),
    (pattern.tok.Token.PAGE, pattern.checker.is_number),
    (pattern.tok.Token.PERSON, pattern.checker.is_person),
    (pattern.tok.Token.SAME_SOURCE, pattern.checker.is_samesource),
    (pattern.tok.Token.URL, pattern.checker.is_url),
]


def split(line: str):
    comma = ',' in line
    result = []

    splitted = tokenize(line)
    for token in splitted:
        token = token.strip()
        result.append(analyze(token))

    if comma:
        items = []
        for item in result:
            items.append(item)
            items.append(pattern.tok.Token.COMMA)
        result = items[:-1]  # remove last comma token
    return result


def tokenize(line: str):
    if ',' in line:
        splitted = line.split(',')
    else:
        splitted = line.split()
    return splitted


def analyze(token: str) -> pattern.tok.Token:
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
