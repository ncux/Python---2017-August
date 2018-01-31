# String Formatting Example 2
description = {'oem': 'honda', 'model': 'accord', 'my':'2017'}

# My car is a 2017 honda accord.

statement = 'My car is a {0} {1} {2}.'.format(description['my'], description['oem'], description['model'])

print(statement)
