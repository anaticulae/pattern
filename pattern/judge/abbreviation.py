# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


def validate(item: str) -> float:
    item = item.lower()
    result = max((strategy(item) for strategy in (dictionary,)))
    return result


def dictionary(item):
    if item not in ABBREVIATION:
        return 0.0
    return 1.0


def same_source(item) -> float:
    if item in SAME_SOURCE:
        return 5.0
    return 0.0


ABBREVIATION = {
    'Aufl.',
    'Bd.',
    'Co.',
    'Diss.',
    'Dok.',
    'Forts.',
    'Hrsg.',
    'Jg.',
    'Sp.',
    'Verf.',
    'Verl.',
    'Vol.',
    'a.a.O.',
    'al.',
    'bzw.',
    'ebd.',
    'ebd.:',
    'et al',
    'etc.',
    'ff.'
    'ggf.',
    'lat.',
    'mind.',
    'o.A.',
    'o.J.',
    'o.V.',
    'o.Ä',
    's.',
    'usw.',
    'vgl.',
    'z.B.',
}

ABBREVIATION = {item.lower() for item in ABBREVIATION}

SAME_SOURCE = {
    'ebd.',
    'ebd.:',
}
