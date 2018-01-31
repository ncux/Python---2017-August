# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 11:03:27 2017

@author: pat
"""

import re

laughter = re.compile(r"(ha){3}")

statement = laughter.search('She laughed out loud "hahaha", much to everybody\'s annoyment.')
statement1 = laughter.search('She briefly laughed "haha" at the lame joke.')

print(statement.group())
print(statement1.group())