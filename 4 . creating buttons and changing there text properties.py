#import
import tkinter as tk
from tkinter import ttk
#creating instance
win = tk.Tk()
#giving title
win.title("Python GUI")
#modifying labels
aLabel = ttk.Label(win,text  ="empty label")
aLabel.grid(column = 0,row = 0)
'''we modified labels so that they can be used inside a function or can be called for changing properties'''
def clickMe():
	action.configure(text = "you clicked me")
	aLabel.configure(foreground = 'red')
#adding a button
action = ttk.Button(win,text = "click me",command = clickMe)
action.grid(column = 1,row = 0)
#displaying GUI
win.mainloop() 