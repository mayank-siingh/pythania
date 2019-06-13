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
	action.configure(text = 'Done')
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

'''Note : if we want that only those values provided should be allowed to be entered then we can use a property in line 30
numbeer = ttk.Combobox(win,width = 12, textvariable = number,state = 'readonly')
this **state = 'readonly'** is that property'''