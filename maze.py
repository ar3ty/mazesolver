from graphics import Line, Point
import time

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            l = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
            self._win.draw_line(l)
        if self.has_top_wall:
            l = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
            self._win.draw_line(l)
        if self.has_right_wall:
            l = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
            self._win.draw_line(l)
        if self.has_bottom_wall:
            l = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
            self._win.draw_line(l)
        
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        l = Line(Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2), Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2))
        self._win.draw_line(l, color)

class Maze:
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column = []
            for j in range(self._num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win == None: 
            return
        x1 = i * self._cell_size_x + self._x1
        y1 = j * self._cell_size_y + self._y1
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win == None: 
            return
        self._win.redraw()
        time.sleep(0.05)




