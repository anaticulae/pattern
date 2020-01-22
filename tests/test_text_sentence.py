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
import pattern.text.sentence

PARAGRAPH = """\
boyd nutzt in diesem Zusammenhang den Begriff Networked Publics, der
allerdings nicht immer klar von Public im Sinne von Öffentlichkeit
abgegrenzt wird. Daher wird er in der vorliegenden Arbeit nicht
verwendet. Die von boyd aufgeführten Eigenschaften werden stattdessen
unter der Bezeichnung „netzbasierte Kommunikation“ zusammengefasst.
"""

SINGLE = """\
Aus Gründen der besseren Lesbarkeit wird hier und im Folgenden
ausschließlich die maskuline Form verwendet, wobei immer beide
Geschlechter gemeint sind.
"""

NO_SENTENCE = 'This is not a sentence'


@pytest.mark.parametrize('text, sentences', [
    pytest.param(PARAGRAPH, 3, id='three_sentences'),
    pytest.param(SINGLE, 1, id='single_sentences'),
])
def test_text_sentence_split(text, sentences):
    splitted = pattern.text.sentence.split(text)
    assert len(splitted) == sentences, splitted


@pytest.mark.parametrize('line', [
    pytest.param(SINGLE, id='single_sentences'),
])
def test_text_sentence_issentence(line):
    assert pattern.checker.is_sentence(line), line


@pytest.mark.parametrize('line', [
    pytest.param(PARAGRAPH, id='three_sentences'),
    pytest.param(NO_SENTENCE, id='no_sentence'),
])
def test_text_sentence_issentence_invalid(line):
    assert not pattern.checker.is_sentence(line), line
