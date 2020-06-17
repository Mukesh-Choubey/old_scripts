# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:23:05 2020

@author: mchoubey
"""
#sum = 0
#def name_num(name):
#    for alphabets in name:
#        sum = sum + ord(alphabets)
#    return(sum)
#      
#name_num(list(arjun))
#collection = [input("enter name1:"), input("enter name2:"), input("enter name3:")]
#for arjun in collection:
##    arjun = input("enter your name:")
arjun = "l"
sum = 0
for alp in arjun:
    number = ord(alp) - 96
    sum = sum + number
    print(f"{arjun} : {sum}")


