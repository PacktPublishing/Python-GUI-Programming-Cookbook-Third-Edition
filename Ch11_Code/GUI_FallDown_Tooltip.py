'''
Created on Jun 17, 2019
Chapter 11
@author: Burkhard
'''

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#===================================================================
class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)           # bind mouse events
        widget.bind('<Leave>', self.mouse_leave)

    def mouse_enter(self, _event):                       
        self.show_tooltip()
        
    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()                          # get widget top-left coordinates
            y_top = self.widget.winfo_rooty() - 18                      # place tooltip above widget or it flickers
            
            self.tip_window = tk.Toplevel(self.widget)                  # create Toplevel window; parent=widget
            self.tip_window.overrideredirect(True)                      # remove surrounding toolbar window
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))        # position tooltip 
    
            label = tk.Label(self.tip_window, text=self.tip_text, justify=tk.LEFT,
                          background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                          font=("tahoma", "8", "normal"))
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy() 
            
#===================================================================          


#======================
# Create instance
#======================
win = tk.Tk() 

#======================
# Add a title       
#====================== 
win.title("Python GUI")

#=========================
# Disable resizing the GUI
#=========================
win.resizable(0,0)

#===============================================================================
# Adding a LabelFrame, Textbox (Entry) and Combobox  
#===============================================================================
lFrame = ttk.LabelFrame(win, text="Python GUI Programming Cookbook")
lFrame.grid(column=0, row=0, sticky='WE', padx=10, pady=10)

#===============================================================================
# Labels
#===============================================================================
ttk.Label(lFrame, text="Enter a name:").grid(column=0, row=0)
ttk.Label(lFrame, text="Choose a number:").grid(column=1, row=0, sticky=tk.W)

#===============================================================================
# Buttons click command
#===============================================================================
def clickMe(name, number):
    messagebox.showinfo('Information Message Box', 'Hello ' + name + \
                        ', your number is: ' + number)
    
#===============================================================================
# Creating several controls in a loop
#===============================================================================
names         = ['name0', 'name1', 'name2']
nameEntries   = ['nameEntry0', 'nameEntry1', 'nameEntry2']

numbers       = ['number0', 'number1', 'number2']
numberEntries = ['numberEntry0', 'numberEntry1', 'numberEntry2']

buttons = []

for idx in range(3):
    names[idx] = tk.StringVar()
    nameEntries[idx] = ttk.Entry(lFrame, width=12, textvariable=names[idx])
    nameEntries[idx].grid(column=0, row=idx+1)
    nameEntries[idx].delete(0, tk.END)
    nameEntries[idx].insert(0, '<name>')

    numbers[idx] = tk.StringVar()
    numberEntries[idx] = ttk.Combobox(lFrame, width=14, textvariable=numbers[idx])
    numberEntries[idx]['values'] = (1+idx, 2+idx, 4+idx, 42+idx, 100+idx)
    numberEntries[idx].grid(column=1, row=idx+1)
    numberEntries[idx].current(0)
  
    button = ttk.Button(lFrame, text="Click Me "+str(idx+1), command=lambda idx=idx: clickMe(names[idx].get(), numbers[idx].get()))
    button.grid(column=2, row=idx+1, sticky=tk.W)  
    buttons.append(button)

    # Add Tooltips to more widgets
    ToolTip(nameEntries[idx], 'This is an Entry widget.') 
    ToolTip(numberEntries[idx], 'This is a DropDown widget.') 
    ToolTip(buttons[idx], 'This is a Button widget.') 

#======================
# Start GUI
#======================
win.mainloop()