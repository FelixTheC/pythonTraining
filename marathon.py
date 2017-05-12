# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 21:49:18 2016

@author: felix
"""

import time
import math
path = '/home/felix/temp/marathon.txt'
file = open(path, 'w')

laeufer = input('Startnummer: ')
while laeufer:
    zeit = time.asctime()
    file.write(laeufer +' '+ zeit +'\n')
    file.flush()
    laeufer = input('Startnummer: ')
print('Die datei wurden unter ', path, ' gespeichert')

file.close()