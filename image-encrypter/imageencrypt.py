import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import vigenerecipher as vc

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

def mainfilename(filename):
    mainf = ''

    filename = filename[-1:-len(filename)-1:-1]

    while '/' not in mainf:
        mainf += filename[0]
        filename = filename[1::]

    

    direc = filename[-1:-len(filename)-1:-1]

    fi = mainf.rstrip(mainf[-1])
    extension = ''

    while '.' not in extension:
        extension += fi[0]
        fi = fi[1::]
    
    fi = fi[-1:-len(fi)-1:-1]
    extension = extension[-1:-len(extension)-1:-1]

    return fi, extension, direc

def encrypt(key, filename, keeporg = True):
    chunk_size = 64*1024
    fil = mainfilename(filename)
    output_file = fil[2]+'/'+vc.cipher(fil[0], key)+fil[1]+".enc"
    key = getKey(key)
    file_size = str(os.path.getsize(filename)).zfill(16)
    IV = ''
    for i in range(16):
        IV += chr(random.randint(0, 0xFF))
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    with open(filename, 'rb') as inputfile:
        with open(output_file, 'wb') as outf:
            outf.write(file_size)
            outf.write(IV)
            while True:
                chunk = inputfile.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                   chunk += ' '*(16 - len(chunk)%16)
                outf.write(encryptor.encrypt(chunk))
    if not keeporg:
        os.remove(filename)
 
def decrypt(key, filename):
    chunk_size = 64*1024
    fil = mainfilename(filename[:-4])
    output_file = fil[2]+'/'+vc.decipher(fil[0], key)+fil[1]
    key = getKey(key)
    with open(filename, 'rb') as inf:
        filesize = long(inf.read(16))
        IV = inf.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        with open(output_file, 'wb') as outf:
            while True:
                chunk = inf.read(chunk_size)
                if len(chunk)==0:
                    break
                outf.write(decryptor.decrypt(chunk))
            outf.truncate(filesize)


 
