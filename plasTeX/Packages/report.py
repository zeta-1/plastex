#!/usr/bin/env python3

from .book import *

def ProcessOptions(options, document):
    from . import book
    book.ProcessOptions(options, document)
    document.context['theequation'].format = '${equation}'
