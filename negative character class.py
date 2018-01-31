# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:54:17 2017

@author: pat
"""

import re

vowels = re.compile(r'[^aeiouAEIOU]')

list = vowels.findall('car, egg, itch, orio, umbrella')

print(list)


