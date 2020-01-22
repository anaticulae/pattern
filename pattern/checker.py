# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pattern.judge.abbreviation
import pattern.judge.date
import pattern.judge.number
import pattern.judge.person
import pattern.judge.url


def is_date(item: str) -> float:
    return pattern.judge.date.validate(item)


def is_url(item: str) -> float:
    return pattern.judge.url.validate(item)


def is_person(item: str) -> float:
    return pattern.judge.person.validate(item)


def is_abbreviation(item: str) -> float:
    return pattern.judge.abbreviation.validate(item)


def is_number(item: str) -> float:
    return pattern.judge.number.validate(item)
