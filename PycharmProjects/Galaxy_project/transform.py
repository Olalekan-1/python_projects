def transform(self, x: int, y: int):
    return self.perspective(x, y)
    #return self.transform_2D(x, y)


def transform_2D(self, x, y):
    return int(x), int(y)


def perspective(self, x, y):
    y_line = y * self.perspective_y / self.height
    if y_line > self.perspective_y:
        y_line = self.perspective_y

    x_dif = x - self.perspective_x
    y_dif = self.perspective_y - y_line
    y_proportion = y_dif / self.perspective_y
    y_proportion = pow(y_proportion, 4)

    trans_x = self.perspective_x + x_dif * y_proportion
    trans_y = self.perspective_y - y_proportion * self.perspective_y

    return (trans_x, trans_y)