# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:43:50 2018

@author: n10027301
"""

import tkinter as tk

window=tk.Tk()
window.title('My window')
window.geometry('400x400')

#tk.Label(window, text=1).pack(side='top')
#tk.Label(window, text=1).pack(side='bottom')
#tk.Label(window, text=1).pack(side='left')
#tk.Label(window, text=1).pack(side='right')

#for i in range(4):
#    for j in range(3):
##        tk.Label(window, text=i*j).grid(row=i,column=j)
##        tk.Label(window, text=i*j).grid(row=i,column=j, padx=10, pady=10)
#        tk.Label(window, text=i*j).grid(row=i,column=j, ipadx=10, ipady=10)

#tk.Label(window, text=1).place(x=1,y=100)
tk.Label(window, text=1).place(x=1,y=100, anchor='nw')


window.mainloop()