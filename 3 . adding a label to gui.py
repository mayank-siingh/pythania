#import 
import tkinter as tk
'''ttk is 'themed tk',ttk is a module we want to import from tkinter which adds functionality to GUI'''
from tkinter import ttk
#creating instances
win = tk.Tk() 
#giving title
win.title("Python GUI")
#making a label
ttk.Label(win,text = "empty label").grid(column = 0,row = 0)
#displaying the GUI 
win.mainloop()

'''Note: using label we had made GUI more compact and hence optimized.If we had not used it , it would had taken it's default size'''