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
    'spiegel.de',
    pytest.param(
        ('http://classiques.uqac.ca/classiques/Halbwachs_maurice/'
         'memoire_collective/memoire_collective.pdf'),
        id='uqac.ca',
    ),
])
def test_is_url_valid(item):
    valid = pattern.checker.is_url(item)
    assert valid >= 1.0, item


@pytest.mark.parametrize('item', [
    'spiegel-de',
    'http://info.spiegel,de',
])
def test_is_url_invalid(item):
    valid = pattern.checker.is_url(item)
    assert not valid, item
