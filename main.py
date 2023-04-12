from tkinter import filedialog
from fileOperation import *

# SAVE KEY
def save_public_key(e, n):
    file_name = filedialog.asksaveasfile(initialdir = '/',
                                          title = 'Save a File',
                                          filetypes = (('pub',
                                                        '*.pub*'))).name
    try:
        f = open(file_name, 'w')
        f.write('(' + str(e) + ',' + str(n) + ')')
        f.close()
    except:
        raise(Exception('File not found and can not be opened:', file_name))
    
def save_private_key(d, n):
    file_name = filedialog.asksaveasfile(initialdir = '/',
                                          title = 'Save a File',
                                          filetypes = (('pri',
                                                        '*.pri*'))).name
    try:
        f = open(file_name, 'w')
        f.write('(' + str(d) + ',' + str(n) + ')')
        f.close()
    except:
        raise(Exception('File not found and can not be opened:', file_name))

# LOAD KEY

# WRITE SIGNATURE
def write_Text_signature(filename, signature):
    writeFile(filename, signature)



import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Digital Signature")

# Create a notebook widget with 2 tabs
notebook = ttk.Notebook(root)

# Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
tk.Label(tab1, text="This is Tab 1").pack(padx=20, pady=20)

# Create the second tab
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")
tk.Label(tab2, text="This is Tab 2").pack(padx=20, pady=20)

# Create the third tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Tab 3")
tk.Label(tab3, text="This is Tab 3").pack(padx=20, pady=20)

# Pack the notebook widget and start the main loop
notebook.pack(expand=True, fill="both")
root.mainloop()
