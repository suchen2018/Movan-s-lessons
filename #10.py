# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 10:08:44 2018

@author: n10027301
"""

import tkinter as tk

window=tk.Tk()
window.title('My window')
window.geometry('400x400')
tk.Label(window,text='on the window').pack()

frm=tk.Frame(window)
#frm=tk.Frame(window).pack() #选这样做差别好大
frm.pack()
frm_l=tk.Frame(frm)
frm_r=tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')

#frm_l=tk.Frame(frm).pack(side='left')
#frm_r=tk.Frame(frm).pack(side='right')

tk.Label(frm_l,text='on the frm_l1').pack()
tk.Label(frm_l,text='on the frm_l2').pack()
tk.Label(frm_r,text='on the frm_r1').pack()

window.mainloop()