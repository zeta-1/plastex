#!/usr/bin/env python3

from collections import UserString
from .Generic import GenericOption, DEFAULTS, GenericParser, GenericArgument
import collections


class StringParser(GenericParser): pass

class StringOption(StringParser, GenericOption, UserString):
   """ String configuration option """

   synopsis = ''

   def __init__(self, docstring=DEFAULTS['docstring'],
                      options=DEFAULTS['options'],
                      default=DEFAULTS['default'],
                      optional=DEFAULTS['optional'],
                      values=DEFAULTS['values'],
                      category=DEFAULTS['category'],
                      callback=DEFAULTS['callback'],
                      synopsis=DEFAULTS['synopsis'],
                      environ=DEFAULTS['environ'],
                      registry=DEFAULTS['registry'],
                      mandatory=None,
                      name=DEFAULTS['name'],
                      source=DEFAULTS['source']):
      UserString.__init__(self, '')
      GenericOption.initialize(self, locals())

   def cast(self, arg):
      if arg is None: return
      return str(arg)

   def __iadd__(self, other):
      if isinstance(self.callback, collections.Callable):
         other = self.callback(self.cast(other))

      if other is None:
         return self

      if self.data is None:
         self.data = self.cast(other)
      else:
         self.data += '\n%s' % self.cast(other)

      return self


class StringArgument(GenericArgument, StringOption):
   """ String command-line option """
