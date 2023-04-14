from tkinter import *
from tkinter import filedialog
from tkinter.messagebox import showinfo
from fileOperation import *
from rsa import *
from signing import *
from verifiying import *

##-------------------------------FUNGSI REUSABLE-------------------------------------------- 
def browse_file(label):
    # ambil path
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                        ("JPG files",
                                                        "*.jpg*"),
                                                        ("JPEG files",
                                                        "*.jpeg*"),
                                                       ("all files",
                                                        "*.*"),
                                                        ))
      
    # Change label contents
    label.insert(END, filename)
    return(filename)

def browse_key(label):
    filename = filedialog.askopenfilename(defaultextension=".pub",
                                         filetypes=[('Public Key', '*.pub'),
                                                    ('Private Key', '*.pri')])
    # show directory
    label.insert(END, filename)
      
def read_key(filename):
    # Change label contents
    content = readFile(filename)

    content = content.strip('()').split(',')
    
    key = int(content[0])
    n = int(content[1])
    return [key, n]

##-------------------------------FUNGSI Tab 1 (GENERATE KEY)-------------------------------- 
# GENERATE KEY
def generate_pub_key():
    p = entry_p.get()
    q = entry_q.get()

    p = int(p)
    q = int(q)
    
    if (isPrima(p) and isPrima(q)):
        # tambahin apakah p = q
        # display n
        n = calculate_n(p,q)
        display_n.config(text=n)

        totion_n = calculate_totion_n(p, q)

        array_e = generatePossiblePublicKey(totion_n)
        entry_e_array.insert(END, str(array_e))
    elif (p == 0 or q == 0):
        showinfo("Warning", "p dan q tidak boleh 0")
    elif ((isPrima(p) == False) or (isPrima(q) == False)):
        showinfo("Warning", "p atau q bukan prima")
    elif (p == q):
        showinfo("Warning", "p tidak boleh sama dengan q")
    
def generate_pri_key():
    p = entry_p.get()
    q = entry_q.get()

    public_key = int(entry_keypub.get())
    totion_n = calculate_totion_n(int(p), int(q))
    print(totion_n)

    if (public_key == 0):
        showinfo("Warning", "public key tidak boleh kosong")
    else:
        public_key = int(public_key)
        private_key = generatePrivateKey(public_key, totion_n)
        display_keypri.config(text=private_key)

# SAVE KEY
def save_pub_key():
    public_key = int(entry_keypub.get())
    n = int(display_n.cget('text'))
    save_key(public_key, n)

def save_pri_key():
    private_key = int(display_keypri.cget('text'))
    n = int(display_n.cget('text'))
    save_key(private_key, n)

def save_key(key, n):
    file_name = filedialog.asksaveasfile(defaultextension=".pub",
                                         filetypes=[('Public Key', '*.pub'),
                                                    ('Private Key', '*.pri')]).name
    try:
        f = open(file_name, 'w')
        f.write('(' + str(key) + ',' + str(n) + ')')
        f.close()
        showinfo("Info", "Key berhasil disimpan")
    except:
        raise(Exception('File not found and can not be opened:', file_name))

##-------------------------------FUNGSI Tab 2 (SIGNING)-------------------------------- 
# BROWSE FILE
def browse_signing_file():
    browse_file(entry_signing_file)

# LOAD KEY
def browse_signing_keypri_file():
    browse_key(entry_signing_keypri_file)

# SIGNING
def sign():
    filePath = entry_signing_file.get()

    key = read_key(entry_signing_keypri_file.get())
    private_key = key[0]
    n =key[1]

    if (sign_mode.get() == "*.txt file"):
        if(findSignature(filePath) == None):
            sign_Text(filePath, private_key, n)
            showinfo("Info", "Digital signature has added in the of file")
        else:
            showinfo("Warning", f'File {filePath} has already had a signature')

    elif (sign_mode.get() == "other file"):
        signature_filename = getNameFromFilepath(filePath)

        sign_Binary(filePath, private_key, n)
        showinfo("Info", f"Tanda tangan tersimpan di /outputFile/{signature_filename}.txt")

##-------------------------------FUNGSI Tab 3 (VERIFYING)-------------------------------- 
# KEY & FILE
def browse_verifying_file():
    browse_file(entry_verifying_file)

def browse_verifying_signature_file():
    browse_file(entry_verifying_signature)

def browse_verifying_keypri_file():
    browse_key(entry_verifying_keypri_file)

def browse_verifying_keypub_file():
    browse_key(entry_verifying_keypub_file)

# VERIFYING
def verify():
    filePath = entry_verifying_file.get()
    signaturePath = entry_verifying_signature.get()

    pub_key = read_key(entry_verifying_keypub_file.get())
    public_key = pub_key[0]
    n_public = pub_key[1]

    pri_key = read_key(entry_verifying_keypri_file.get())
    private_key = pri_key[0]
    n_private = pri_key[1]

    if (n_private == n_public):
        if (verify_mode.get() == "*.txt file"):
            if(findSignature(filePath) != None):
                isValid = verify_text(filePath, public_key, n_private, n_public)
                if (isValid):
                    showinfo("Info", "Tanda tangan valid")
                else:
                    showinfo("Info", "Terdapat perubahan pada file !")

            else:
                showinfo("Warning", f'File {filePath} belum ditandatangani')

        elif (verify_mode.get() == "other file"):
            if(findSignature(signaturePath) != None): # jika file txt yg dimasukkan ada signature
                isValid = verify_BinFile(filePath, signaturePath, public_key, private_key, n_private, n_public)
                if (isValid):
                    showinfo("Sukses", "Tanda tangan valid")
                else:
                    showinfo("Gagal", f"File {filePath} dan tanda  {signaturePath} tidak valid !")
            else:
                showinfo("Gagal", f"File tanda tangan {signaturePath} kosong !")
    else:
        showinfo("Info", "Kunci publik dan kunci privat tidak berpadanan")



import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Digital Signature")
root.geometry("700x400")

# Create a notebook widget with 3 tabs
notebook = ttk.Notebook(root)

##-------------------------------Tab 1 (GENERATE KEY)-------------------------------- 
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Get Private & Public Key")
title1 = tk.Label(tab1, text="Generate Key", font= ('arial', 12))
title1.grid(row=0, column=0, padx=10, pady=10)
# entry p
label_p = tk.Label(tab1, text = 'Enter p:', font = ('Inter ', 10))#.pack(padx=20, pady=5)
label_p.grid(row=1, column=0, padx=10, pady=5, stick='e')
prime_p = IntVar()
entry_p = tk.Entry(tab1, textvariable=prime_p,width = 40)#.pack(ipadx=20, ipady=10)
entry_p.grid(row=1, column=1, stick='w', padx=20, pady=5)
# entry q
label_q = tk.Label(tab1, text = 'Enter q :', font = ('Inter ', 10))#.pack(padx=20, pady=5)
label_q.grid(row=2, column=0, padx=10, pady=5, stick='e')
prime_q = IntVar()
entry_q = tk.Entry(tab1, textvariable=prime_q, width = 40)#.pack(ipadx=20, ipady=10)
entry_q.grid(row=2, column=1, stick='w', padx=20, pady=5)
# display n
label_n = tk.Label(tab1, text = 'n :', font = ('Inter ', 10))
label_n.grid(row=3, column=0, padx=10, pady=5, stick='e')
display_n = tk.Label(tab1, text="")
display_n.grid(row=3, column=1, stick='w', padx=20, pady=5)
# display possible e array
label_e_array = tk.Label(tab1, text = 'Possible public key (e) :', font = ('Inter ', 10))
label_e_array.grid(row=4, column=0, stick='e', padx=20, pady=5)
entry_e_array = tk.Entry(tab1, text="", width = 40)
entry_e_array.grid(row=4, column=1, stick='w', padx=20, pady=5)
# entry e (public key)
label_keypub = tk.Label(tab1, text = 'Enter public key (e) :', font = ('Inter ', 10))#.pack(padx=20, pady=5)
label_keypub.grid(row=5, column=0,padx=10, pady=5, stick='e')
key_public = IntVar()
entry_keypub = tk.Entry(tab1, textvariable=key_public, width = 40)#.pack(ipadx=20, ipady=10)
entry_keypub.grid(row=5, column=1, stick='w', padx=20, pady=5)
# display d (private key)
label_keypri = tk.Label(tab1, text = 'Private key (d) :', font = ('Inter ', 10))
label_keypri.grid(row=6, column=0, padx=10, pady=5, stick='e')
display_keypri = tk.Label(tab1, text="")
display_keypri.grid(row=6, column=1, stick='w', padx=20, pady=5)
# generate public key button
btn_generate_pub_key = tk.Button(tab1, height=1, width=15, text="Generate Public Key!",  font = ('arial ', 10), fg="black", bg="#D3C3B1", 
                                 command=generate_pub_key)
btn_generate_pub_key.grid(row=2, column=2, pady=2)
# generate private key button
btn_generate_pri_key = tk.Button(tab1, height=1, width=15, text="Generate Private Key!",  font = ('arial ', 10), fg="black", bg="#D3C3B1", 
                                 command=generate_pri_key)
btn_generate_pri_key.grid(row=5, column=2, pady=2)
# save public key button
btn_save_pub_key = tk.Button(tab1, height=1, width=15, text="Save Public Key",  font = ('arial ', 10), fg="black", bg="#D3C3B1", 
                             command=save_pub_key)
btn_save_pub_key.grid(row=3, column=2, pady=2)
# save private key button
btn_save_pri_key = tk.Button(tab1, height=1, width=15, text="Save Private Key",  font = ('arial ', 10), fg="black", bg="#D3C3B1", 
                             command=save_pri_key)
btn_save_pri_key.grid(row=6, column=2, pady=2)


##-------------------------------Tab 2 (SIGNING)-------------------------------- 
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Signing")
title2 = tk.Label(tab2, text="Signing", font=('arial', 15))
# entry file
label_signing_file = tk.Label(tab2, text = 'File : ', font = ('Inter ', 10))
label_signing_file.grid(row=1, column=0, padx=10, pady=5, stick='e')
entry_signing_file = tk.Entry(tab2, width = 30)
entry_signing_file.grid(row=1, column=1, stick='w', padx=20, pady=5)
# entry private key file
label_signing_keypri_file = tk.Label(tab2, text = 'Private key file  :', font = ('Inter ', 10))
label_signing_keypri_file.grid(row=2, column=0, padx=10, pady=5, stick='e')
entry_signing_keypri_file = tk.Entry(tab2, width = 30)#.pack(ipadx=20, ipady=10)
entry_signing_keypri_file.grid(row=2, column=1, stick='w', padx=20, pady=5)
# browse file button
btn_signing_browse_file = tk.Button(tab2, height=1, width=15, text="Browse file",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=browse_signing_file)#.pack(padx=15, pady=5)
btn_signing_browse_file.grid(row=1, column=2, pady=2)
# browse private key button
btn_browse_pri_key = tk.Button(tab2, height=1, width=15, text="Browse private key",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=browse_signing_keypri_file)#.pack(padx=15, pady=5)
btn_browse_pri_key.grid(row=2, column=2, pady=2)
# radio button
sign_mode = tk.StringVar()
sign_mode.set("*.txt file") # set default setting
radio_button_textFile = tk.Radiobutton(tab2, text="*.txt file", variable=sign_mode, value="*.txt file")
radio_button_textFile.grid(row=3, column=0, stick='w', padx=20, pady=5)
radio_button_binFile = tk.Radiobutton(tab2, text="other file", variable=sign_mode, value="other file")
radio_button_binFile.grid(row=3, column=1, stick='w', padx=20, pady=5)
# sign button
btn_signing = tk.Button(tab2, height=1, width=15, text="Sign",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=sign)#.pack(padx=15, pady=5)
btn_signing.grid(row=4, column=1, pady=2)


##-------------------------------Tab 3 (VERIFYING)--------------------------------
tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Verifying")
title3 = tk.Label(tab3, text="Verifying", font=('arial', 15))#.pack(padx=20, pady=20)
# entry file
label_verifying_file = tk.Label(tab3, text = 'File : ', font = ('Inter ', 10))
label_verifying_file.grid(row=1, column=0, padx=10, pady=5, stick='e')
entry_verifying_file = tk.Entry(tab3, width = 30)
entry_verifying_file.grid(row=1, column=1, stick='w', padx=20, pady=5)
# entry signature file
label_verifying_signature = tk.Label(tab3, text = 'Signature file  :', font = ('Inter ', 10))
label_verifying_signature.grid(row=2, column=0, padx=10, pady=5, stick='e')
entry_verifying_signature = tk.Entry(tab3, width = 30)#.pack(ipadx=20, ipady=10)
entry_verifying_signature.grid(row=2, column=1, stick='w', padx=20, pady=5)
# entry public key file
label_verifying_keypub_file = tk.Label(tab3, text = 'Public key file  :', font = ('Inter ', 10))
label_verifying_keypub_file.grid(row=3, column=0, padx=10, pady=5, stick='e')
entry_verifying_keypub_file = tk.Entry(tab3, width = 30)#.pack(ipadx=20, ipady=10)
entry_verifying_keypub_file.grid(row=3, column=1, stick='w', padx=20, pady=5)
# entry private key file
label_verifying_keypri_file = tk.Label(tab3, text = 'Private key file  :', font = ('Inter ', 10))
label_verifying_keypri_file.grid(row=4, column=0, padx=10, pady=5, stick='e')
entry_verifying_keypri_file = tk.Entry(tab3, width = 30)#.pack(ipadx=20, ipady=10)
entry_verifying_keypri_file.grid(row=4, column=1, stick='w', padx=20, pady=5)

# browse file button
btn_verifying_browse_file = tk.Button(tab3, height=1, width=15, text="Browse file",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=browse_verifying_file)
btn_verifying_browse_file.grid(row=1, column=2, pady=2)
# browse signature button
btn_verifying_browse_signature = tk.Button(tab3, height=1, width=15, text="Browse signature",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=browse_verifying_signature_file)
btn_verifying_browse_signature.grid(row=2, column=2, pady=2)
# browse pub key button
btn_verifying_browse_pub_key = tk.Button(tab3, height=1, width=15, text="Browse public key",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=browse_verifying_keypub_file)
btn_verifying_browse_pub_key.grid(row=3, column=2, pady=2)
# browse pri key button
btn_verifying_browse_pri_key = tk.Button(tab3, height=1, width=15, text="Browse private key",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=browse_verifying_keypri_file)
btn_verifying_browse_pri_key.grid(row=4, column=2, pady=2)

# radio button
verify_mode = tk.StringVar()
verify_mode.set("*.txt file") # set default setting
verifying_radio_button_textFile = tk.Radiobutton(tab3, text="*.txt file", variable=verify_mode, value="*.txt file")
verifying_radio_button_textFile.grid(row=5, column=0, stick='w', padx=20, pady=5)
verifying_radio_button_binFile = tk.Radiobutton(tab3, text="other file", variable=verify_mode, value="other file")
verifying_radio_button_binFile.grid(row=5, column=1, stick='w', padx=20, pady=5)
# sign button
btn_verifying = tk.Button(tab3, height=1, width=15, text="Verify",  font = ('arial ', 10), fg="black", bg="#D3C3B1", command=verify)
btn_verifying.grid(row=6, column=1, pady=2)

# Pack the notebook widget and start the main loop
notebook.pack(expand=True, fill="both")
root.mainloop()