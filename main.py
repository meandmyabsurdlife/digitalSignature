from tkinter import filedialog
from fileOperation import *

# SAVE KEY
def save_key(e, n):
    file_name = filedialog.asksaveasfile(defaultextension=".pub",
                                         filetypes=[('Public Key', '*.pub'),
                                                    ('Private Key', '*.pri')]).name
    try:
        f = open(file_name, 'w')
        f.write('(' + str(e) + ',' + str(n) + ')')
        f.close()
    except:
        raise(Exception('File not found and can not be opened:', file_name))

# LOAD KEY
def load_key():
    filename = filedialog.askopenfilename(defaultextension=".pub",
                                         filetypes=[('Public Key', '*.pub'),
                                                    ('Private Key', '*.pri')])
      
    # Change label contents
    content = readFile(filename)

    content = content.strip('()').split(',')
    
    key = int(content[0])
    #print(key)
    #print(type(key))
    n = int(content[1])
    return [key, n]

# WRITE SIGNATURE IN *.TXT
def addKeyInNewLine(filename, text):
    try:
        f_in = open(filename, 'r')
        lines = f_in.readlines()
        # Add a new line
        lines.append('\n')
        # Append the new paragraph as a new string to the end of the list
        lines.append('<ds>\n' + text + '\n</ds>')

        # Open the output file for writing
        f_out =  open(filename, 'w')
        # Write the modified lines to the output file
        f_out.writelines(lines)
    except:
        raise(Exception(f'Failed to add digital signature in {filename}'))



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
