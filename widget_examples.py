from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty

Builder.load_file("widget_examples.kv")

class WidgetsExample(GridLayout):

    toggle = BooleanProperty(False)

    count = 1
    my_text = StringProperty("1")

    # slider_value = 50
    # slider_value_txt = StringProperty("50")

    text_input_str = StringProperty("foo")

    def on_button_click(self):
        print('Button clicked')
        if self.toggle:
            self.count +=1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print(widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.toggle = False
        else:
            widget.text = "ON"
            self.toggle = True

    def on_switch_active(self, widget):
        print(widget.active)

    # def on_slider_value(self, widget):
    #     print(int(widget.value))
        # self.slider_value = int(widget.value)
        # self.slider_value_txt = str(self.slider_value)

    def on_text_validate(self, widget):
        self.text_input_str = widget.text
