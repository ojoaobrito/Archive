import os
import sys
import encryption as encc
import cli_options as cliOpt
import settings

def menu(args) :
    
    if len(args) > 0 :
        if (args[0] == "help") :
            print ""
            cliOpt.print_menu ()
            return

        if (args[0] == "list") :
            cliOpt.printing_enc_files()
            return

        if (args[0] == "exit") :
            exit(0)

        if (args[0] == "time") :
            sett = settings.import_settings()
            print "\n----> Time: " + sett["time"]
            return

        if len(args) == 1 :
            if args[0] == "enc" :
                print "\n---- Incomplete Command -----"
                print "\n----  enc [FILE_NAME] ----"
                return

            if args[0] == "dec" :
                print "\n---- Incomplete Command -----"
                print "\n----  des [FILE_NAME] ----"
                return

            if args[0] == "rm" :
                print "\n---- Incomplete Command          ----"
                print "\n---- Remove File: rm [FILE_NAME] ----"
                print "\n---- Remove All Files: rm all    ----"
                return

    if len(args) > 1 :
        if (args[0] == "enc") :
            cliOpt.enc(args)
            return

        if (args[0] == "dec") :
            cliOpt.desc(args)
            return

        if (args[0] == "ch" and args[1] == "time") :
            sec = int(raw_input("\n----> Insert new time sec: "))
            settings.change_time(sec)

        if (args[0] == "rm") :
            if args[1] == "all" : 
                cliOpt.remove_all()
            else :
                cliOpt.remove_file(args[1], True)

            return
    
    print "\n---- Invalid command ----"

def __main__ () :

    if len(sys.argv) > 1 :
        menu(sys.argv[1:])
        exit(1)

    while(True) :
        try :
            args = raw_input("\n----> Enter you command <----\n\n>> ").strip().split(" ")
        except KeyboardInterrupt :
            print "\n... Closing ..."
            sys.exit(1)

        menu(args)

__main__ ()