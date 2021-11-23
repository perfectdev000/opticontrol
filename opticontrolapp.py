import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config


class OptiControl(Widget):
    btn_Pre_Process = ObjectProperty(None)
    btn_Analysis_1 = ObjectProperty(None)
    btn_Visualise_1 = ObjectProperty(None)
    btn_Analysis_2 = ObjectProperty(None)
    btn_Visualise_2 = ObjectProperty(None)
    layout_preprocess = ObjectProperty(None)
    layout_analysis1 = ObjectProperty(None)
    layout_visualise1 = ObjectProperty(None)
    layout_analysis2 = ObjectProperty(None)
    layout_visualise2 = ObjectProperty(None)

    def clear_color_btn(self):
        self.btn_Pre_Process.background_color = 0,0,0,1
        self.btn_Analysis_1.background_color = 0,0,0,1
        self.btn_Visualise_1.background_color = 0,0,0,1
        self.btn_Analysis_2.background_color = 0,0,0,1
        self.btn_Visualise_2.background_color = 0,0,0,1

    def set_heigth_to_zero(self):
        self.layout_preprocess.height = 0
        self.layout_analysis1.height = 0
        self.layout_visualise1.height = 0
        self.layout_analysis2.height = 0
        self.layout_visualise2.height = 0

    def click_btn_Pre_Process(self):
        self.clear_color_btn()
        self.set_heigth_to_zero()
        self.btn_Pre_Process.background_color = 0,0,255,1
        self.layout_preprocess.height = self.height
        return

    def click_btn_Analysis_1(self):
        self.clear_color_btn()
        self.set_heigth_to_zero()
        self.btn_Analysis_1.background_color = 0,0,255,1
        self.layout_analysis1.height = self.height
        return

    def click_btn_Visualise_1(self):
        self.clear_color_btn()
        self.set_heigth_to_zero()
        self.btn_Visualise_1.background_color = 0,0,255,1
        self.layout_visualise1.height = self.height
        return

    def click_btn_Analysis_2(self):
        self.clear_color_btn()
        self.set_heigth_to_zero()
        self.btn_Analysis_2.background_color = 0,0,255,1
        self.layout_analysis2.height = self.height
        return

    def click_btn_Visualise_2(self):
        self.clear_color_btn()
        self.set_heigth_to_zero()
        self.btn_Visualise_2.background_color = 0,0,255,1
        self.layout_visualise2.height = self.height
        return

class OptiControlApp(App):
    def build(self):
        Window.size = (1024,600)
        Window.clearcolor = (0.2, 0.2, 0.2, 1)
        return OptiControl()


if __name__ == "__main__":
    OptiControlApp().run()