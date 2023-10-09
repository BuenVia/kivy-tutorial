from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.graphics.vertex_instructions import Line, Rectangle
from kivy.graphics.context_instructions import Color
from kivy.metrics import dp

Builder.load_file("canvas_examples.kv")

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 10, 400, 500), width=2)
            Color(0, 1, 0)
            Line(circle=(400, 200, 80), width=2)
            Line(rectangle=(700, 500, 150, 100), width=5)
            self.rect = Rectangle(pos=(700, 200), size=(150, 100))
    
    def on_button_a_click(self):
        x, y = self.rect.pos
        w, h = self.rect.size
        if x < (self.width - w):
            x += dp(10)
            self.rect.pos = (x, y)
        # else:
        #     self.rect.pos = (self.width - (w + 50), y)
    
class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas: