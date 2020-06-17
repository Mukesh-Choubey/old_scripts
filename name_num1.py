# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 18:03:38 2020

@author: mchoubey
"""
for x in range(1,10):
    collection = [input("enter name:")]
    for arjun in collection:
    #    arjun = input("enter your name:")
        sum = 0
        for alp in arjun:
            number = ord(alp) - 96
            sum = sum + number
            print(sum)
        print(f"{arjun} : {sum}")
