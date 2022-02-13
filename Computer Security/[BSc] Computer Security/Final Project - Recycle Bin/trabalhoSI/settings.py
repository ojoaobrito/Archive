#takes care os settings
import os

__settings_file_name__ = ".sets.txt"
__name_of_folder__ = "FALL-INTO-OBLIVION"
__file_set__ = os.getenv("HOME") + "/FALL-INTO-OBLIVION/.sets.txt"

#TODO:
#1.add more settings
def create_setting() :
    settings = open(__settings_file_name__, "w")
    settings.write("time,10")

    settings.close()

# Open settings file, and put the settigns in a form of dictionary
def import_settings() :
    sets = {}
    preSettings = open(__file_set__, "r").readlines()
    for set in preSettings :
        s = set.split(",")
        sets.update({s[0]:s[1]})
    return sets


def change_time(sec) :
    sett = open(__file_set__, "r").readlines()
    os.remove(__file_set__)
    new_sets = open(__file_set__, "w")
    for item in sett :
        if "time" == item.split(",")[0] :
            new_sets.write("time," + str(sec))
        else :
            new_sets.write(item)

    print "\n----> Setting Changed\n"