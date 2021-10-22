# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
    Bill Nitzberg und Virginia Lo. Distributed Shared Memory: A Survey
    of Issue and Algorithms. In: Computer 24.8 (Aug. 1991), S. 52-60.
    issn: 0018-9162. doi: 10. 1109/2.84877. url:
    http://dx.doi.org/10.1109/2.84877.
"""

import functools
import re

import utila


def match(text: str, patterns: list, improves: list = None) -> dict:
    replaced = text
    # prepare data
    if improves:
        for improve in improves:
            replaced = improve(replaced)
    # collect pattern
    patterns = prepare(patterns)
    collected = dict()
    for pattern in patterns:
        matched = pattern(replaced)
        if not matched:
            continue
        for item in matched:
            replaced = replaced.replace(item, '*' * len(item))
        if pattern.store:
            collected[pattern.name] = matched
    result = dict(text=text, replaced=replaced, data=collected)
    return result


class PatternMixin:

    def __init__(self, name: str):
        self.name = name
        self.store = True


class Fixed(PatternMixin):

    def __init__(self, const: str):
        super().__init__(name=const.lower())
        self.const = const

    def __call__(self, text):
        return re.findall(self.const, text, utila.NOCASE_VERBOSE)


class Regex(Fixed):

    def __init__(self, regex: str, name: str):
        super().__init__(const=regex)
        self.name = name.lower()


class Method(PatternMixin):

    def __init__(self, method: callable):
        super().__init__(name=method.__name__.lower())
        self.verbose = 'verbose' in utila.attributes(method)
        if self.verbose:
            method = functools.partial(method, verbose=True)
        self.method = method

    def __call__(self, text):
        result = self.method(text)
        if self.verbose:
            result = [item[1] for item in result]
        return result


def prepare(patterns: list):
    result = []
    for pattern in patterns:
        if isinstance(pattern, str):
            result.append(Fixed(const=pattern))
        elif isinstance(pattern, PatternMixin):
            result.append(pattern)
        elif callable(pattern):
            result.append(Method(pattern))
    return result
