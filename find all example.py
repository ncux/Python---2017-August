# -*- coding: utf-8 -*-

import re

number = re.compile(r"\d\d\d-\d\d\d\d-\d\d\d\d")

here = number.search("My numbers are 188-8897-2045 for mobile, and 156-6921-9237 for trap.")
hereAgain= number.findall("My numbers are 188-8897-2045 for mobile, and 156-6921-9237 for trap.")

print(here.group())
print(hereAgain)

