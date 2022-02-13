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
from subprocess import Popen, PIPE

from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '450')

class PoliceMain(Widget):
    
    def new_accident(self):
        process = Popen(['python3', 'police_new.py'], stdout=PIPE, stderr=PIPE)

    def search_accident(self):
        process = Popen(['python3', 'police_search.py'], stdout=PIPE, stderr=PIPE)

class MyApp(App): # main class
    def build(self):
        self.title = 'Cliente Polícia'
        self.load_kv('kv/police_main.kv')
        return PoliceMain()

if __name__ == "__main__":
    MyApp().run()