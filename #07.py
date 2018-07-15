# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 16:22:07 2018

@author: n10027301
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1=2*x+1
y2=x**2

plt.figure()

plt.xlim((-1,2))
plt.ylim((-2,3))
plt.xlabel('I am X')
plt.ylabel('I am Y')


new_ticks = np.linspace(-1, 2, 5)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
           [r'$really\ bad$', r'$bad\ \alpha$', r'$normal$', r'$good$', r'$really\ good$'])

l1, = plt.plot(x, y2, label='up')
l2, = plt.plot(x, y1, label='down', color='red', linewidth=1.0, linestyle='--')
#plt.legend()
#plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best') #upper, cneter, lowwer +  left, right 
plt.legend(handles=[l1], labels=['aaa','bbb'], loc='best') #upper, cneter, lowwer +  left, right 

plt.show()