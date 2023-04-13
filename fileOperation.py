import os

# Operasi write dan read file
def readFile(filename):
    try:
        f = open(filename,"r")
        file_content = f.read()
        f.close()
        return file_content
    except:
        raise(Exception('File not found and can not be opened:', filename))

def writeFile(filename, text):
    try:
        f = open(filename, "w")
        f.write(text)
        f.close()
    except:
        raise(Exception('File not found and can not be opened:', filename))


def readBinaryFile(filename):
    try:
        f = open(filename,"rb")
        file_content = f.read()
        f.close()
        return file_content
    except:
        raise(Exception('File not found and can not be opened:', filename))
    

def writeBinaryFile(filename, text):
    try:
        f = open(filename, "wb")
        f.write(text)
        f.close()
    except:
        raise(Exception('File not found and can not be opened:', filename))
    
def getNameFromFilepath(filepath):
    filename = os.path.basename(filepath)
    name, extension = os.path.splitext(filename)
    return(name)