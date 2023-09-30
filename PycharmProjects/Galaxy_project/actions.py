from kivy.uix.relativelayout import RelativeLayout


def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    if keycode[1] == 'h':
        self.current_speed_x = self.SPEED_X
    elif keycode[1] == 'l':
        self.current_speed_x = - self.SPEED_X
    return True


def on_keyboard_up(self, keyboard, keycode):
    self.current_speed_x = 0
    return True


def on_touch_down(self, touch):
    if not self.game_over_state and self.game_has_started_state:
        if touch.x < self.width / 2:
            self.current_speed_x = self.SPEED_X
        else:
            self.current_speed_x = - self.SPEED_X

    return super(RelativeLayout, self).on_touch_down(touch)


def on_touch_up(self, touch):
    self.current_speed_x = 0