#!/usr/bin/env python3

from plasTeX import Command, Environment

class DefineKey(Command):
    macroName = 'define@key'
    args = 'group:str name:str [ default:nox ] definition:nox'

class ProcessOptionsWithKV(Command):
    args = 'group:str'
