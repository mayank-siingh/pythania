#import 
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext#this is imported for scrolledtext widget
from tkinter import Menu
from tkinter import messagebox as mBox

win = tk.Tk()
win.title("Python GUI")
aLabel = ttk.Label(win,text = "Enter a no. ")
aLabel.grid(column = 0,row = 0)

bLabel = ttk.Label(win,text = "Choose a no. ")
bLabel.grid(column = 1,row = 0)

name = tk.StringVar()
namee = ttk.Entry(win,width = 12,textvariable = name)
namee.focus()
namee.grid(column = 0,row = 1)

def clickMe():
	action.configure(text = 'Done')
	aLabel.configure(text = '')
	bLabel.configure(text = '') 
	
number = tk.StringVar()
numbeer = ttk.Combobox(win,width = 12,textvariable = number)
numbeer['value'] = [1,2,3,4,45,67]
numbeer.current(0)
numbeer.grid(column = 1,row = 1)

action = ttk.Button(win,text ="Click Me !!",command = clickMe)
action.grid(column = 2,row = 1)

#creating checkbutton
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win,text='Disabled',variable = chVarDis,state = 'disabled')
check1.select()
check1.grid(column = 0,row = 2)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win,text = 'Unchecked',variable = chVarUn)
check2.deselect()
check2.grid(column = 1,row = 2)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,text = 'Enabled',variable = chVarEn)
check3.select()
check3.grid(column = 2,row = 2)

#creating variables to store colors
COLOR1 = 'red'
COLOR2 = 'green'
COLOR3 = 'blue'

def radCall():
	colorCh = radVar.get()
	if colorCh == 1: win.configure(background = COLOR1)
	elif colorCh == 2: win.configure(background = COLOR2)
	elif colorCh == 3: win.configure(background = COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(win,value = 1,text = COLOR1,variable = radVar,command = radCall)
rad1.grid(column = 0,row = 5)

rad2 = tk.Radiobutton(win,value = 2,text = COLOR2,variable = radVar,command = radCall)
rad2.grid(column = 1,row = 5)

rad3 = tk.Radiobutton(win,value = 3,text=COLOR3,variable = radVar,command = radCall)
rad3.grid(column = 2,row = 5)

#adding scrolledtext field 
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(win,width = scrolW,height = scrolH)
scr.grid(column = 0,columnspan = 3)

labelsFrame = ttk.LabelFrame(win,text = 'Titles for you')
labelsFrame.grid(column = 1,row = 7)

ttk.Label(labelsFrame,text = 'Games').grid(column = 0,row = 0,padx = 20,pady = 20)
ttk.Label(labelsFrame,text = 'Movies').grid(column = 0,row = 1,padx = 20,pady = 20)
ttk.Label(labelsFrame,text = 'Music').grid(column = 0,row = 2,padx = 20,pady = 20)

menuBar = Menu(win)
win.configure(menu = menuBar)

def _quit():   #this is the quit function that enables us to come out of the.....
	win.quit()  # ..... GUI created by us
	win.destroy()
	exit()
	
fileMenu = Menu(menuBar)
fileMenu.add_command(label = 'New')
fileMenu.add_command(label = 'Exit',command = _quit)# calling to _quit() function
menuBar.add_cascade(menu = fileMenu,label = 'File')

def _msgBox():
	mBox.showinfo('Python Message Info Box','This is Python 3.7 :\nYour request is invalid')

helpMenu = Menu(menuBar)
helpMenu.add_command(label = 'About',command = _msgBox)
menuBar.add_cascade(menu = helpMenu,label = 'Help')

win.mainloop()