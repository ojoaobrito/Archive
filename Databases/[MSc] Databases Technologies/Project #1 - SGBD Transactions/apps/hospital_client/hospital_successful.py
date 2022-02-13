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
import sys

from kivy.config import Config
Config.set('graphics', 'width', '250')
Config.set('graphics', 'height', '175')

class HospitalSuccessful(Widget):
    
    def ok_button(self):
        sys.exit()

class MyApp(App): # main class
    def build(self):
        self.title = 'Successo'
        self.load_kv('kv/hospital_successful.kv')
        return HospitalSuccessful()

if __name__ == "__main__":
    MyApp().run()