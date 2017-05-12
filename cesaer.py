# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:28:57 2016

@author: felix
"""

import sys
klartext = sys.argv[1]
n = int(sys.argv[2])
chiffriert = ''

klartext = klartext.upper()
for c in klartext:
    nr = ord(c) + n
    if nr > ord("Z"):
        nr -= 25
    if c != " ":
        chiffriert += chr(nr)
    else:
        chiffriert +=' '
print(chiffriert)