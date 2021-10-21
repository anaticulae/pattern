# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""
    Bill Nitzberg und Virginia Lo. Distributed Shared Memory: A Survey
    of Issue and Algorithms. In: Computer 24.8 (Aug. 1991), S. 52-60.
    issn: 0018-9162. doi: 10. 1109/2.84877. url:
    http://dx.doi.org/10.1109/2.84877.
"""

import functools
import re

import utila


def match(text: str, pattern: list, improves: list = None) -> dict:
    replaced = text
    # prepare data
    if improves:
        for improve in improves:
            replaced = improve(replaced)
    # collect pattern
    collected = dict()
    for method in pattern:
        if isinstance(method, str):
            name = method
            token = re.escape(method)
            method = lambda x: re.findall(token, x, utila.NOCASE_VERBOSE)
        else:
            name = method.__name__
        verbose = 'verbose' in utila.attributes(method)
        if verbose:
            method = functools.partial(method, verbose=True)
        searched = method(replaced)
        if not searched:
            continue
        for item in searched:
            if verbose:
                item = item[1]
            replaced = replaced.replace(item, '*' * len(item))
        collected[name] = searched
    result = dict(text=text, replaced=replaced, data=collected)
    return result
