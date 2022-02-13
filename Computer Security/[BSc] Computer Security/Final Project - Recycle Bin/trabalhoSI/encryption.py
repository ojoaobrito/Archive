#encoding: utf-8

import os, rsa, hashlib
from textwrap import wrap
from Crypto.PublicKey import RSA 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#key=hash(pin)

__standart_prefix_file__ = os.getenv("HOME") + "/FALL-INTO-OBLIVION/"

def fillFile(f):
    str1 = ""
 
    while f:
        x = f.read(16)
        if(len(x) == 16): str1 = str1 + x
        else:
            i = 16 - len(x)
            for j in range(i): x = x + 'i'
            str1 = str1 + x
            break
 
    if(i > 9): str1 = str1 + '00000000000000' + str(i)
    else: str1 = str1 + '000000000000000' + str(i)
 
    return(str1)
 

def cleanfile(file):
    str1 = ""

    while file:
        x = file.read(16)
        if len(x)==16:
            str1=str1 + x
        else:
            try:
                num=int(str1[len(str1)-16:len(str1)])
                break
            except:
                return (-1) 

    return (str1[0:len(str1)-16-num])


def hash(text):
    hs = hashlib.md5()
    hs.update(text)
    hss = hs.hexdigest()
    return hss

def putfile(file,pin):
    ficheiro = open(file,"r")
    hash_original = hash(ficheiro.read())
    ficheiro.close()

    ficheiro = open(file,"r")
    mensagem = fillFile(ficheiro)

    encrypt = cipher(hash(pin),mensagem)
    (private_key,public_key) = getkey()
    
    return(hash_original, encrypt, sign(encrypt,private_key))

# Decrypted MSG: retorna texto se n der erro, caso contrario, tem o pin o errado
def outfile(pin, signature, hashoriginal, crypt):
    (private_key,public_key)=getkey()

    ver= verify(crypt,public_key,signature)
    #if not ver :
    #    print "---- File corrupted, removing it... ----"
    #    return -1
    try :
        decrypttext=decipher(hash(pin),crypt)
        open("tmp","w").write(decrypttext)
    except :
        return -1

    decrypttext=cleanfile(open("tmp","r"))#Limpar blocos
    os.remove("tmp")

    #print decrypttext
    if decrypttext == -1 :
        print "\n---- Wrong Pin ----"
        return -2
    
    hash1=hash(decrypttext)
    
    if(hashoriginal != hash1 ) :
        print "\n---- Wrong Pin -----"
        return -2

    if decrypttext != -1 and not ver :
        return -1

    return(decrypttext)


# Return Cypher Text
def cipher(key, mensagem):
    cipher = Cipher(algorithms.AES(key), modes.CBC('0000000000000000'), backend = default_backend() )   
    encryptor = cipher.encryptor()
    
    ct = encryptor.update(mensagem) + encryptor.finalize()
    
    return ct

# Return Plain Text
def decipher(key, crypt):
    cipher = Cipher(algorithms.AES(key), modes.CBC('0000000000000000'), backend = default_backend() ) 
    decryptor = cipher.decryptor()

    try: 
        dct = decryptor.update(crypt) + decryptor.finalize()
    except:
        return -1
    return dct


def sign(file,private_key) :
    return rsa.sign(file, private_key, 'SHA-256')


def verify(mensagem,public_key,signature):
    try: 
        ver=rsa.verify(mensagem,signature,public_key)
        return True
    except:
        return False 


def getkey():
    public_key1 = rsa.PublicKey.load_pkcs1_openssl_pem( open(__standart_prefix_file__ + ".pk.txt", "r").read() )     
    private_key1 =rsa.PrivateKey.load_pkcs1( open(__standart_prefix_file__  + ".sk.txt", "r").read()  )
    
    return (private_key1,public_key1)





#(hash1,enc,sign)=putfile("teste.txt","1234")
#(decrypt)=outfile("1234",sign,hash1,enc+" ")
#print decrypt
