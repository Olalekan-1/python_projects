import random

from kivy import platform
from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
from kivy.core.window import Window

from kivy.app import App
from kivy.graphics import Line, Color, Quad, Triangle
from kivy.properties import NumericProperty, Clock
from kivy.uix.widget import Widget



class MainWidget(Widget):
    from actions import on_keyboard_down, on_keyboard_up, on_touch_down, on_touch_up
    from transform import transform, transform_2D, perspective

    perspective_y = NumericProperty(0)
    perspective_x = NumericProperty(0)

    vertical_space = .1
    vertical_lines = []
    NB_of_lines = 15

    Horizontal_space = .1
    NB_of_Hor_lines = 17
    Horizontal_lines = []

    current_offset = 0
    current_y_loop = 0

    current_offset_x = 0
    current_speed_x = 0
    SPEED_X = 1


    tiles = []
    tiles_cordinates = []
    NB_TILES = 6

    SHIP_WIDTH = .1
    SHIP_HEIGHT = 0.035
    SHIP_BASE_Y = 0.04
    ship = None
    ship_coordinates = [(0, 0), (0, 0), (0, 0)]

    def __init__(self, **kwargs):

        super(MainWidget, self).__init__(**kwargs)
        self.init_vertical_lines()
        self.init_Horizontal_line()
        self.init_tiles()
        self.pre_fill_tiles_coordinates()
        self.init_ship()
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

    def init_ship(self):
        with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle()

    def update_ship(self):
        center_x = self.width / 2
        base_y = self.SHIP_BASE_Y * self.height
        ship_half_width = self.SHIP_WIDTH * self.width / 2
        ship_height = self.SHIP_HEIGHT * self.height

        self.ship_coordinates[0] = (center_x - ship_half_width, base_y)
        self.ship_coordinates[1] = (center_x, base_y + ship_height)
        self.ship_coordinates[2] = (center_x + ship_half_width, base_y)

        x1, y1 = self.transform(*self.ship_coordinates[0])
        x2, y2 = self.transform(*self.ship_coordinates[1])
        x3, y3 = self.transform(*self.ship_coordinates[2])

        self.ship.points = [x1, y1, x2, y2, x3, y3]

    def check_ship_collision(self):
        for i in range(0, len(self.tiles_coordinates)):
            ti_x, ti_y = self.tiles_coordinates[i]
            if ti_y > self.current_y_loop + 1:
                return False
            if self.check_ship_collision_with_tile(ti_x, ti_y):
                return True
        return False

    def check_ship_collision_with_tile(self, ti_x, ti_y):
        xmin, ymin = self.get_tile_coordinates(ti_x, ti_y)
        xmax, ymax = self.get_tile_coordinates(ti_x + 1, ti_y + 1)
        for i in range(0, 3):
            px, py = self.ship_coordinates[i]
            if xmin <= px <= xmax and ymin <= py <= ymax:
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
        min_index = -int(self.NB_of_lines / 2) + 1
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

    def pre_fill_tiles_coordinates(self):
        for i in range(0, 10):
            self.tiles_cordinates.append((0, i))

    def gene_rate_tile_cordinate(self):

        last_y = 0
        last_x = 0

        for i in range(len(self.tiles_cordinates)-1, -1, -1):
            if self.tiles_cordinates[i][1] < self.current_y_loop:
                del self.tiles_cordinates[i]

        if len(self.tiles_cordinates) > 1:
            last_cord = self.tiles_cordinates[-1]
            last_x = last_cord[0]
            last_y = last_cord[1] + 1

        for i in range(len(self.tiles_cordinates), self.NB_TILES):
            r = random.randint(0, 2)


            min_index = -int(self.NB_of_lines / 2) + 1
            max_index = min_index + self.NB_of_lines - 1

            if last_x <= min_index:
                r = 1
            if last_x >= max_index:
                r = 2

            self.tiles_cordinates.append((last_x, last_y))
            if r == 1:
                last_x += 1
                self.tiles_cordinates.append((last_x, last_y))
                last_y += 1
                self.tiles_cordinates.append((last_x, last_y))
            if r == 2:
                last_x -= 1
                self.tiles_cordinates.append((last_x, last_y))
                last_y += 1
                self.tiles_cordinates.append((last_x, last_y))
            last_y += 1


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
        self.update_ship()

        speed_y = 0.2 * self.height / 100
        self.current_offset += speed_y * time_factor

        spacing_y = self.Horizontal_space * self.height
        if self.current_offset >= spacing_y:
            self.current_offset -= spacing_y
            self.current_y_loop += 1
            self.gene_rate_tile_cordinate()

        speed_x = self.current_speed_x * self.width / 100
        self.current_offset_x += speed_x * time_factor

        if not self.check_ship_collision():
            print("Game Over!")

class GalaxyApp(App):
    pass


GalaxyApp().run()
