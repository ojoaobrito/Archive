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

class PoliceNew(Widget):
    
    label_severely_injured_value = ObjectProperty(None)
    label_casualties_value = ObjectProperty(None)

    text_accident_description_value = ObjectProperty(None)
    text_accident_location_value = ObjectProperty(None)
    text_accident_km_value = ObjectProperty(None)
    text_accident_concelho_value = ObjectProperty(None)
    text_accident_timestamp_value = ObjectProperty(None)
    
    severely_number = "0"
    casualty_number = "0"

    def decrease_severely_injured(self):
        
        if(self.severely_number=="0"): return

        self.severely_number = str(int(self.severely_number)-1)
        self.label_severely_injured_value.text = self.severely_number

    def increase_severely_injured(self):

        self.severely_number = str(int(self.severely_number)+1)
        self.label_severely_injured_value.text = self.severely_number

    def decrease_casualties(self):
        
        if(self.casualty_number=="0"): return

        self.casualty_number = str(int(self.casualty_number)-1)
        self.label_casualties_value.text = self.casualty_number

    def increase_casualties(self):
        
        self.casualty_number = str(int(self.casualty_number)+1)
        self.label_casualties_value.text = self.casualty_number
    
    def save_accident(self):
        
        if(self.text_accident_description_value.text==""):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

        elif(self.text_accident_location_value.text==""):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

        elif(self.text_accident_km_value.text==""):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

        elif(self.text_accident_concelho_value.text==""):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)

        elif(len(self.text_accident_timestamp_value.text)<16):
            process = Popen(['python3', 'police_input_warning.py'], stdout=PIPE, stderr=PIPE)
        
        else:
            new_id = get_query_result("SELECT MAX(IdAcidente) FROM Acidentes;")[0][0] + 1
            new_road_id = get_query_result("SELECT IdVia FROM Vias Where Nome = '" + self.text_accident_location_value.text + "';")
            new_concelho_name = get_query_result("SELECT IdConcelho FROM Concelhos Where Nome = '" + self.text_accident_concelho_value.text + "';")

            if(len(new_concelho_name)==0):
                new_concelho_id = get_query_result("SELECT MAX(IdConcelho) FROM Concelhos;")[0][0] + 1
                get_query_result("INSERT INTO Concelhos(IdConcelho, Nome, IdDistrito) VALUES (" + str(new_concelho_id) + ", '" + self.text_accident_concelho_value.text + "',1); COMMIT;")
            
            else:
                new_concelho_id = new_concelho_name[0][0]

            if(len(new_road_id)==0): # it's a new road
                new_new_road_id = get_query_result("SELECT MAX(IdVia) FROM Vias;")[0][0] + 1
                get_query_result("INSERT INTO Vias(IdVia, Nome, IdConcelho, Tipo) VALUES (" + str(new_new_road_id) + ", '" + self.text_accident_location_value.text + "'," + str(new_concelho_id) + ", 'None'); COMMIT;")
                get_query_result("INSERT INTO Acidentes(IdAcidente, DataHora, IdVia, Natureza, Km, Mortos, FeridosGraves) VALUES (" + str(new_id) + ", '" + self.text_accident_timestamp_value.text + "', " + str(new_new_road_id) + ", '" + self.text_accident_description_value.text + "', " + self.text_accident_km_value.text + ", " + self.casualty_number + ", " + self.severely_number + "); COMMIT;")

            else:
                get_query_result("INSERT INTO Vias(IdVia, Nome, IdConcelho, Tipo) VALUES (" + str(new_road_id[0][0]) + ", '" + self.text_accident_location_value.text + "'," + str(new_concelho_id) + ", 'None'); COMMIT;")
                get_query_result("INSERT INTO Acidentes(IdAcidente, DataHora, IdVia, Natureza, Km, Mortos, FeridosGraves) VALUES (" + str(new_id) + ", '" + self.text_accident_timestamp_value.text + "', " + str(new_road_id[0][0]) + ", '" + self.text_accident_description_value.text + "', " + self.text_accident_km_value.text + ", " + self.casualty_number + ", " + self.severely_number + "); COMMIT;")
        
            process = Popen(['python3', 'police_successful.py'], stdout=PIPE, stderr=PIPE)

    def update_padding(self, text_input, *args): # align text within a textinput field
        
        text_width = text_input._get_text_width(
            text_input.text,
            text_input.tab_width,
            text_input._label_cached)
        text_input.padding_x = (text_input.width - text_width)/2

    def update_padding_and_format(self, text_input, *args): # routine to take care of the date and time formats, as well as thei alignment
        
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
        
        self.title = 'Cliente Polícia - Novo Acidente'
        self.load_kv('kv/police_new.kv')
        return PoliceNew()

if __name__ == "__main__":
    MyApp().run()