from kivy import platform
from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
from kivy.core.window import Window

from kivy.app import App
from kivy.graphics import Line, Color, Quad
from kivy.properties import NumericProperty, Clock
from kivy.uix.widget import Widget


class MainWidget(Widget):
    from actions import on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up
    from transform import transform, transform_2D, perspective

    perspective_y = NumericProperty(0)
    perspective_x = NumericProperty(0)

    vertical_space = .15
    vertical_lines = []
    NB_of_lines = 5

    Horizontal_space = .1
    NB_of_Hor_lines = 9
    Horizontal_lines = []

    current_offset = 0
    current_y_loop = 0

    current_offset_x = 0
    current_speed_x = 0
    SPEED_X = 2


    tiles = []
    tiles_cordinates = []
    NB_TILES = 4

    def __init__(self, **kwargs):

        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_Horizontal_line()
        self.init_tiles()
        self.gene_rate_tile_cordinate()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1 / 60)

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self.on_keyboard_down)
        self._keyboard.unbind(on_key_up=self.on_keyboard_down)
        self._keyboard = None

    def is_desktop(self):
        if platform in ("linux", "win", "macosx"):
            return True
        return False

    def getLineX(self, index):
        central_x = self.perspective_x
        spacing = self.vertical_space * self.width
        offset = index - 0.5
        x = central_x + offset * spacing + self.current_offset_x
        return x

    def getLineY(self, index):
        spacing_y = self.Horizontal_space * self.height
        y = index * spacing_y - self.current_offset
        return y

    def init_vertical_lines(self):

        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_of_lines):
                self.vertical_lines.append(Line())

    def update_vertical_lines(self):
        min_index = - int(self.NB_of_lines / 2) + 1
        max_index = min_index + self.NB_of_lines

        for i in range(min_index, max_index):
            x = self.getLineX(i)
            x1, y1 = self.transform(x, 0)
            x2, y2 = self.transform(x, self.height)
            self.vertical_lines[i].points = [x1, y1, x2, y2]

    def init_Horizontal_line(self):

        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_of_Hor_lines):
                self.Horizontal_lines.append(Line())

    def update_Horizontal_line(self):
        min_index = - int(self.NB_of_lines / 2) + 1
        max_index = min_index + self.NB_of_lines - 1

        xmin = self.getLineX(min_index)
        xmax = self.getLineX(max_index)
        for i in range(0, self.NB_of_lines):
            y = self.getLineY(i)
            x1, y1 = self.transform(xmin, y)
            x2, y2 = self.transform(xmax, y)
            self.Horizontal_lines[i].points = [x1, y1, x2, y2]

    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(0, self.NB_TILES):
                self.tiles.append(Quad())

    def gene_rate_tile_cordinate(self):
        for i in range(0, self.NB_TILES):
            self.tiles_cordinates.append((0, i))


    def get_tile_cordinate(self, x, y):
        y = y - self.current_y_loop
        cord_x = self.getLineX(x)
        cord_y = self.getLineY(y)

        return cord_x, cord_y

    def update_tiles(self):
        for i in range(0, self.NB_TILES):
            tile_cordinates = self.tiles_cordinates[i]
            xmin, ymin = self.get_tile_cordinate(tile_cordinates[0], tile_cordinates[1])
            xmax, ymax = self.get_tile_cordinate(tile_cordinates[0] + 1, tile_cordinates[1] + 1)

            x0, y0 = self.transform(xmin, ymin)
            x1, y1 = self.transform(xmin, ymax)
            x2, y2 = self.transform(xmax, ymax)
            x3, y3 = self.transform(xmax, ymin)

            self.tiles[i].points = [x0, y0, x1, y1, x2, y2, x3, y3]

    def update(self, dt):
        time_factor = dt * 60
        self.update_vertical_lines()
        self.update_Horizontal_line()
        self.update_tiles()
        self.current_offset += 1 * time_factor

        spacing_y = self.Horizontal_space * self.height
        if self.current_offset >= spacing_y:
            self.current_offset -= spacing_y
            self.current_y_loop += 1
        self.current_offset_x += self.current_speed_x * time_factor


class GalaxyApp(App):
    pass


GalaxyApp().run()
