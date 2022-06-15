import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
import math

class MainScreen(Screen):
    pass

class FirstWindow(Screen):
    def Ras1(self):
        v1 = self.ids.input1.text
        v2 = self.ids.input2.text
        r1 = ((int(v1) * int(v2)) + (int(v1) * int(v2)*10/100))
        r11 = (math.ceil(r1/6)*6)
        r2 = int(r11/6)
        self.ids.palki.text = "НАДО: \nПЛАШКИ: " + str(r11) + "\nПОДДОНЫ: " + str(r2)
   
class SecondWindow(Screen):
    def Ras2(self):
        v1 = self.ids.input3.text
        v2 = self.ids.input4.text
        r1 = ((int(v1) * int(v2)) + (int(v1) * int(v2)*10/100))
        r11 = (math.ceil(r1/6)*6)
        r2 = int(r11/6)
        self.ids.palki1.text = "НАДО: \nПЛАШКИ: " + str(r11) + "\nПОДДОНЫ: " + str(r2)

class ThirdWindow(Screen):
    def Ras3(self):    
        v1 = self.ids.input5.text
        v2 = self.ids.input6.text
        v3 = self.ids.input7.text
        r1 = ((int(v1) * int(v2)) + (int(v1) * int(v2)*10/100))
        r11 = (math.ceil(r1/6)*6)
        r111 = int(r11/6)
        r2 = ((int(v1) * int(v3)) + (int(v1) * int(v3)*10/100))
        r22 = (math.ceil(r2/6)*6)
        r222 = int(r22/6)
        self.ids.palki2.text = "Надо: \nПЛАШКИ: " + str(r11) + "\nПОДДОНЫ: " + str(r111) + "\nПЛАШКИ: " + str(r22) + "\nПОДДОНЫ: " + str(r222)

class ResultScreen(Screen):    
    def on_press(self):
        self.ids.recup_infos.text = App.get_running_app().root.ids.First.ids.palki.text

class ResultScreen1(Screen):
    def on_press1(self):
        self.ids.res.text = App.get_running_app().root.ids.Second.ids.palki1.text

class ResultScreen2(Screen):
    def on_press2(self):
        self.ids.res1.text = App.get_running_app().root.ids.Third.ids.palki2.text

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('gg.kv')

class Zeher(App):

    def build(self):
        return kv
    
if __name__ == '__main__':
    Zeher().run()