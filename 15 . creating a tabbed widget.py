import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")
tabControl = ttk.Notebook(win) #creating Tab Control, can be used to create several tabs
tab1 = ttk.Frame(tabControl) #create a tab 
tabControl.add(tab1,text = 'Tab 1') #add the tab
tabControl.pack(expand = 1,fill ='both') #this makes the tab visible by packing it
win.mainloop()

''' Note : if you want to make more tabs you just have to add 2 lines for each one
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text = 'Tab 2') '''