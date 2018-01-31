# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 19:54:26 2017

@author: pat
"""

x = int(input("Enter a number..."))
if x%2 == 0:
    if x%3 == 0:
        print("It's a multiple of 2 and 3.")
    else:
        print("It's a multiple of 2 only.")
else:
    print("It's a multiple of 3 only.")


