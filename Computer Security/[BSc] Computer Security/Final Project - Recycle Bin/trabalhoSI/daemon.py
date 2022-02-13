import os
import sys
import rsa
import random
import time as tp
import encryption as encc
import settings as sett
from Crypto.PublicKey import RSA 

__menu_name_of_file__ = ".menuHelp.txt"
__name_of_folder__ = "FALL-INTO-OBLIVION"

def generate_keys() :
        new_key = RSA.generate(1024) 

        open(".sk.txt","w").write(new_key.exportKey("PEM"))
        open(".pk.txt","w").write(new_key.publickey().exportKey("PEM"))

def create_menu () :
    menu_txt = open(__menu_name_of_file__, "w")
    menu_txt.write("FALL-INTO-OBLIVION's help guide:\n\n")
    menu_txt.write("This programs work like the avereage recicly bin... But with cryptography method\n\n")
    menu_txt.write("- enc [FILE-NAME]    : encrypt the file, removes the original, and send it to the FALL-INTO-OBLIVION folder\n\n")
    menu_txt.write("- dec [FILE-NAME]    : decrypt the file in the bin and moves it to the current folder. It will ask for a pin. After 3 wrong tries the file is removed permanently\n\n")
    menu_txt.write("- list               : shows the list of all the encrypted files in the bin\n\n")
    menu_txt.write("- time               : shows the period of the deamon cicle\n\n")
    menu_txt.write("- ch time            : option to change the period\n\n")
    menu_txt.write("- rm [FILE-NAME]     : remove the file from the folder permanently\n\n")
    menu_txt.write("- rm all             : remove all the files in the folder\n\n")
    menu_txt.write("- exit               : exits the shell\n\n")

def __initiliaze_daemon__ () :
    try :
        while(True) :
            lst_files = os.listdir(os.getcwd())
            settings = sett.import_settings()

            for name in lst_files :
                if name[0] != '.' :
                    pin = int(random.random() * 10000)
                    print "\n---- " + name + " : " + str(pin) + " ----"
                    (hs, enc, sign) = encc.putfile(name, str(pin))
                    open("." + name, "w").write(enc)
                    open(".data.txt", "a").write(name + ",," + hs + ",," + sign + "...\n")
                    os.remove(name)

            tp.sleep(float(settings["time"]))
    except KeyboardInterrupt :
        print "\nDaemon Finished"

def __manage_folders__ () :
    os.chdir(os.getenv("HOME"))
    lstdir = os.listdir(os.getcwd())

    if sett.__name_of_folder__ not in lstdir :
        os.mkdir(__name_of_folder__)
        os.chdir(os.getenv("HOME") + "/" + __name_of_folder__)
        sett.create_setting()
        #create record of files
        open(".data.txt", "w")
        create_menu()
        generate_keys()
    else :
        os.chdir(os.getenv("HOME") + "/" + __name_of_folder__)

def __main__ () :
    __manage_folders__ ()
    __initiliaze_daemon__ ()


__main__ ()