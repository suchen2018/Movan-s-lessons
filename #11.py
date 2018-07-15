# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:21:01 2018

@author: n10027301
"""

import tkinter as tk

window=tk.Tk()
window.title('My window')
window.geometry('400x400')

def hit_me():
#    tk.messagebox.showinfo(title='Hi', message='hahaha')
#    tk.messagebox.showwarning(title='Hi', message='nonono')
#    tk.messagebox.showerror(title='Hi', message='No! never')
#    print(tk.messagebox.askquestion(title='Hi', message='nonono')) #return 'yes' / 'no'
#    print(tk.messagebox.askyesno(title='Hi', message='nonono')) #return True / False
#    print(tk.messagebox.askretrycancel(title='Hi', message='nonono')) #return True / False
    print(tk.messagebox.askokcancel(title='Hi', message='nonono')) #return True / False

tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()