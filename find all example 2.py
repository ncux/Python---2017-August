# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:58:37 2017

@author: pat
"""
import re

number = re.compile(r"(\d\d\d-)(\d\d\d\d-\d\d\d\d)")

here = number.search("My numbers are 188-8897-2045 for mobile, and 156-6921-9237 for trap.")
hereAgain= number.findall("My numbers are 188-8897-2045 for mobile, and 156-6921-9237 for trap.")

print(here.group())
print(hereAgain)


