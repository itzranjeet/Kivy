from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window

Builder.load_file('./OpenXApp.kv')
Window.size = (750, 550)

class MainScreen(Widget):
    pass

class SimpleWidget(Widget):
    pass

class OpenXApp(App):
    def build(self):
        return MainScreen()

    def generate_xosc(self, *args):
        print("It's Babaji")
        

if __name__ == '__main__':
    OpenXApp().run()