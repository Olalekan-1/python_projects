from kivy.app import App
from kivy.graphics.context import Clock
from kivy.graphics.vertex_instructions import Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
#from kivy.lang import Builder

class Main(App):
    pass


class canvas_Ex(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.velx = dp(50)
        self.vely = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1/900000000000000)

    def on_size(self, *args):
        #print("my sizes are " + str(self.width) +" for width and " + str(self.height) + " for heaight")
        self.ball.pos = self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2

    class canvas_Ex2(BoxLayout):
        pass


    def update(self, dt):
        #print(" i am updated")
        x, y = self.ball.pos
        x += self.velx
        y += self.vely

        if x > self.width - self.ball_size:
            self.velx = - self.velx
        if y > self.height - self.ball_size:
            self.vely = - self.vely
        if y < 0:
            self.vely = - self.vely
        if x < 0:
            self.velx = - self.velx


        self.ball.pos = (x, y)


"""
class GridExample(GridLayout):
    count = 1
    my_text = StringProperty(str(count))

    def Button_clicked(self):
        self.count += 1
        self.my_text = str(self.count)
        print(self.count)

    def toggleButton(self, my_state):
        print(my_state.state)
        if my_state.state == "normal":
            my_state.text = "OFF"
        else:
            my_state.text = "ON"


#class Widget(Widget):
    #pass


#class CanvasEx(Widget):
    #pass



"""



Main().run()
