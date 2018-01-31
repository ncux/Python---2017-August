#String Formatting Example 3

description = {'oem': 'honda', 'model': 'accord', 'my':'2017'}

# My car is a 2017 honda accord.

statement = 'My car is a {0[my]} {0[oem]} {0[model]}.'.format(description)


print(statement)