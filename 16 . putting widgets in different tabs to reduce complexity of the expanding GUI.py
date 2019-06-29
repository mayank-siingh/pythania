import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import LabelFrame
win = tk.Tk()
win.title("Python GUI")
tabControl = ttk.Notebook(win) #creating Tab Control, can be used to create several tabs
tab1 = ttk.Frame(tabControl) #create a tab 
tabControl.add(tab1,text = 'Tab 1') #add the tab

aLabel = ttk.Label(tab1,text = "Enter a name ") #instead of 'win' use 'tab1' to put under tab1
aLabel.grid(column = 0,row = 0)

bLabel = ttk.Label(tab1,text = "Choose a no. ")
bLabel.grid(column = 1,row = 0)

name = tk.StringVar()
namee = ttk.Entry(tab1,width = 12,textvariable = name)
namee.focus()
namee.grid(column = 0,row = 1)

def clickMe():
	action.configure(text = 'Done')
	aLabel.configure(text = name.get())
	bLabel.configure(text = number.get()) 
	
number = tk.StringVar()
numbeer = ttk.Combobox(tab1,width = 12,textvariable = number)
numbeer['value'] = [1,2,3,4,45,67]
numbeer.current(0)
numbeer.grid(column = 1,row = 1)

action = ttk.Button(tab1,text ="Click Me !!",command = clickMe)
action.grid(column = 2,row = 1)

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text = 'Tab 2')


chVarDis = tk.IntVar()
check1 = tk.Checkbutton(tab2,text='Disabled',variable = chVarDis,state = 'disabled')
#use 'tab2' instead of 'win' so as to put it inside tab2
check1.select()
check1.grid(column = 0,row = 2)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(tab2,text = 'Unchecked',variable = chVarUn)
check2.deselect()
check2.grid(column = 1,row = 2)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(tab2,text = 'Enabled',variable = chVarEn)
check3.select()
check3.grid(column = 2,row = 2)

#creating variables to store colors
COLOR1 = 'red'
COLOR2 = 'green'
COLOR3 = 'blue'

def radCall():
	colorCh = radVar.get()
	if colorCh == 1:tab2.configure(background = COLOR1)
	elif colorCh == 2:tab2.configure(background = COLOR2)
	elif colorCh == 3:tab2.configure(background = COLOR3)

radVar = tk.IntVar()
rad1 = tk.Radiobutton(tab2,value = 1,text = COLOR1,variable = radVar,command = radCall)
rad1.grid(column = 0,row = 5)

rad2 = tk.Radiobutton(tab2,value = 2,text = COLOR2,variable = radVar,command = radCall)
rad2.grid(column = 1,row = 5)

rad3 = tk.Radiobutton(tab2,value = 3,text=COLOR3,variable = radVar,command = radCall)
rad3.grid(column = 2,row = 5)

#adding scrolledtext field 
scrolW = 30
scrolH = 3
scr = scrolledtext.ScrolledText(tab2,width = scrolW,height = scrolH)
scr.grid(column = 0,columnspan = 3)

#creating labels
Laabel = ttk.LabelFrame(tab2,text = 'Labels')
Laabel.grid(column = 0,row = 9,columnspan = 3,padx = 50,pady = 30)
'''(padx) and (pady) are the two functionalities that allow us to add horizontal and vertical padding that makes our GUI look fantastic'''

ttk.Label(Laabel,text = 'Label1').grid(column = 0,row = 11)
ttk.Label(Laabel,text = 'Label2').grid(column = 0,row = 13)
ttk.Label(Laabel,text = 'Label3').grid(column = 0,row = 15)

tabControl.pack(fill = 'both',expand = 1)
win.mainloop()
