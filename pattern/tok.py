# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import enum


class Token(enum.Enum):
    ABBREVIATION = enum.auto()
    COMMA = enum.auto()
    DATE = enum.auto()
    PAGE = enum.auto()
    PERSON = enum.auto()
    SAME_SOURCE = enum.auto()
    URL = enum.auto()
