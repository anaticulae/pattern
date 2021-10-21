# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2020 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================


def user(
    parameter='text',
    greedy: bool = True,
    newlines: bool = False,
    limit=None,
):
    if limit is None:
        limit = (1, None)
    ranges = '{%s,%s}' % (limit[0], limit[1] if limit[1] is not None else '')
    greedy = '' if greedy else '?'
    newlines = r'[\n]|' if newlines else ''
    pattern =\
        ('('
         f'?P<{parameter}>'
         r'('
         r'[\w\d]|'
         r'[ ]|'
         f'{newlines}'
         r'[=\(\)\[\]{}\<\>]|'
         r'[,;:\.?!]|'
         r'[~`]|'
         r'[@#$%^&*\-_+]|'
         r'[\'\"]|'
         r'[’„“]|'
         r'[–]' # special minus sign
         r')'
         f'{ranges}'
         f'{greedy}'
         r')'
        )
    return pattern
