from graphics import Line, Point
import time, random

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
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        l = Line(Point(self._x1, self._y1), Point(self._x1, self._y2))
        if self.has_left_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
        l = Line(Point(self._x1, self._y1), Point(self._x2, self._y1))
        if self.has_top_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
        l = Line(Point(self._x2, self._y1), Point(self._x2, self._y2))
        if self.has_right_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
        l = Line(Point(self._x1, self._y2), Point(self._x2, self._y2))
        if self.has_bottom_wall:
            self._win.draw_line(l)
        else:
            self._win.draw_line(l, "white")
        
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        l = Line(Point((self._x1 + self._x2)/2, (self._y1 + self._y2)/2), Point((to_cell._x1 + to_cell._x2)/2, (to_cell._y1 + to_cell._y2)/2))
        self._win.draw_line(l, color)

class Maze:
    def __init__(self, x1, y1, num_cols, num_rows, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        if self._seed != None:
            random.seed(self._seed)

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

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_go = []
            if j - 1 >= 0: 
                if self._cells[i][j-1].visited == False:
                    to_go.append((i, j-1))
            if i + 1 < self._num_cols:  
                if self._cells[i+1][j].visited == False:
                    to_go.append((i+1, j))
            if j + 1 < self._num_rows:  
                if self._cells[i][j+1].visited == False:
                    to_go.append((i, j+1))
            if i - 1 >= 0: 
                if self._cells[i-1][j].visited == False:
                    to_go.append((i-1, j))
            if len(to_go) == 0:
                self._draw_cell(i,j)
                return
            dest = random.randrange(0, len(to_go))
            x, y = to_go[dest][0], to_go[dest][1]
            if y < j and x == i:
                self._cells[i][j].has_top_wall = False
                self._cells[x][y].has_bottom_wall = False
            elif x > i and j == y:
                self._cells[i][j].has_right_wall = False
                self._cells[x][y].has_left_wall = False
            elif y > j and x == i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[x][y].has_top_wall = False
            else:
                self._cells[i][j].has_left_wall = False
                self._cells[x][y].has_right_wall = False
            self._break_walls_r(x,y)

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def solve(self):
        l = Line(Point(self._x1 + self._cell_size_x/2, self._y1 + self._cell_size_y/2), Point(self._x1 + self._cell_size_x/2, self._y1 - self._cell_size_y/2))
        self._win.draw_line(l, "red")
        res = self._solve_bfs(0,0)
        l = Line(Point(self._x1 + self._cell_size_x * (self._num_cols - 0.5), self._y1 + self._cell_size_y * (self._num_rows - 0.5)), Point(self._x1 + self._cell_size_x * (self._num_cols - 0.5), self._y1 + self._cell_size_y * (self._num_rows + 0.5)))
        self._win.draw_line(l, "red")
        return res
    
    def _solve_dfs_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        if j - 1 >= 0: 
            if self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j-1])
                res = self._solve_dfs_r(i, j-1)
                if res:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
        if i + 1 < self._num_cols:  
            if self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
                self._cells[i][j].draw_move(self._cells[i+1][j])
                res = self._solve_dfs_r(i+1, j)
                if res:
                    return True
                self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
        if j + 1 < self._num_rows:  
            if self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
                self._cells[i][j].draw_move(self._cells[i][j+1])
                res = self._solve_dfs_r(i, j+1)
                if res:
                    return True
                self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
        if i - 1 >= 0: 
            if self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
                self._cells[i][j].draw_move(self._cells[i-1][j])
                res = self._solve_dfs_r(i-1, j)
                if res:
                    return True
                self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
        return False
    
    
    def _solve_bfs(self, x, y):
        self._animate()
        to_visit = [(x,y)]
        paths = {}
        res = False
        while len(to_visit) > 0:
            i,j = to_visit.pop()
            self._cells[i][j].visited = True
            if i == self._num_cols - 1 and j == self._num_rows - 1:
                res = True
                break
            if j - 1 >= 0: 
                if self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
                    self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
                    self._animate()
                    to_visit.insert(0,(i,j-1))
                    paths[(i,j-1)] = (i,j)
            if i + 1 < self._num_cols:  
                if self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
                    self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
                    self._animate()
                    to_visit.insert(0,(i+1,j))
                    paths[(i+1,j)] = (i,j)
            if j + 1 < self._num_rows:  
                if self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
                    self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
                    self._animate()
                    to_visit.insert(0,(i,j+1))
                    paths[(i,j+1)] = (i,j)
            if i - 1 >= 0: 
                if self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
                    self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
                    self._animate()
                    to_visit.insert(0,(i-1,j))
                    paths[(i-1,j)] = (i,j)
        if res == True:
            current = (self._num_cols - 1, self._num_rows - 1)
            while current != (0,0):
                previous = paths[current]
                self._cells[current[0]][current[1]].draw_move(self._cells[previous[0]][previous[1]])
                current = previous
        return res