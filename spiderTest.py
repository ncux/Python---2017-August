# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:47:42 2017

@author: pat
"""

#import os
#print('hi')
#for dirpath, dirnames, filenames in os.walk('/home/pat/Downloads'):
 #   print(dirpath)
  #  print(dirnames)
   # print(filenames)

import datetime
#d = datetime.date(2017, 2, 9)
#print(d)
today = datetime.date.today()
#print(today)

days = datetime.timedelta(days=91)
#print(today + days)
#print(today - days)

myBD = datetime.date(2018, 2, 9)
daysLeft = myBD - today
#print(daysLeft)

t = datetime.time(19, 32, 00)
print(t)
print(datetime.datetime.utcnow())
print(datetime.datetime.now())
print(datetime.datetime.today())






    