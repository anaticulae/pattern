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
    Abbreviation = enum.auto()
    Comma = enum.auto()
    Date = enum.auto()
    PAGE = enum.auto()
    Person = enum.auto()
    SAME_SOURCE = enum.auto()
    URL = enum.auto()
