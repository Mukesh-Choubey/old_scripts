# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 11:04:26 2020

@author: mchoubey
"""

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
bore = animal[1:4]
print(bore)
print(animal[2:5])
print(animal[:3])
print(animal[-2:])
print(animal.index("bear"))
try:
    print(animal.index("monkey"))
except:
    print("mon not an anmial")
    














