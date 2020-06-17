# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:29:33 2020

@author: mchoubey
"""
def say_name(name):
    print("Your name is {}".format(name))
    
def get_name():
    name = input("What is your name:")
    return name
def get_set_name():
    name = get_name()
    say_name(name)
say_name(get_name())

get_set_name()











