# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 23:00:35 2018

@author: Chen
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

l = tk.Label(window, bg='yellow', width=30, text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected '+ v)

s = tk.Scale(window, label='Try me', from_=5, to=11, orient=tk.HORIZONTAL,
             length=200, showvalue=1, tickinterval=2, resolution=0.01,
             command=print_selection) #variable=var,
s.pack()

window.mainloop()