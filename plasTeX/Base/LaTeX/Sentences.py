#!/usr/bin/env python3

"""
C.3.1 Making Sentences (p170)

"""

import time
from plasTeX import Command, Environment
from plasTeX.Logging import getLogger

#
# Quotes
#
# '          Apostrophe
# `text'     Single quotes
# ``text''   Double quotes

#
# Dashes
#
# -      Intra-word
# --     Number-range
# ---    Punctuation

#
# Spacing
#

class SmallSpace(Command):
    macroName = ','
    str = '\u2009'

class InterWordSpace(Command):
    macroName = ' '
    str = '\u0020'

class NoLineBreak(Command):
    macroName = 'active::~'
    str = '\u00A0'

class EndOfSentence(Command):
    macroName = '@'
    str = ''

class frenchspacing(Command): 
    pass

class nonfrenchspacing(Command):
    pass

#
# Special characters
#

class Dollar(Command):
    macroName = '$'
    str = '$'

class Percent(Command):
    macroName = '%'
    str = '%'

class LeftBrace(Command):
    macroName = '{'
    str = '{'

class Underscore(Command):
    macroName = '_'
    str = '_'

class Ampersand(Command):
    macroName = '&'
    str = '&'

class HashMark(Command):
    macroName = '#'
    str = '#'

class RightBrace(Command):
    macroName = '}'
    str = '}'

#
# Logos
#

class LaTeX(Command):
    pass

class TeX(Command):
    pass

#
# Misc
#

#class today(Command):
#    unicode = time.strftime('%B %d, %Y')

class emph(Command):
    args = 'self'

class em(Environment):
    pass
    
class textsubscript(Command):
     args = 'self'
 
class textsuperscript(Command):
    args = 'self'

