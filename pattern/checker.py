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
import pattern.text.sentence


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


def is_samesource(item: str) -> float:
    return pattern.judge.abbreviation.same_source(item)


def is_sentence(item: str) -> float:
    splitted = pattern.text.sentence.split(item)
    if len(splitted) == 1:
        splitted = splitted[0]
        if pattern.text.sentence.is_closed(splitted):
            return 1.0
    return 0.0
