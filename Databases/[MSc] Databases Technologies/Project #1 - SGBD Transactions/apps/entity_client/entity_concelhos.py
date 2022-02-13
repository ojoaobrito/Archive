# import kivy stuff
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import sys

# import utilities
from client import get_query_result
from subprocess import Popen, PIPE

from kivy.config import Config
Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '650')

class EntityConcelhos(ScrollView):
    
    def __init__(self, testes, **kwargs):
        super().__init__(**kwargs)
        # get the data from the "concelho" given
        data = get_query_result("SELECT * FROM acidentes WHERE IdVia IN (SELECT IdVia FROM vias WHERE IdConcelho = (SELECT IdConcelho FROM concelhos WHERE Nome =  '" + sys.argv[1] + "'))")
        testes = []
        for i in range(len(data)):
            testes.append([])

            # date and time
            year = str(data[i][1]).split(" ")[0].split("-")[0]
            month = str(data[1][1]).split(" ")[0].split("-")[1]
            day = str(data[1][1]).split(" ")[0].split("-")[2]

            date = day + "/" + month + "/" + year + " "

            # Time
            hour = str(data[1][1]).split(" ")[1].split(":")[0]
            minutes = str(data[1][1]).split(" ")[1].split(":")[1]

            time = hour + ":" + minutes
            date = day + "/" + month + "/" + year + " " + hour + ":" + minutes

            testes[i].append("ID: " + str(data[i][0]) + " | " + date + " | IdVia: " + str(data[i][2]) + " | \"" + data[i][3] + "\" | KM: " + str(data[i][4]) + " | M.: " + str(data[i][5]) + " | FG.: " + str(data[i][6]))

        for teste in testes:
            self.ids.box.add_widget(Label(text=teste[0],font_size=17,size_hint_y=None,height=50, width=300, color=(0.0, 0.0, 0.4, 1.0)))

class MyApp(App): # main class
    def build(self):
        self.title = 'Resultados'
        self.load_kv('kv/entity_concelhos.kv')
        return EntityConcelhos([])

if __name__ == "__main__":
    MyApp().run()