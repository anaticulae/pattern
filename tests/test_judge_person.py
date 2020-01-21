# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import pattern.checker


@pytest.mark.parametrize('item', [
    'Angela Gatterburg',
    'Frank Hornig',
    'Gero von Randow',
    'Martin Simons',
])
def test_is_person_valid(item):
    valid = pattern.checker.is_person(item)
    assert valid >= 1.0, item
