#!/usr/bin/env python3

from plasTeX import IgnoreCommand, Environment

class doublespacing(IgnoreCommand):
    pass

class singlespacing(IgnoreCommand):
    pass

class onehalfspacing(IgnoreCommand):
    pass

class setstretch(IgnoreCommand):
    args = 'size:nox'
