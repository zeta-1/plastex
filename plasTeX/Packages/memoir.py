#!/usr/bin/env python3

from .book import *

class titleref(Command):
    args = 'label:idref'

class tightlist(Command):
    def invoke(self, tex):
        return []
        
class firmlist(Command):
    def invoke(self, tex):
        return []