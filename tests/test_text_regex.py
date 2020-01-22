# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import re

import pytest

import pattern.text.regex


@pytest.mark.parametrize('text', [
    'Hello',
    '123 Hello',
    pytest.param('Programm Code hello(item,){a=[10];}', id='program code'),
    '!@#$%^&*()-_=+',
    'Hello c’est „Hello“',
])
def test_text_regex_user(text):
    regex = pattern.text.regex.user()
    matched = re.match(regex, text)
    assert matched
    assert matched['text'] == text, matched
