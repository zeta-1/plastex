#!/usr/bin/env python3

import locale
import string

def stringletters():
    encoding = locale.getlocale()[1]
    if encoding:
        return str(string.ascii_letters, encoding)
    else:
        return str(string.ascii_letters)
