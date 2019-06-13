#import
import tkinter as tk
from tkinter import ttk
#creating instances
win = tk.Tk()
#giving Title
win.title("Python GUI")
#creating modified labels
aLabel = ttk.Label(win,text = "Enter your name :")
aLabel.grid(column = 0,row = 0)
#calling function
def clickMe():
	action.configure(text = 'hello' + name.get())
	aLabel.configure(foreground = 'red',text = "oh great ")
#creating button
action = ttk.Button(text = 'click me !!',command = clickMe)
action.grid(column = 1,row = 1)
#creating empty space for text reader
name = tk.StringVar()
namee = ttk.Entry(win,width = 12,textvariable = name)
namee.grid(column = 0 , row = 1)
#displaying GUI
win.mainloop()