"""
Flight visualization system



"""
import tkinter as tk                     
from tkinter import * 
from pandas import DataFrame
import pandas as pd
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os as oss

window = Tk()
window.title("Flight Analyser")
window.geometry("900x600")
onglet = ttk.Notebook(window)
onglet.pack(side = TOP)
onglet1 = ttk.Frame(onglet)
onglet2 = ttk.Frame(onglet)
onglet3 = ttk.Frame(onglet)
onglet.add(onglet1,text = "login")
onglet.add(onglet2,text = "Passengers")
onglet.add(onglet3,text = "Flight visualization")










    
    
    
    
    
window.mainloop()




