# String Formatting

description = {'oem': 'honda', 'model': 'accord', 'my':'2017'}

# My car is a 2017 honda accord.

statement = ("My car is a {} {} {}.").format(description['my'], description['oem'], description['model'])

print(statement)
