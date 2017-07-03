from Crypto.Cipher import AES
from Crypto.Hash import SHA256
import random
import base64
from Crypto import Random
import os

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]

def encrypt(text, key):

    key = SHA256.new(key).digest()
    text = pad(text)
    IV = Random.new().read( AES.block_size )
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    ciphertext = encryptor.encrypt(text)
    
    return base64.b64encode(IV+ciphertext)

def decrypt(text, key):
    key = SHA256.new(key).digest()
    
    text=base64.b64decode(text)
    
    IV = text[:16]
        
    decryptor = AES.new(key, AES.MODE_CBC, IV)

    deciphertext = unpad(decryptor.decrypt(text[16:]))

    return deciphertext



