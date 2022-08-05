#!/bin/bash/env python3

from tkinter import *
from tkinter import ttk
from sysmon_Parse import sysmon_Parse
import sys

#Create an instance of Tkinter frame
win = Tk()
win.title('')

#Set the geometry of Tkinter frame
win.geometry("1000x400")
file = sys.argv[1]
is_opened = False

def switchButtonState():
   #print('got invoked!')
   button1.config(state=DISABLED)

# close popup window
def close_win():
   win.destroy()

# open popup window
def open_popup():

   switchButtonState()
   popup_frame = Frame(win)
   popup_frame.pack()

   # setup scrollbar (horizontal)
   popup_scroll = Scrollbar(popup_frame,orient='horizontal')
   popup_scroll.pack(side= BOTTOM,fill=X)

   my_popup = ttk.Treeview(popup_frame, xscrollcommand =popup_scroll.set)
   my_popup.pack()
   popup_scroll.config(command=my_popup.xview)
   
   #define column
   my_popup['columns'] = ('Timestamp', 'Details')
   
   # format column
   my_popup.column("#0", width=0,  stretch=NO)
   my_popup.column("Timestamp",anchor='w', width=150)
   my_popup.column("Details",anchor='w',width=10000)

   #Create Headings
   my_popup.heading("Timestamp",text="Timestamp",anchor=W)
   my_popup.heading("Details",text="Details",anchor=W)

   
   #add data 
   data = sysmon_Parse(file)

   for index, list in enumerate(data):
      # date, details in order
      my_popup.insert(parent='',index='end',iid=index,text='', values=(list[0], list[1]))
   
   my_popup.pack()


#Edit this label depending on what you are searching for (from sysmon_Parse.py)
Label(win, text=f"There are {len(sysmon_Parse(file))} possible IOC Found: CVE-2022-30190 (Follina)", font=('Helvetica 14 bold')).pack(pady=20)

#Create a button in the main Window to open the popup
button1 = Button(win, text= "Show Me", command=open_popup, state=ACTIVE)
button1.pack()
print(button1)
button2 = Button(win, text= "Close", command=close_win).pack()


win.mainloop()