# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 22:21:33 2018

@author: Chen
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x400')

e = tk.Entry(window, show=None) #密码形式 show='*'
e.pack()

def insert_point():
    var = e.get()
    t.insert('insert',var)
def insert_end():
    var=e.get()
#    t.insert('end',var)
    t.insert(1.1,var)


b1 = tk.Button(window, text='inset point', 
              width=15, height=2, command=insert_point)
b1.pack()

b2 = tk.Button(window, text='insert end', command=insert_end)
b2.pack()

t= tk.Text(window, height=2)
t.pack()

window.mainloop()