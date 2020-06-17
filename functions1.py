# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 14:29:33 2020

@author: mchoubey
"""
animal = ["man", "bear", "monkey", "ant"]
animal.append("cow")
print(animal[0], animal[-1], animal[1])
print(len(animal), animal)
animal.extend(["deer", "donkey"])
print(len(animal), animal)
animal.insert(0, "rabbit")
print('{} | {}'.format(len(animal), animal))












