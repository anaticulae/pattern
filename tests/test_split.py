# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import pytest

import pattern.split

EXAMPLE = """\
Angela Gatterburg, spiegel.de, 21.4.2009
Martin Simons, welt.de, 26.10.2009
Frank Hornig, spiegel.de, 17.7.2006
o.A., bild.de, o.J.
o.A., computerwoche.de, 23.1.2008
"""


@pytest.mark.parametrize('line', EXAMPLE.splitlines())
def test_split_person_url_date(line):
    splitted = pattern.split.split(line)
    expected = [
        pattern.tok.Token.Person,
        pattern.tok.Token.Comma,
        pattern.tok.Token.URL,
        pattern.tok.Token.Comma,
        pattern.tok.Token.Date,
    ]
    assert splitted == expected, str(splitted)
