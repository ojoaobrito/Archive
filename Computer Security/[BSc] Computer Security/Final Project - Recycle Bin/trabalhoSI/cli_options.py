
import os
import sys
import encryption as encc

__menu_name_of_file__ = os.getenv("HOME") + "/FALL-INTO-OBLIVION/.menuHelp.txt"
__standart_prefix_file__ = os.getenv("HOME") + "/FALL-INTO-OBLIVION/"
__data_ficheiros_encryptados__ = os.getenv("HOME") + "/FALL-INTO-OBLIVION/.data.txt"
__standart_prefix_command__ = __standart_prefix_file__ + ".COMMAND."

# Remove a name of the file in .data.txt
def update_list(del_me) :
    data_files = open(__data_ficheiros_encryptados__, "r").read().split("...\n")
    del data_files[len(data_files) - 1]

    os.remove(__data_ficheiros_encryptados__)

    fl_data = open(__data_ficheiros_encryptados__, "w")

    for line in data_files :
        aux = line.split(",,")
        if aux[0] != ( del_me ) : 
           fl_data.write(line + "...\n")
    fl_data.close()

# Find a file. return all the data from it
def find_me(lines, name) :
    for line in lines :
        ll = line.split(",,")
        if ll[0] == name :
            return ll
    return []


def list_encrypted_files() :
    try:
        data_files = open(__data_ficheiros_encryptados__, "r").read().split("...\n")
    except:
        return []
    
    files = []
    for i in data_files : files.append(i.split(",,")[0])
    del files[len(files) - 1]
    files.sort()
    return files
    
####
def print_menu() :
    menu_txt = open(__menu_name_of_file__, "r").readlines()
    for line in menu_txt :
        sys.stdout.write(line)
    sys.stdout.flush()

####
def printing_enc_files():
    print "\n---- Files inlisted ----\n"

    list = list_encrypted_files()
    for item in list :
        print "-->  " + item
        
    return

####
def enc(args) :
    def send_file(command_args_lst, name_of_file) :
        if name_of_file not in os.listdir(os.getcwd()) :
            print "-- File not found --"
            return
        try :
            old_file_lines = open(name_of_file, "r+").readlines()
            new_file = open(__standart_prefix_file__ + name_of_file, "w")
            #new_file_command = open(__standart_prefix_command__ + name_of_file, "w")
        except :
            print "\n---- Invalid File ----"
            return

        for line in old_file_lines :
            new_file.write(line)

        #for step in command_args_lst :
        #    new_file_command.write(step + " ")
        #new_file_command.write("\n")

        os.remove(name_of_file)
        new_file.close()
        #new_file_command.close()

    if args[1] not in os.listdir(os.getcwd()) :
        print "\n-- File not exists --\n"
    else :
        existent_files = list_encrypted_files()
        if args[1] in existent_files :
            print "\n---- There is already a file with that name ----\n"
        else :
            print "\n-- Sending file --\n"
            send_file(args, args[1])

####
def desc(args) :
    print "\n-- Scanning for File --\n"

    data_lines = open(__standart_prefix_file__ + ".data.txt", "r").read().split("...\n")
    for file in os.listdir(__standart_prefix_file__) :
        if file == ("." + args[1]) :
            tries_left = 3
            while(tries_left) :
                try :
                    print ("\n---> Tries left %d : ") % (tries_left)
                    pin = int(raw_input())
                    if pin > 10000 :
                        print "\n---- Invalid pin, pin must have 4 digits ----"
                        continue
                except KeyboardInterrupt :
                    print "\n---- Canceled ----"
                    return
                except:
                    print "\n---- Invalid Input----"
                    continue

                step = find_me(data_lines, args[1])
                if step == [] :
                    print "\n---- There is a error, file do not exists ----"
                    return

                msg = encc.outfile(str(pin), step[2], step[1], open(__standart_prefix_file__ + "." + step[0], "r").read())
                
                if msg != -1 and msg != -2 :
                    fl = open(args[1], "w")
                    fl.write(msg)
                    fl.close()
                    os.remove(__standart_prefix_file__ + "." + args[1])
                    update_list(args[1])
                    print "\n-- Decrypted successfully --\n"
                    return
            
                if msg == -1 :
                    print "\n--- File corrupted, File is being removed from the list ---\n"
                    os.remove(__standart_prefix_file__ + "." + args[1])
                    update_list(args[1])
                    return

                tries_left -= 1

            print "\n---- Tries exceded, File is being removed from the list ----\n"
            os.remove(__standart_prefix_file__ + "." + args[1])
            update_list(args[1])
            return

    print "\n-- File not found --\n"


def remove_file(nome, f) :
    list_info = find_me(open(__data_ficheiros_encryptados__, "r").read().split("...\n") ,nome)
    if list_info == [] :
        print "---- File don't exists ----"
        return
    os.remove(os.getenv("HOME") + "/FALL-INTO-OBLIVION/." + nome)
    update_list(nome)
    if f : print "\n---- File removed ----"

def remove_all() :
    list_files = os.listdir(__standart_prefix_file__)
    list_files.remove(".data.txt")
    list_files.remove(".sk.txt")
    list_files.remove(".pk.txt")
    list_files.remove(".sets.txt")
    list_files.remove(".menuHelp.txt")

    for i in list_files :
        if i[0] == "." :
            remove_file(i[1:], False)

    print "\n---- Folder cleared ----"