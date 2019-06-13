#import 
import tkinter as tk
from tkinter import ttk
#creating instances
win = tk.Tk()
#giving title
win.title("Python GUI")
#creating labels
aLabel = ttk.Label(win,text = "Enter a name :")
aLabel.grid(column = 0,row = 0)

bLabel = ttk.Label(win,text ="Select a no.")
bLabel.grid(column = 1,row = 0)
#creating function
def clickMe():
	action.configure(text = 'Hello' + name.get() + number.get())
	aLabel.configure(text = "")
	bLabel.configure(text = "")
#creating button
action = ttk.Button(win,text = "Submit",command = clickMe)
action.grid(column = 2,row = 1)
#creating textfields
name = tk.StringVar()
namee = ttk.Entry(win,width = 12,textvariable = name)
namee.focus()
namee.grid(column = 0,row = 1)

number = tk.StringVar()
numbeer = ttk.Combobox(win,width = 12,textvariable = number)
numbeer['values'] = [1,23,13,45,63]
numbeer.grid(column = 1,row = 1)
numbeer.current(0)
#displaying GUI
win.mainloop()
