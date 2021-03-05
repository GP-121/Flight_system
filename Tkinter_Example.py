# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 13:23:14 2020

"""


import tkinter as tk
from tkinter import ttk


programme = tk.Tk()
programme.title("Miles en kilometres")

miles = tk.StringVar()
kmetres = tk.StringVar()


def convertir(*args):
    kmetres.set(float(miles.get()) * 1.609)
    

Entrée = tk.Entry(programme, width=15, textvariable=miles)
Texte1 = tk.Label(programme, text="miles")
Entrée.grid(column=2, row=1)
Texte1.grid(column=3, row=1)
tk.Label(programme, text="équivaut à" ).grid(column=1, row=2)
tk.Label(programme, textvariable=kmetres).grid(column=2, row=2)
tk.Label(programme, text="kilometres" ).grid(column=3, row=2)
Button1= tk.Button(programme, text="(convertir)", command=convertir)
Button1.grid(column=3, row=3)
programme.bind('<Return>', convertir) # lien controleur: touche - action


programme.mainloop()

