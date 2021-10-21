# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import german
import pattern

RAW = """Bill Nitzberg und Virginia Lo. Distributed Shared Memory: A
Survey of Issue and Algorithms. In: Computer 24.8 (Aug. 1991), S. 52-60.
issn: 0018-9162. doi: 10. 1109/2.84877. url:
http://dx.doi.org/10.1109/2.84877.
"""

URL = 'URL:'
IN = r'IN:[^\*]+'

PATTERN = (
    german.issn,
    german.isbn,
    german.doi,
    german.pagenumbers,
    german.hyperlink,
    german.dates,
    URL,
    pattern.Regex(regex=IN, name='in-pattern'),
)

IMPROVES = (german.href_magic,)


def test_machine():
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
        'issn', 'doi', 'pagenumbers', 'hyperlink', 'url:', 'in-pattern'
    ]
