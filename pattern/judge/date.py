# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import re


def validate(item: str) -> float:
    result = [
        strategy(item) for strategy in [
            day_month_year,
            day_name_year,
            no_date,
        ]
    ]
    return max(result)


DATE_FACTOR = 5.0

MONTH = (r'(?P<month>Januar|Februar|März|April|Mai|Juni|Juli|'
         r'August|September|Oktober|November|Dezember)')


def day_month_year(item: str):
    pattern = r'(?P<day>\d{1,2})\.(?P<month>\d{1,2})\.(?P<year>\d{4})'
    matched = re.match(pattern, item)
    if matched:
        day = int(matched['day'])
        month = int(matched['month'])
        year = int(matched['year'])
        if not 1 <= day <= 31:
            return 0.0
        if not 1 <= month <= 12:
            return 0.0
        if not 0 <= year <= 2050:
            return 0.0
        return DATE_FACTOR
    return 0.0


def day_name_year(item: str):
    pattern = (r'(?P<day>\d{1,2})\.[ ]{0,1}'
               f'{MONTH}'
               r'[ ]{0,1}'
               r'(?P<year>\d{4})')
    matched = re.match(pattern, item)
    if matched:
        return DATE_FACTOR
    return 0.0


def no_date(item: str):
    if item != 'o.J.':
        return 0.0
    return DATE_FACTOR
