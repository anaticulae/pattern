# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila


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

DAY_MONTH_YEAR = utila.compiles(r"""
    (?P<day>\d{1,2})
    \.
    (?P<month>\d{1,2})
    \.
    (?P<year>(20[012]\d|1[789]\d\d))
""")


def day_month_year(item: str):
    """\
    >>> day_month_year('25.08.1987')
    5.0
    """
    matched = DAY_MONTH_YEAR.match(item)
    if not matched:
        return 0.0
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


DAY_NAME_YEAR = utila.compiles(r"""
    (?P<day>\d{1,2})\.[ ]{0,1}
    (?P<month>Januar|Februar|März|April|Mai|Juni|Juli|
              August|September|Oktober|November|Dezember
    )
    [ ]{0,1}
    (?P<year>(20[012]\d|1[789]\d\d))
""")


def day_name_year(item: str) -> float:
    """\
    >>> day_name_year('20. April 1999')
    5.0
    >>> day_name_year('01. Januar 1733')
    5.0
    """
    if DAY_NAME_YEAR.match(item):
        return DATE_FACTOR
    return 0.0


def no_date(item: str):
    if item != 'o.J.':
        return 0.0
    return DATE_FACTOR
