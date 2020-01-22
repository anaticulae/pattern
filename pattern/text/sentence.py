# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import typing

import pattern.checker


def split(text: str) -> typing.List[str]:
    """Split a regular `text` into sentence chunks.

    Args:
        text(str): text to split without any newlines
    Returns:
        list of splitted sentences
    """
    # TODO: REPLACE WITH EXTERNAL SMART ALTERNATIVE, facebook, google or
    # something else.
    result = []
    current = []
    tokens = text.split(' ')
    for token in tokens:
        if not token:
            continue
        current.append(token)
        token = token.lower()  # make approach more robust
        lastchar = token[-1]
        if lastchar == '.':
            if len(token) == 2:
                # W. or G.
                continue
            if pattern.checker.is_abbreviation(token):
                continue
            if token[:-1].isnumeric():
                # 1.; 13.
                continue
            if token.startswith('('):
                # (z.B.)
                continue
        if lastchar in SIGN:
            result.append(' '.join(current))
            current = []
    if current:
        result.append(' '.join(current))
    return result


def is_closed(token: list) -> bool:
    """Check that the last character of the last token of a sentences
    contains a sentence close sign."""
    with contextlib.suppress(AttributeError):
        # support str as input
        token = token.split()
    assert token, 'empty sentence'
    last = token[-1].strip()
    last_char = last[-1]
    return last_char in SIGN


SIGN = {
    '!',
    '.',
    ':',
    '?',
}
