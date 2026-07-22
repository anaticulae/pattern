# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import germania
import utilo

import pattern

RAW = """Bill Nitzberg und Virginia Lo. Distributed Shared Memory: A
Survey of Issue and Algorithms. In: Computer 24.8 (Aug. 1991), S. 52-60.
issn: 0018-9162. doi: 10. 1109/2.84877. url:
http://dx.doi.org/10.1109/2.84877.
"""

URL = 'URL:'
IN = r'IN:[^\*]+'

PATTERN = (
    germania.issn,
    germania.isbn,
    germania.doi,
    germania.pagenumbers,
    germania.hyperlink,
    germania.dates_master,
    URL,
    pattern.SimpleCleanup,
    pattern.Regex(regex=IN, name='in-pattern'),
    pattern.SimpleCleanup,
)

IMPROVES = (germania.href_magic,)


def test_machine_simple():
    matched = pattern.match(
        RAW,
        patterns=PATTERN,
        improves=IMPROVES,
    )
    replaced = matched['replaced']
    assert 'url' not in replaced
    assert replaced.count('*') >= 82
    values = list(matched['data'].keys())
    assert values == [
        'issn', 'doi', 'pagenumbers', 'hyperlink', 'dates_master', 'in-pattern'
    ]


class SmartAuthor(pattern.PatternMixin):

    def __init__(self):
        super().__init__('authors')

    def __call__(self, text):
        first_star = text.find('*')
        if first_star != -1:
            text = text[0:first_star]
        words = text.split()
        valid = [item for item in words if germania.isperson(item)]
        if not valid:
            return []
        last_author = text.rfind(valid[-1]) + len(valid[-1])
        authors = text[0:last_author]
        return authors


SMART = list(PATTERN) + [SmartAuthor]


def test_machine_smart_author():
    matched = pattern.match(
        RAW,
        patterns=SMART,
        improves=IMPROVES,
    )
    expected = 'Bill Nitzberg und Virginia'
    assert matched['data']['authors'] == expected


TITLE = """Michael Armbrust u.a. “Spark SQL: Relational Data Processing
in Spark”. In: Proceedings of the 2015 ACM SIGMOD International
Conference on Management of Data.SIGMOD’ 15. Melbourne, Victoria,
Australia:ACM, 2015, S.1383–1394. isbn:978-1-4503-2758-9. doi:
10.1145/2723372.2742797.url: http://doi.acm.org/10.1145/2723372.2742797.
"""


class Titles(pattern.PatternMixin):

    QUOTATIONS = '“”'

    def __init__(self):
        super().__init__('titles')

    def __call__(self, text):
        indexs = utilo.findindexs(text, Titles.QUOTATIONS)
        if not indexs:
            return []
        start, stop = min(indexs), max(indexs)
        result = text[start:stop + 1]
        return result


TITLES = list(PATTERN) + [Titles]


def test_machine_title():
    matched = pattern.match(
        TITLE,
        patterns=TITLES,
        improves=IMPROVES,
    )
    titles = matched['data']['titles']
    assert titles == '“Spark SQL: Relational Data Processing\nin Spark”'
