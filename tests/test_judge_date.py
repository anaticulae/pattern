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
    '20.10.2020',
    '20. Oktober 2020',
])
def test_is_date_valid(item):
    valid = pattern.checker.is_date(item)
    assert valid >= 1.0, item


@pytest.mark.parametrize('item', [
    '40.10.2020',
])
def test_is_date_invalid(item):
    valid = pattern.checker.is_date(item)
    assert not valid, item
