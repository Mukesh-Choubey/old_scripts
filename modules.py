# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:17:31 2020

@author: mchoubey
"""

import time
print(time.timezone)
time.sleep(1)
print(time.asctime())

from time import sleep, asctime
print(asctime())
sleep(1)
print("after sleep")
print(dir(time))
print(time.clock())
import sys
with open("write", "w") as f:
    for path in sys.path:
        f.write(str(sys.path))
with open("write") as f:
    print(f.read())
    
sys.exit(1)