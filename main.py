import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from fileOperation import *
from rsa import *

def generate_key():
    p = entry_p.get()
    q = entry_q.get()
    e = entry_keypub.get()
    if (isPrima(p)==True and isPrima(q)==True):
        n = calculate_n(p,q)
        totion_n = calculate_totion_n(p, q)
        array_e = generatePossiblePublicKey(totion_n)

        while (e not in (array_e)):
            showinfo("Warning", "Nilai e tidak relatif prima dengan totion n.")
            entry_keypub.delete('1.0', END)
    #masukan ke texte entry kunci rahasia, kunci publik -> save

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
    n = int(content[1])
    return [key, n]

# WRITE SIGNATURE IN *.TXT
def addKeyInNewLine(filePath, text):
    try:
        f_in = open(filePath, 'r')
        lines = f_in.readlines()
        # Add a new line
        lines.append('\n')
        # Append the new paragraph as a new string to the end of the list
        lines.append('<ds>\n' + text + '\n</ds>')

        # Open the output file for writing
        f_out =  open(filePath, 'w')
        # Write the modified lines to the output file
        f_out.writelines(lines)
    except:
        raise(Exception(f'Failed to add digital signature in {filePath}'))

# WRITE SIGNATURE IN OTHER FILE (FOR BIN FILE)
def writeSignature(text):
    file_name = filedialog.asksaveasfile(initialdir = "/",
                                          title = "Save a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*"))).name
    try:
        f = open(file_name, 'w')
        f.write('<ds>\n' + text + '\n</ds>')
        f.close()
    except:
        raise(Exception('File not found and can not be opened:', file_name))


# Create the main window
root = tk.Tk()
root.title("Digital Signature")
root.geometry("700x400")

# Create a notebook widget with 2 tabs
notebook = ttk.Notebook(root)

# Create the first tab
## Create the first tab
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
tk.Label(tab1, text="This is Tab 1").pack(padx=20, pady=20)
notebook.add(tab1, text="Get Private & Public Key")
title1 = tk.Label(tab1, text="Generate Key", font= ('arial', 14))
title1.grid(row=0, column=0, padx=10, pady=10)

label_p = tk.Label(tab1, text = 'Enter your p:', font = ('Inter ', 12))#.pack(padx=20, pady=5)
label_p.grid(row=1, column=0, padx=10, pady=5)
prime_p = IntVar()
entry_p = tk.Entry(tab1, textvariable=prime_p,width = 30)#.pack(ipadx=20, ipady=10)
entry_p.grid(row=1, column=1, stick='w', padx=20, pady=5)

label_q = tk.Label(tab1, text = 'Enter your q:', font = ('Inter ', 12))#.pack(padx=20, pady=5)
label_q.grid(row=2, column=0, padx=10, pady=5)
prime_q = IntVar()
entry_q = tk.Entry(tab1, textvariable=prime_q, width = 30)#.pack(ipadx=20, ipady=10)
entry_q.grid(row=2, column=1, stick='w', padx=20, pady=5)

label_keypub = tk.Label(tab1, text = 'Enter your e (key public):', font = ('Inter ', 10))#.pack(padx=20, pady=5)
key_public = IntVar()
entry_keypub = tk.Entry(tab1, textvariable=key_public, width = 40)#.pack(ipadx=20, ipady=10)

btn_generate = tk.Button(tab1, height=1, width=15, text="Generate Your Key!",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=generate_key)#.pack(padx=15, pady=5)

#button_generate = tk.Button(tab1, text = )

# Create the second tab
## Create the second tab 
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")
tk.Label(tab2, text="This is Tab 2").pack(padx=20, pady=20)
notebook.add(tab2, text="Signing")
title2 = tk.Label(tab2, text="Signing", font=('arial', 15))#.pack(padx=20, pady=20)

# Create the third tab
## Create the third tab
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Tab 3")
tk.Label(tab3, text="This is Tab 3").pack(padx=20, pady=20)
notebook.add(tab3, text="Verifying")
title3 = tk.Label(tab3, text="Verifying", font=('arial', 15))#.pack(padx=20, pady=20)

# Pack the notebook widget and start the main loop
notebook.pack(expand=True, fill="both")