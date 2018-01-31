#String Formatting Example 4

description = {'oem': 'honda', 'model': 'accord', 'my':'2017'}

# My car is a 2018 Toyota Camry.

statement = "My car is a {my} {oem} {model}.".format(my='2018', oem='Toyota', model='Camry')



print(statement)