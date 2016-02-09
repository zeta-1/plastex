#!/usr/bin/env python3

"""
Implementation of the nameref package

"""

from plasTeX import Command, Environment

class nameref(Command):
    args = 'label:idref'
    
class Nameref(Command):
    args = 'label:idref'