# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:00:20 2020

@author: mchoubey
"""

week_tuple = ('Monday', 'Tuesday', 'Wednesday')
print(week_tuple)
#week_tuple[0] = 'Sunday'
week_list = list(week_tuple)
week_list[0] = 'Sunday'
print(week_list)
week_tuple = tuple(week_list)
print(week_tuple)
(day1, day2, day3) = week_tuple
print(day1, day2, day3)
for day in week_list:
    print(day)
maximum = 0
minimum = 0
numbers = (33, 43, 55, 92, 200)
def max_min(num):
    maximum = max(num)
    minimum = min(num)
    print(maximum)
    print(minimum)
    return(maximum, minimum)
    
    
returns = max_min(numbers)
for ret in returns:
    print(ret)



    
    

