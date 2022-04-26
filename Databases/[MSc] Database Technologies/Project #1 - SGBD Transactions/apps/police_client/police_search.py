# import kivy stuff
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# import utilities
from client import get_query_result
from subprocess import Popen, PIPE
import sys

from kivy.config import Config
Config.set('graphics', 'height', '700')

class PoliceSearch(Widget):

    text_id_search = ObjectProperty(None)
    text_concelho_search = ObjectProperty(None)
    text_accident_description_value = ObjectProperty(None)
    text_accident_location_value = ObjectProperty(None)
    text_accident_timestamp_value = ObjectProperty(None)

    # new variables
    severely_number = "0"
    casualty_number = "0"
    erro = 0

    # old variables
    ID = ""
    description_old = ""
    location_id_old = -1
    location_text_old = ""
    timestamp_old = ""
    severely_old = -1
    casualties_old = -1
    km_old = -1

    def id_search(self):

        if(self.text_id_search.text==""):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

        else:
            self.ID = self.text_id_search.text

            # retireve our results
            results_list = get_query_result("SELECT * FROM acidentes WHERE IdAcidente=" + self.ID + ";") # format = [(IdAcidente, DataHora, IdVia, Natureza, Km, Mortos, FeridosGraves)]
            print("RESULTS")
            print(results_list)
            # Description
            # ---------------------------------------------------------------------------------------------------------------------
            self.text_accident_description_value.text = results_list[0][3]
            self.description_old = results_list[0][3]
            # ---------------------------------------------------------------------------------------------------------------------

            # Location
            # ---------------------------------------------------------------------------------------------------------------------
            location = get_query_result("SELECT IdVia, Nome FROM Vias Where IdVia = (SELECT IdVia FROM Acidentes Where IdAcidente = " + self.ID + ");")
            self.location_id_old = location[0][0]
            self.location_text_old = location[0][1]
            self.text_accident_location_value.text = location[0][1]
            # ---------------------------------------------------------------------------------------------------------------------

            # KM
            # ---------------------------------------------------------------------------------------------------------------------
            self.text_accident_km_value.text = str(results_list[0][4])
            self.km_old = int(results_list[0][4])
            # ---------------------------------------------------------------------------------------------------------------------

            # Date and Time
            # -----------------------------------------------------------
            # Date
            year = str(results_list[0][1]).split(" ")[0].split("-")[0]
            month = str(results_list[0][1]).split(" ")[0].split("-")[1]
            day = str(results_list[0][1]).split(" ")[0].split("-")[2]

            date = day + "/" + month + "/" + year + " "

            # Time
            hour = str(results_list[0][1]).split(" ")[1].split(":")[0]
            minutes = str(results_list[0][1]).split(" ")[1].split(":")[1]

            time = hour + ":" + minutes
            self.timestamp_old = year + "/" + month + "/" + day + " " + hour + ":" + minutes

            self.text_accident_timestamp_value.text = date + time
            # -----------------------------------------------------------

            # Casualties
            # -----------------------------------------------------
            self.casualty_number = str(results_list[0][5])
            self.label_casualties_value.text = self.casualty_number
            self.casualties_old = int(results_list[0][5])
            # -----------------------------------------------------

            # Severely Injured
            # -----------------------------------------------------------
            self.severely_number = str(results_list[0][6])
            self.label_severely_injured_value.text = self.severely_number
            self.severely_old = int(results_list[0][6])
            # -----------------------------------------------------------

    def save(self):

        if(self.ID==-1): pass
        if(self.erro==1): pass

        else:
            control = 0

            if(len(self.text_accident_timestamp_value.text)<16):
                process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

            if(self.text_accident_description_value.text!="" and self.text_accident_description_value.text!=self.description_old):
                self.description_old = self.text_accident_description_value.text
                control = 1

            if(self.text_accident_km_value.text!="" and self.text_accident_km_value.text!=self.km_old):
                self.km_old = self.text_accident_km_value.text
                control = 1

            if(self.text_accident_location_value.text!="" and self.text_accident_location_value.text!=self.location_text_old):
                control = 1

                # new road ID
                location_id_new = get_query_result("SELECT IdVia FROM Vias Where Nome = '" + self.text_accident_location_value.text + "';")

                # "concelho" and "tipo" of the currently stored road data
                location_concelho = get_query_result("SELECT IdConcelho FROM Vias Where IdVia = '" + str(self.location_id_old) + "';")[0][0]
                location_tipo = get_query_result("SELECT Tipo FROM Vias Where IdVia = '" + str(self.location_id_old) + "';")[0][0]
                
                if(len(location_id_new)==0): # it's a new road

                    max_id = get_query_result("SELECT MAX(IdVia) FROM Vias;")[0][0]
                    get_query_result("INSERT INTO Vias (IdVia, Nome, IdConcelho, Tipo) Values (" + str(max_id+1) + ", '" + self.text_accident_location_value.text + "', " + str(location_concelho) + ", '" + location_tipo + "'); COMMIT;")
                    self.location_id_old = max_id+1

                else: # it's an already stored road
                    self.location_id_old = location_id_new[0][0]

            if(len(self.text_accident_timestamp_value.text)==16 and self.text_accident_timestamp_value.text!=self.timestamp_old):
                
                self.timestamp_old = self.text_accident_timestamp_value.text
                control = 1

                # invert the timestamp
                year = str(self.timestamp_old).split(" ")[0].split("/")[2]
                month = str(self.timestamp_old).split(" ")[0].split("/")[1]
                day = str(self.timestamp_old).split(" ")[0].split("/")[0]

                date = year + "/" + month + "/" + day + " "

                # Time
                hour = str(self.timestamp_old).split(" ")[1].split(":")[0]
                minutes = str(self.timestamp_old).split(" ")[1].split(":")[1]

                time = hour + ":" + minutes
                self.timestamp_old = date + time

            if(self.severely_number!=str(self.severely_old)):
                self.severely_old = int(self.severely_number)
                control = 1

            if(self.casualty_number!=str(self.casualties_old)):
                self.casualties_old = int(self.casualty_number)
                control = 1

            if(control==0): pass
            
            else:
                get_query_result("UPDATE Acidentes SET Natureza = '" + self.description_old + "', IdVia = " + str(self.location_id_old) + ", Km = " + str(self.km_old) + ", DataHora = '" + self.timestamp_old + "', Mortos = " + str(self.casualties_old) + ", FeridosGraves = " + str(self.severely_old) + " WHERE IdAcidente = " + self.ID + "; COMMIT;")
                process = Popen(['python3', 'police_successful.py'], stdout=PIPE, stderr=PIPE)
                self.id_search()

    def concelho_search(self):

        if(self.text_concelho_search.text==""):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

        else:
            results = get_query_result("SELECT * FROM concelhos WHERE Nome = '" + self.text_concelho_search.text + "';")
            print(results)
            if(len(results)==0):
                process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)
            else:
                process = Popen(['python3', 'police_concelhos.py', self.text_concelho_search.text], stdout=PIPE, stderr=PIPE)

    def decrease_severely_injured(self):

        if(self.label_severely_injured_value.text=="-" or self.severely_number=="0"): return

        self.severely_number = str(int(self.severely_number)-1)
        self.label_severely_injured_value.text = self.severely_number

    def increase_severely_injured(self):

        if(self.label_severely_injured_value.text=="-"): return

        self.severely_number = str(int(self.severely_number)+1)
        self.label_severely_injured_value.text = self.severely_number

    def decrease_casualties(self):

        if(self.label_severely_injured_value.text=="-" or self.casualty_number=="0"): return

        self.casualty_number = str(int(self.casualty_number)-1)
        self.label_casualties_value.text = self.casualty_number

    def increase_casualties(self):

        if(self.label_severely_injured_value.text=="-"): return

        self.casualty_number = str(int(self.casualty_number)+1)
        self.label_casualties_value.text = self.casualty_number

    def update_padding(self, text_input, *args): # align text within a textinput field

        if(text_input.text==""):
            text_input.hint_text = "Teste"
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached)
        text_input.padding_x = (text_input.width - text_width)/2

    def update_padding_and_format(self, text_input, *args): # routine to take care of the date and time formats, as well as thei alignment

        if(self.ID!=""):
        
                aux = ""
                for i in self.text_accident_timestamp_value.text:
                    if(not (""+i).isdigit() and (""+i)!="/" and (""+i)!=":" and (""+i)!=" "): 
                        self.erro = 1
                        continue
                    aux += i

                for i in range(len(self.text_accident_timestamp_value.text)): 
                    if(self.text_accident_timestamp_value.text[i]=="/" and i!=2 and i!=5): 
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                for i in range(len(self.text_accident_timestamp_value.text)): 
                    if(self.text_accident_timestamp_value.text[i]==":" and i!=13): 
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)
                
                for i in range(len(self.text_accident_timestamp_value.text)): 
                    if(self.text_accident_timestamp_value.text[i]==" " and i!=10): 
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                if(len(self.text_accident_timestamp_value.text)==16):

                    if(self.erro==1): process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    if(int(self.text_accident_timestamp_value.text[0])>3):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)
                    
                    elif(int(self.text_accident_timestamp_value.text[3])>1):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[4])>2):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[6])>2):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[7])!=0):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[8])>1):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[11])>2):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[12])>3):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                    elif(int(self.text_accident_timestamp_value.text[14])>5):
                        process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

                self.text_accident_timestamp_value.text = aux

        else:

            # AUTOMATICALLY ADD "/", ":" OR " "
            #-------------------------------------------------------------
            if(len(text_input.text)==2 and "/" in text_input.text):
                text_input.text = text_input.text.replace('/','')

            if(len(text_input.text)==2 and "/" not in text_input.text):
                aux = text_input.text
                text_input.text = ""
                text_input.text = aux + "/"

            if(len(text_input.text)<=5 and text_input.text.count('/')>1):
                text_input.text = text_input.text[:-1]

            if(len(text_input.text)==5 and text_input.text.count('/')==1):
                aux = text_input.text
                text_input.text = ""
                text_input.text = aux + "/"

            # take care of the time format
            if(len(text_input.text)==13 and ":" not in text_input.text):
                aux = text_input.text
                text_input.text = ""
                text_input.text = aux + ":"

            if(len(text_input.text)==13 and ":" in text_input.text):
                text_input.text = text_input.text.replace(':','')
            #-------------------------------------------------------------

            # ELIMINATE INVALID CHARACTERS
            #--------------------------------------------------------------------
            aux = ""
            for i in range(len(text_input.text)):

                if(text_input.text[i]==" "):
                    if(i==10): aux += text_input.text[i]
                    else: continue

                elif(text_input.text[i]=="/"):
                    if(i==2 or i==5): aux += text_input.text[i]
                    else: continue

                elif(text_input.text[i]==":"):
                    if(i==13): aux += text_input.text[i]
                    else: continue

                elif(not (text_input.text[i]).isdigit()): # a forbidden character
                    continue

                else: aux += text_input.text[i]

            text_input.text = aux
            #--------------------------------------------------------------------

            # TOO MANY NUMBERS
            #----------------------------------------------------------------------------------------
            # take care of the date
            if(text_input.text.count('/')==1 and len(text_input.text.split("/")[0])>2):
                text_input.text = text_input.text[:2] + "/"

            if(text_input.text.count('/')==2 and len(text_input.text.split("/")[1])>2):
                text_input.text = text_input.text[:5] + ""

            if(len(text_input.text)>10 and text_input.text[10]!=' '):
                text_input.text = text_input.text[:10]

            # take care of the time
            if(text_input.text.count(':')==1 and len(text_input.text.split(" ")[1].split(":")[0])>2):
                text_input.text = text_input.text[:13] + ":"

            if(len(text_input.text)>16):
                text_input.text = text_input.text[:16]
            #----------------------------------------------------------------------------------------

            # RANGES EXCEEDED
            #--------------------------------------------------------------------------------------------------------------------------------------------
            # day outside of range
            if(len(text_input.text)==3 and (int(text_input.text.split("/")[0])>31 or int(text_input.text.split("/")[0])<0)):
                text_input.text = ""

            # month outside of range
            if(len(text_input.text)==6 and (int(text_input.text.split("/")[1])>12 or int(text_input.text.split("/")[1])<0)):
                text_input.text = text_input.text[:3]

            # year outside of range
            if(len(text_input.text)==10 and (int(text_input.text.split("/")[2])>2019 or int(text_input.text.split("/")[2])<1500)):
                text_input.text = text_input.text[:6]

            # hour outside of range
            if(len(text_input.text)==14 and (int(text_input.text.split(" ")[1].split(":")[0])>23 or int(text_input.text.split(" ")[1].split(":")[0])<0)):
                text_input.text = text_input.text[:11]

            # minutes outside of range
            if(len(text_input.text)==16 and (int(text_input.text.split(" ")[1].split(":")[1])>59 or int(text_input.text.split(" ")[1].split(":")[1])<0)):
                text_input.text = text_input.text[:14]
            #--------------------------------------------------------------------------------------------------------------------------------------------
        

        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached)
        text_input.padding_x = (text_input.width - text_width)/2

class MyApp(App): # main class
    def build(self):
        self.title = 'Cliente Polícia - Pesquisar Acidentes'
        self.load_kv('kv/police_search.kv')
        return PoliceSearch()

if __name__ == "__main__":
    MyApp().run()
