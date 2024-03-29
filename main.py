from kivy.app import App
# from kivy.metrics import dp
# from kivy.uix.button import Button
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.pagelayout import PageLayout
# from kivy.uix.widget import Widget
# from kivy.properties import StringProperty, BooleanProperty
from kivy.properties import ObjectProperty
from navigation_screen_manager import NavigationScreenManager
from canvas_examples import *

class MyScreenManager(NavigationScreenManager):
    pass

class TheLabApp(App):
    manager = ObjectProperty(None)

    def build(self):
        self.manager = MyScreenManager()
        return self.manager
        # return CanvasExample7()

if __name__ == "__main__":
    TheLabApp().run()