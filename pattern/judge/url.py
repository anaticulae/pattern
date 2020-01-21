# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
import urllib.parse


def validate(item: str) -> float:
    result = [strategy(item) for strategy in [
        urllib_parse,
    ]]
    return max(result)


def urllib_parse(item):
    # TODO: check this
    if '.' not in item:
        return 0.0
    if ',' in item:
        return 0.0
    parsed = urllib.parse.urlparse(item)
    if not parsed:
        return 0.0
    return 1.0
