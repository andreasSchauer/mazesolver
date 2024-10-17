from graphics import Line, Point

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

  
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        
        left = Line(Point(x1, y1), Point(x1, y2))
        top = Line(Point(x1, y1), Point(x2, y1))
        right = Line(Point(x2, y1), Point(x2, y2))
        bottom = Line(Point(x1, y2), Point(x2, y2))

        if self.has_left_wall:
            self._win.draw_line(left)
        else:
            self._win.draw_line(left, "white")

        if self.has_top_wall:
            self._win.draw_line(top)
        else:
            self._win.draw_line(top, "white")

        if self.has_right_wall:
            self._win.draw_line(right)
        else:
            self._win.draw_line(right, "white")

        if self.has_bottom_wall:
            self._win.draw_line(bottom)
        else:
            self._win.draw_line(bottom, "white")

  
    def draw_move(self, to_cell, undo=False):
        if undo:
            fill_color = "gray"
        else:
            fill_color = "red"

        center1_x = (self._x1 + self._x2) / 2
        center1_y = (self._y1 + self._y2) / 2
        center2_x = (to_cell._x1 + to_cell._x2) / 2
        center2_y = (to_cell._y1 + to_cell._y2) / 2
        line = Line(Point(center1_x, center1_y), Point(center2_x, center2_y))
        self._win.draw_line(line, fill_color)