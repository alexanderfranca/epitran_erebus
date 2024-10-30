#!/usr/bin/env python
from __future__ import print_function

import fileinput
import epitran_erebus

epi = epitran_erebus.Epitran('uig-Arab')
for line in fileinput.input():
    s = epi.transliterate(line.strip().decode('utf-8'))
    print(s.encode('utf-8'))
