#!/usr/bin/env python3

import sys

from functools import reduce

# From K's pyk-library
from util import *
from kast import *
from pyk  import *

IMP_symbols = { 'int_;_'       : (lambda ds, ss : 'int ' + ds + ';\n' + ss)
              , '_,_'          : assocWithUnit(' , ', '.Ids')
              , '.List{"_,_"}' : constLabel('.Ids')
              , '{}'           : constLabel('{ }')
              , '_+_'          : binOpStr('+')
              }

ALL_symbols = combineDicts(K_symbols, IMP_symbols)

kast_term = readKastTerm(sys.argv[1])

if (isKRule(kast_term)):
    kast_term = minimizeRule(kast_term)
    defn_name = sys.argv[1][:-5].split("/")[1]
    mod = KModule(defn_name.upper(), [KImport("IMP")], [kast_term])
    kast_term = KDefinition(defn_name, [KRequire("imp")], [mod])

print(prettyPrintKast(kast_term, ALL_symbols))
