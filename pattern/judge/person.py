# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


def validate(item: str) -> float:
    result = max((strategy(item) for strategy in (dictionary,)))
    return result


def dictionary(item):
    splitted = item.split(' ')
    for name in splitted:
        if all([
                name not in SURNAME,
                name not in NAME,
                name != 'von',
        ]):
            return 0.0
    # prefere person over abbreviation
    return 5.0


# TODO: LOAD FROM FILE

SURNAME = {
    'Angela',
    'Frank',
    'Gero',
    'Martin',
}

NAME = {
    'Gatterburg',
    'Hornig',
    'Randow',
    'Simons',
    'o.A.',
}
