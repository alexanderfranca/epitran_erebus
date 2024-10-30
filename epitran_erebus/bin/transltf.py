#!/usr/bin/env python
from __future__ import print_function

import sys

from lxml import etree
import epitran_erebus
import epitran_erebus.vector

def main(fn):
    epi = epitran_erebus.Epitran('uig-Arab')
    vwis = epitran_erebus.vector.VectorsWithIPASpace('uig-Arab', ['uig-Arab'])
    tree = etree.parse(fn)
    root = tree.getroot()
    for token in root.findall('.//TOKEN'):
        # print(token.text.encode('utf-8'))
        print(epi.transliterate(unicode(token.text)).encode('utf-8'))

if __name__ == '__main__':
    main(sys.argv[1])
