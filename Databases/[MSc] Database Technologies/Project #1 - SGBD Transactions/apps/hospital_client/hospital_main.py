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

from kivy.config import Config
Config.set('graphics', 'height', '650')

class HospitalMain(Widget):

    text_id_search = ObjectProperty(None)
    label_concelho_search = ObjectProperty(None)
    label_accident_description_value = ObjectProperty(None)
    label_accident_location_value = ObjectProperty(None)
    label_accident_timestamp_value = ObjectProperty(None)
    label_accident_km_value = ObjectProperty(None)
    label_casualties_value = ObjectProperty(None)
    label_severely_injured_value = ObjectProperty(None)
    text_concelho_search = ObjectProperty(None)

    severely_number = "0"
    casualty_number = "0"
    severely_old = -1
    casualties_old = -1
    erro = 0
    ID = ""

    def id_search(self):

        if(self.text_id_search.text==""):
            process = Popen(['python3', 'hospital_input_warning.py'], stdout=PIPE, stderr=PIPE)

        else:
            self.ID = self.text_id_search.text

            # retireve our results
            results_list = get_query_result("SELECT * FROM acidentes WHERE IdAcidente=" + self.ID + ";") # format = [(IdAcidente, DataHora, IdVia, Natureza, Km, Mortos, FeridosGraves)]
            
            # Description
            # ---------------------------------------------------------------------------------------------------------------------
            self.label_accident_description_value.text = results_list[0][3]
            # ---------------------------------------------------------------------------------------------------------------------

            # Location
            # ---------------------------------------------------------------------------------------------------------------------
            location = get_query_result("SELECT IdVia, Nome FROM Vias Where IdVia = (SELECT IdVia FROM Acidentes Where IdAcidente = " + self.ID + ");")
            self.label_accident_location_value.text = location[0][1]
            # ---------------------------------------------------------------------------------------------------------------------

            # KM
            # ---------------------------------------------------------------------------------------------------------------------
            self.label_accident_km_value.text = str(results_list[0][4])
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

            self.label_accident_timestamp_value.text = date + time
            # -----------------------------------------------------------

            # Casualties
            # -----------------------------------------------------
            self.label_casualties_value.text = str(results_list[0][5])
            self.casualties_old = int(results_list[0][5])
            # -----------------------------------------------------

            # Severely Injured
            # -----------------------------------------------------------
            self.label_severely_injured_value.text = str(results_list[0][6])
            self.severely_old = int(results_list[0][6])
            # -----------------------------------------------------------

    def save(self):
        
        if(self.ID==-1): pass
        if(self.erro==1): pass

        else:
            control = 0

            if(self.label_severely_injured_value!=str(self.severely_old)):
                self.severely_old = int(self.severely_number)
                control = 1

            if(self.label_casualties_value!=str(self.casualties_old)):
                self.casualties_old = int(self.casualty_number)
                control = 1

            if(control==0): pass
            
            else:
                get_query_result("UPDATE Acidentes SET Mortos = " + str(self.casualties_old) + ", FeridosGraves = " + str(self.severely_old) + " WHERE IdAcidente = " + self.ID + "; COMMIT;")
                process = Popen(['python3', 'hospital_successful.py'], stdout=PIPE, stderr=PIPE)
                self.id_search()

    def concelho_search(self):

        if(self.text_concelho_search.text==""):
            process = Popen(['python3', 'hospital_input_warning.py'], stdout=PIPE, stderr=PIPE)

        else:
            results = get_query_result("SELECT * FROM concelhos WHERE Nome = '" + self.text_concelho_search.text + "';")
            print(results)
            if(len(results)==0):
                process = Popen(['python3', 'hospital_input_warning.py'], stdout=PIPE, stderr=PIPE)
            else:
                process = Popen(['python3', 'hospital_concelhos.py', self.text_concelho_search.text], stdout=PIPE, stderr=PIPE)

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

class MyApp(App): # main class
    def build(self):
        self.title = 'Cliente Hospital'
        self.load_kv('kv/hospital_main.kv')
        return HospitalMain()

if __name__ == "__main__":
    MyApp().run()