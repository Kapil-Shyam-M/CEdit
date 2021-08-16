#!/usr/bin/python3.8

#########################################################################
#  Project           		:   CEDIT-A PYTHON BASED TEXT EDITOR
#  Name of the file	     	:   ceterm.py
#  Brief Description of file   :   Terminal module File for CEdit
#  Name                        :   KAPIL SHYAM.M 
#  Email ID                    :   cedit.ceo@gmail.com
#                                                                       #
#                                                                       #
#########################################################################


import tkinter as tk
from tkterminal import Terminal

def exit_terminal(event=None):
    if tk.messagebox.askokcancel("Quit?", "Do you want to QUIT from Terminal for sure?\n"):
        root.destroy()
        

def ceterm():
    root = tk.Tk()
    root.title("CEdit Terminal")           
    terminal = Terminal(root, background='#360940', foreground='white', pady=5, padx=5)
    terminal.basename="CE-terminal$"
    terminal.tag_config("basename", foreground="#97ABFF")
    terminal.pack(expand=True, fill='both')
    terminal.shell = True
    root.mainloop()
