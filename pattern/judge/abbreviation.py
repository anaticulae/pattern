# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


def validate(item: str) -> float:
    result = max([strategy(item) for strategy in [
        dictionary,
    ]])
    return result


def dictionary(item):
    if item not in ABBREVIATION:
        return 0.0
    return 1.0


ABBREVIATION = {
    'ebd.',
    'o.A.',
    'o.J.',
    'vgl.',
}
