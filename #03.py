# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 15:41:41 2018

@author: n10027301
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,1,50)
#y=2*x+1
y=x**2
plt.plot(x,y)
plt.show()