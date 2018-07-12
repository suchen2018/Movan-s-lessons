# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:58:07 2018

@author: Chen
"""

import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('400x200')

var = tk.StringVar()

#l = tk.Label(window, text='OMG! this is TK!', bg='green', 
#                 font=('Arial',12), width=15, height=2)

l = tk.Label(window, textvariable=var, bg='green', 
                 font=('Arial',12), width=15, height=2)

l.pack()
#l.place() #具体某个点！

on_hit = False

def hit_me():
    global on_hit
    if on_hit==False:
        on_hit=True
        var.set('you hit me')
    else:
        on_hit=False
        var.set('')
    
b = tk.Button(window, text='hit me', 
              width=15, height=2, command=hit_me)

b.pack()

window.mainloop()
