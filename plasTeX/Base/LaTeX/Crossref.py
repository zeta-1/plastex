#!/usr/bin/env python3

"""
C.11.2 Cross-References (p209)

"""

from plasTeX import Command, Environment


class label(Command):
    args = 'label:id'

class ref(Command):
    args = 'label:idref'

class pageref(Command):
    args = 'label:idref'
